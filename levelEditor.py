import pygame
from pygame.locals import *
from pygame._sdl2 import Window
#import zipfile
import os
import glob
import time
import re
import numpy as np
import random
from noise import snoise2
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

# Define constants for world size
COLUMNS = 5 #number of columns of tilemaps to make big map
NUM_MAPS = 25 #total number of maps

#Define constants for map size
TILEMAP_WIDTH = 40
TILEMAP_HEIGHT = 32

#CONST dimensions for sprite and tile size
DIMENSION_X = 16
DIMENSION_Y = 16
#-------
#tile defintions
#-------
# Constants for tile/terrain types, need to be identified in spritemap
WATER = 1792
SAND = 768
GRASS = 0
STONE = 192
WOOD = 234
#^ this is all that is required for the terrain generator

# Define failback colors for each tile ID
TILE_COLORS = {
    WATER: (0, 0, 128),
    SAND: (96, 64, 0),
    GRASS: (0, 96, 0),
    STONE: (96, 96, 96),
    WOOD: (64,32,0),
    # Add more colors as needed
}



TILE_SIZE = DIMENSION_X
SMALL_TILE_SIZE = 2


# Global Variables
bigMap = False
cursorState = 0
statusString = "test"
statusTimeout = 0
statusLimit = 100
id = 0
maxTiles = 0
#SPRITE DIMENSIONS IN PACKED SPRITESHEET, IMPORTANT
tile_size = (DIMENSION_X, DIMENSION_Y)
tile_file = ('./Tileset.png')


class TileSelector:
    def __init__(self, tileset_path, tile_size, screen, position=(0, 0)):
        self.tile_size = tile_size
        self.screen = screen
        self.position = position  # Position where tileset is drawn
        self.tileset = pygame.image.load(tileset_path).convert_alpha()
        
        # Get tileset dimensions
        tileset_rect = self.tileset.get_rect()
        self.tileset_width = tileset_rect.width
        self.tileset_height = tileset_rect.height

        # Calculate the number of tiles
        self.num_tiles_x = self.tileset_width // tile_size
        self.num_tiles_y = self.tileset_height // tile_size

        # Selected tile
        self.selected_tile = None

        # Highlight color
        self.highlight_color = (255, 0, 0)  # Red for highlighting

    def draw(self):
        """Draw the tileset and highlight the selected tile."""
        # Draw the tileset
        self.screen.blit(self.tileset, self.position)

        # Draw the highlight around the selected tile
        self.draw_highlight()

        # Draw the selected tile preview
        self.draw_selected_tile()

        # Draw the index of the selected tile
        self.draw_tile_index()

    def draw_highlight(self):
        """Draw a border around the selected tile."""
        if self.selected_tile is not None:
            tile_x, tile_y = self.selected_tile
            highlight_rect = pygame.Rect(
                self.position[0] + tile_x * self.tile_size,
                self.position[1] + tile_y * self.tile_size,
                self.tile_size,
                self.tile_size
            )
            pygame.draw.rect(self.screen, self.highlight_color, highlight_rect, 3)  # Border with thickness 3

    def draw_selected_tile(self):
        """Draw the selected tile preview on the screen."""
        if self.selected_tile is not None:
            tile_x, tile_y = self.selected_tile
            tile_rect = pygame.Rect(
                tile_x * self.tile_size,
                tile_y * self.tile_size,
                self.tile_size,
                self.tile_size
            )
            tile_image = self.tileset.subsurface(tile_rect)
            preview_position = (self.position[0] + self.tileset_width + 10, self.position[1] + 10)
            self.screen.blit(tile_image, preview_position)

    def draw_tile_index(self):
        """Draw the index of the selected tile on the screen."""
        if self.selected_tile is not None:
            tile_x, tile_y = self.selected_tile
            tile_index = tile_y * self.num_tiles_x + tile_x
            font = pygame.font.Font(None, 36)
            index_text = font.render(f"Tile Index: {tile_index}", True, (0, 0, 0))
            preview_position = (self.position[0] + self.tileset_width + 10, self.position[1] + 10 + self.tile_size + 20)
            self.screen.blit(index_text, preview_position)

    def handle_click(self, position):
        """Handle click events to select a tile."""
        global cursorState  # Access the global variable
        x, y = position
        # Adjust position based on tileset position on the screen
        x -= self.position[0]
        y -= self.position[1]

        if x < self.tileset_width and y < self.tileset_height:
            tile_x = x // self.tile_size
            tile_y = y // self.tile_size
            if 0 <= tile_x < self.num_tiles_x and 0 <= tile_y < self.num_tiles_y:
                self.selected_tile = (tile_x, tile_y)
                cursorState = tile_y * self.num_tiles_x + tile_x  # Update the global variable with the tile index

def prompt_for_details():
        details = {}
        details['buildings'] = messagebox.askyesno("Configuration", "Include buildings? (yes/no)")
        if details['buildings']:
            details['mazes'] = messagebox.askyesno("Configuration", "Mazes (yes/no)")
        elif not details['buildings']:
            details['mazes'] = False
        if details['buildings']:
            details['building_count'] = int(simpledialog.askstring("Configuration", "Max buildings/map [3] (integer):").strip())
        details['rivers'] = messagebox.askyesno("Configuration", "Include rivers? (yes/no)")
        if details['rivers']:
            details['river_width'] = float(simpledialog.askstring("Configuration", "River width [1] (integer):").strip())
        elif not details['rivers']:
            details['river_width'] = 0.0
        details['terrain_scale'] = float(simpledialog.askstring("Configuration", "Terrain scale [10.0] (float):").strip())
        details['octaves'] = int(simpledialog.askstring("Configuration", "Octaves [6] (integer):").strip())
        details['persistence'] = float(simpledialog.askstring("Configuration", "Persistence [0.5] (float):").strip())
        return details


def load_tiles(spritemap_path, tile_size):
    """
    Load tiles from a spritemap image.

    :param spritemap_path: Path to the spritemap image file.
    :param tile_size: Tuple (width, height) of each tile in the spritemap.
    :return: A list of pygame.Surface objects representing each tile.
    """
    
    spritemap = pygame.image.load(spritemap_path).convert_alpha()  # Load the spritemap with transparency support
    tile_width, tile_height = tile_size

    # Get dimensions of the spritemap
    spritemap_width, spritemap_height = spritemap.get_size()

    # Number of tiles per row and column
    num_tiles_x = spritemap_width // tile_width
    num_tiles_y = spritemap_height // tile_height

    # List to hold all tile surfaces
    tiles = []

    for y in range(num_tiles_y):
        for x in range(num_tiles_x):
            # Define the rect for the current tile
            tile_rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)

            # Create a new surface for the tile
            tile_surface = pygame.Surface((tile_width, tile_height), pygame.SRCALPHA)
            tile_surface.blit(spritemap, (0, 0), tile_rect)
            
            # Add the tile surface to the list
            tiles.append(tile_surface)

    return tiles

# Example usage
pygame.init()
screen = pygame.display.set_mode((800, 600))
tile_size = (DIMENSION_X, DIMENSION_Y)
tiles = load_tiles(tile_file, tile_size)
maxTiles = len(tiles) - 1

def generate_maze(width, height):
    # Ensure dimensions are even for the maze generation
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    # Create a grid filled with stone tiles (non-passable) using NumPy array
    maze = np.full((height, width), WOOD, dtype=int)
    
    # Define directions for moving in the maze (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Helper function to check if a cell is within the grid and is a stone tile
    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    # Depth-First Search to carve out the maze
    def carve_maze(cx, cy):
        maze[cy, cx] = GRASS  # Carve the current cell
        random.shuffle(directions)
        for direction in directions:
            nx, ny = cx + direction[0] * 2, cy + direction[1] * 2
            if in_bounds(nx, ny) and maze[ny, nx] == WOOD:
                # Carve the wall between the current cell and the next cell
                maze[cy + direction[1], cx + direction[0]] = GRASS
                carve_maze(nx, ny)

    # Start carving the maze from a random position
    start_x, start_y = random.randint(0, (width - 1) // 2) * 2, random.randint(0, (height - 1) // 2) * 2
    carve_maze(start_x, start_y)
    
    return maze

def add_maze_to_terrain(terrain_map, maze):
    """Add a maze to the existing terrain map, only carving through stone tiles."""
    t_height, t_width = terrain_map.shape
    m_height, m_width = maze.shape
    
    # Compute the offset to center the maze on the terrain map
    offset_x = (t_width - m_width) // 2
    offset_y = (t_height - m_height) // 2
    
    for y in range(m_height):
        for x in range(m_width):
            if 0 <= y + offset_y < t_height and 0 <= x + offset_x < t_width:
                # Only place maze tiles on stone tiles in the terrain map
                if maze[y, x] == GRASS:  # Maze paths
                    if terrain_map[y + offset_y, x + offset_x] == WOOD:
                        terrain_map[y + offset_y, x + offset_x] = GRASS

def create_terrain_map(width, height, settings, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0, num_rivers=5, num_buildings=10):
    """Generate a terrain map with given dimensions using Perlin noise and add buildings."""
    terrain_map = np.zeros((height, width), dtype=np.int32)
    
    if settings["buildings"]:
        num_buildings = random.randint(0, int(settings["building_count"]))
    else:
        num_buildings = 0
    
    if settings["rivers"]:
        num_rivers = random.randint(0, 4)
    else:
        num_rivers = 0
    
    scale = settings["terrain_scale"]
    octaves = settings["octaves"]
    persistence = settings["persistence"]
    river_width = int(settings["river_width"])
    
    if settings["mazes"]:
        maze = generate_maze(width, height)
    
    # Generate terrain using Perlin noise
    base = random.randint(0, 100000) * 2
    for y in range(height):
        for x in range(width):
            noise_value = snoise2(x / scale,
                                  y / scale,
                                  octaves=octaves,
                                  persistence=persistence,
                                  lacunarity=lacunarity,
                                  repeatx=width,
                                  repeaty=height,
                                  base=base)
            
            normalized_value = (noise_value + 1) / 2

            if normalized_value < 0.2:
                terrain_map[y, x] = WATER
            elif normalized_value < 0.4:
                terrain_map[y, x] = SAND
            elif normalized_value < 0.6:
                terrain_map[y, x] = GRASS
            else:
                terrain_map[y, x] = STONE

    # Add rivers to the terrain map
    for _ in range(num_rivers):
        start_pos = (random.randint(0, width-1), random.randint(0, height-1))
        terrain_map = add_river(terrain_map, start_pos, width, height, river_width)
    
    # Add buildings to the terrain map
    for _ in range(num_buildings):
        while True:
            building_width = random.randint(5, 20)
            building_height = random.randint(5, 20)
            start_x = random.randint(0, width - building_width)
            start_y = random.randint(0, height - building_height)
            if can_place_building(terrain_map, start_x, start_y, building_width, building_height):
                terrain_map = add_building(terrain_map, start_x, start_y, building_width, building_height, width, height)
                break
    
    # Add maze to the terrain map if specified
    if settings["mazes"]:
        add_maze_to_terrain(terrain_map, maze)
    
    #print(terrain_map)
    return terrain_map

def add_river(terrain_map, start_pos, width, height, river_width):
    """Add a river to the terrain map from the start position."""
    x, y = start_pos
    length = random.randint(30, 100)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for _ in range(length):
        if 0 <= x < width and 0 <= y < height:
            for dx in range(-river_width, river_width + 1):
                for dy in range(-river_width, river_width + 1):
                    if 0 <= x + dx < width and 0 <= y + dy < height:
                        distance = np.sqrt(dx**2 + dy**2)
                        if distance <= river_width:
                            terrain_map[y + dy, x + dx] = WATER

            direction = random.choice(directions)
            x += direction[0]
            y += direction[1]

    return terrain_map

def add_building(terrain_map, start_x, start_y, width, height, terrain_width, terrain_height):
    """Add a rectangular building to the terrain map."""
    for y in range(start_y, min(start_y + height, terrain_height)):
        for x in range(start_x, min(start_x + width, terrain_width)):
            terrain_map[y, x] = WOOD

    return terrain_map

def can_place_building(terrain_map, start_x, start_y, width, height):
    """Check if a building can be placed at the specified location without overlapping water."""
    for y in range(start_y, min(start_y + height, terrain_map.shape[0])):
        for x in range(start_x, min(start_x + width, terrain_map.shape[1])):
            if terrain_map[y, x] == WATER:
                return False
    return True



def create_random_map(width, height,settings):
    """Generate a random tilemap with given dimensions."""
    #return np.random.randint(low=0, high=2 + 1, size=(height, width), dtype=np.int32)
    return create_terrain_map(width,height,settings)

def save_map_to_file(map_data, file_name, id):
    """Save the map data to a file."""
    with open(file_name, 'w') as f:
        height, width = map_data.shape
        id2 = str(id).zfill(3)
        outputString = f"int lvl0{id2}[{yTiles}][{xTiles}] =\n{{\n"
        f.write(outputString)
        for row in map_data:
            row_str = ','.join(map(str, row.flatten()))
            f.write(f'    {{{ row_str }}},\n')
        f.write('};\n')

def generate_and_save_maps(num_maps,settings):
    """Generate and save a number of random maps."""
    for i in range(num_maps):
        id = i
        map_data = create_random_map(TILEMAP_WIDTH, TILEMAP_HEIGHT,settings)
        save_map_to_file(map_data, f'levels/level{i:03d}.h', id)

def updateStatusLine(statusString):
    text_surface3 = my_font.render(statusString, True, (255,255,255))
    return text_surface3

def prompt_for_integer():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    user_input = simpledialog.askinteger("Input", "Go to map: ")
    if user_input is not None:
        return user_input
    return 0

def parse_tilemap_data(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Refined regular expression to match the tilemap data
    tilemap_pattern = re.compile(
        r'int\s+(\w+)\s*\[\s*(\d+)\s*\]\s*\[\s*(\d+)\s*\]\s*=\s*\{(.*?)\};',
        re.DOTALL
    )
    tilemaps = {}

    for match in tilemap_pattern.finditer(content):
        name = match.group(1)
        height = int(match.group(2))
        width = int(match.group(3))
        data = match.group(4).replace('\n', '').replace(' ', '')

        # Clean the data
        data = data.strip('{}').replace('},{', ' ').replace(',', ' ')

        # Convert the cleaned data into a numpy array
        try:
            expected_size = height * width
            data_array = np.fromstring(data, dtype=np.int32, sep=' ')
            if data_array.size != expected_size:
                #print(f"Data size mismatch: expected {expected_size}, got {data_array.size}")
                continue
            
            tiles = data_array.reshape((height, width))
            tilemaps[name] = tiles
        except ValueError as e:
            print(f"Error parsing tilemap {name}: {e}")

    return tilemaps

def create_small_tilemaps(tilemaps):
    small_tilemaps = []
    for name, tilemap in tilemaps.items():
        height, width = tilemap.shape
        for y in range(0, height, TILEMAP_HEIGHT):
            for x in range(0, width, TILEMAP_WIDTH):
                small_tilemap = tilemap[y:y+TILEMAP_HEIGHT, x:x+TILEMAP_WIDTH]
                small_tilemaps.append(small_tilemap)
    return small_tilemaps

def generate_large_tilemap(small_tilemaps):
    num_tiles = len(small_tilemaps)
    num_columns = COLUMNS
    num_rows = (num_tiles + num_columns - 1) // num_columns

    large_tilemap = np.zeros((num_rows * TILEMAP_HEIGHT, num_columns * TILEMAP_WIDTH), dtype=np.int32)

    for idx, small_tilemap in enumerate(small_tilemaps):
        row = idx // num_columns
        col = idx % num_columns
        large_tilemap[row*TILEMAP_HEIGHT:(row+1)*TILEMAP_HEIGHT, col*TILEMAP_WIDTH:(col+1)*TILEMAP_WIDTH] = small_tilemap

    return large_tilemap

#main map renderer
def render_tilemap(tilemap, tiles, bigMap, id):
    if not bigMap:
        TILE_SIZE = DIMENSION_X
        pygame.mouse.set_visible(False)
    elif bigMap:
        TILE_SIZE = SMALL_TILE_SIZE
        pygame.mouse.set_visible(True)
    # Use a background color to clear the screen
    background_color = (0, 0, 0)  # Black background

    if not bigMap:
        # Small map rendering
        screen.fill(background_color)  # Clear the screen

        for y, row in enumerate(data):
            for x, item in enumerate(row):
                tilePos = (x * TILE_SIZE, y * TILE_SIZE)
                color = TILE_COLORS.get(item, (255, 255, 255))  # Default to white if item is unknown
                #pygame.draw.rect(screen, color, pygame.Rect(tilePos[0], tilePos[1], TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(tilePos[0], tilePos[1], TILE_SIZE, TILE_SIZE),1)
                tile_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            
                # Draw the tile rectangle
                #pygame.draw.rect(screen, (255, 255, 255), tile_rect)  # White rectangle for the tile background

                # Draw the tile sprite on top of the rectangle
                #tile_sprite_rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
                tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
                cursor_tile = pygame.Surface((TILE_SIZE,TILE_SIZE))
                
                if 0 <= item < len(tiles):
                    tile_surface = tiles[item]
                    cursor_tile = tiles[cursorState]
                    tile_surface = pygame.transform.scale(tile_surface, tile_size)
                    screen.blit(tile_surface, (x * tile_size[0], y * tile_size[1]))
                    
        
        pygame.draw.rect(screen, (128,128,128), pygame.Rect(0, screenyDim - 151, 5000, screenyDim - 149))                    
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, screenyDim - 150, 5000, 5000))
        tile_selector.draw()            
        cursor_tile = pygame.transform.scale(cursor_tile, (128,128))
        screen.blit(cursor_tile, (screenxDim - 64, screenyDim - 64))
        # Display status texts
        
        text_surface = my_font.render("map: " + str(id), True, (255,255,255))
        text_surface2 = my_font.render("arrow keys select map | pgup/pgdn to zoom in/out | - to switch to world view", True, (255,255,255))
        text_surface3 = my_font.render("current tile: " + str(cursorState) , True, (255,255,255))
        
        screen.blit(text_surface, (0, screenyDim - 75))
        screen.blit(text_surface2, (150, screenyDim - 75))
        screen.blit(status_text, (0, screenyDim - 125))
        screen.blit(text_surface3, (68, screenyDim))
        display_tile = pygame.Surface((TILE_SIZE,TILE_SIZE))
        display_tile = tiles[cursorState]
        
        pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), int(tile_size[0]/2.5))
        cursor_color = TILE_COLORS.get(cursorState, (255, 255, 255))  # Default to white if cursorState is unknown
        pygame.draw.circle(screen, cursor_color, pygame.mouse.get_pos(), TILE_SIZE/4)
        display_tile = pygame.transform.scale(display_tile, (TILE_SIZE/2,TILE_SIZE/2))
        screen.blit(display_tile, ((pygame.mouse.get_pos()[0] - TILE_SIZE/4),(pygame.mouse.get_pos()[1] - TILE_SIZE/4)))
    else:
        # Large map rendering
        screen.fill(background_color)  # Clear the screen
        for y in range(tilemap.shape[0]):
            for x in range(tilemap.shape[1]):
                tile_id = tilemap[y, x]
                color = TILE_COLORS.get(tile_id, (255, 255, 255))  # Default to white if tile_id is unknown
                #pygame.draw.rect(screen, color, pygame.Rect(x * SMALL_TILE_SIZE, y * SMALL_TILE_SIZE, SMALL_TILE_SIZE, SMALL_TILE_SIZE))
                tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
                if 0 <= tile_id < len(tiles):
                    tile_surface = tiles[tile_id]
                    tile_surface = pygame.transform.scale(tile_surface, (SMALL_TILE_SIZE,SMALL_TILE_SIZE))
                    screen.blit(tile_surface, (x * SMALL_TILE_SIZE, y * SMALL_TILE_SIZE))
        tilemaps = parse_tilemap_data('levels.h')
        small_tilemaps = create_small_tilemaps(tilemaps)
        num_tiles = len(small_tilemaps)
        num_columns = COLUMNS
        for idx in range(num_tiles):
            row = idx // num_columns
            col = idx % num_columns
            tile_rect = pygame.Rect(col * TILEMAP_WIDTH * TILE_SIZE, row * TILEMAP_HEIGHT * TILE_SIZE, TILEMAP_WIDTH * TILE_SIZE, TILEMAP_HEIGHT * TILE_SIZE)
            #print(tile_rect)
            if idx == id:
                
                index_text = my_font.render(str(idx), True, (0, 0, 0))

                pygame.draw.rect(screen, (255, 0, 0), tile_rect, 3)  # Draw rectangle around the tilemap
            else:
                index_text = small_my_font.render(str(idx), True, (0, 0, 0))
                pygame.draw.rect(screen, (128, 128, 128), tile_rect, 1)  # Draw rectangle around the tilemap
            
            screen.blit(index_text, (col * TILEMAP_WIDTH * TILE_SIZE + 5, row * TILEMAP_HEIGHT * TILE_SIZE + 5))
        pygame.draw.rect(screen, (128,128,128), pygame.Rect(0, screenyDim - 151, 5000, screenyDim - 149))                    
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(0, screenyDim - 150, 5000, 5000))            
        # Display status texts
        
        text_surface = my_font.render("map: " + str(id), True, (255,255,255))
        text_surface2 = my_font.render("arrow keys select map | + to switch to map view | mousewheel zooms in/out", True, (255,255,255))
        
        text_surface3 = my_font.render("F11 go to map [id]",True,(255,255,255))
        text_surface4 = my_font.render("F12 randomize maps",True,(255,255,255))
        #text_surface5 = my_font.render(statusString, True, (255,255,255))
        
        screen.blit(text_surface, (0, screenyDim))
        screen.blit(text_surface2, (0, screenyDim - 30))
        
        screen.blit(text_surface3, (0, screenyDim - 90))
        screen.blit(text_surface4, (0, screenyDim - 120))
        screen.blit(status_text, (0, screenyDim - 150))
        
    pygame.display.flip()

def render_map(bigMap,id):
    tilemaps = parse_tilemap_data('levels.h')
    small_tilemaps = create_small_tilemaps(tilemaps)
    large_tilemap = generate_large_tilemap(small_tilemaps)
    render_tilemap(large_tilemap, spritemap, bigMap, id)

def concat_and_pack():
    filenames = glob.glob('levels/*.h')
    with open('levels.h', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())
                outfile.write('\n')

def remove_all_h_files(directory):
    pattern = os.path.join(directory, '**', '*.h')
    for file_path in glob.iglob(pattern, recursive=True):
        try:
            os.remove(file_path)
            print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def extract_files(zip_filename, files_to_extract, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        if isinstance(files_to_extract, str):
            files_to_extract = [files_to_extract]
        
        for file in files_to_extract:
            try:
                zipf.extract(file, path=output_dir)
                print(f"Extracted {file} to {output_dir}")
            except KeyError:
                print(f"Warning: '{file}' not found in the archive.")
    print(f"Extraction complete to: {output_dir}")

def create_zip_with_headers(zip_filename, directory):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.h'):
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, directory)
                    zipf.write(file_path, arcname=arcname)
    print(f"Created ZIP archive: {zip_filename}")

def writeToFile(id):
    id = str(id).zfill(3)
    levelname = "levels/level" + id + ".h"
    with open(levelname, 'w') as f:
        outputString = f"int lvl0{id}[{yTiles}][{xTiles}] =\n{{\n"
        for rowIndex, row in enumerate(data):
            outputString += "    { "
            outputString += ','.join(str(element) for element in row)
            outputString += " }"
            outputString += "," if rowIndex < len(data) else "\n"
            outputString += '\n'
        outputString += "};"
        f.write(outputString)

def readFile(id):
    id2 = str(id).zfill(3)
    levelname = f"levels/level{id2}.h"
    global newLevel
    newLevel = False
    try:
        f = open(levelname, 'r')
    except FileNotFoundError:
        print(f"{levelname} not found, blank template loaded")
        f = open("levels/level000.h", 'r')
        newLevel = True
    y = 0
    arr = None
    details = []
    for line in f:
        if newLevel:
            id = 0
            #newLevel = False
        id2 = str(id).zfill(4)
        levelName = f"lvl{id2}"
        if levelName in line:
            details = line.split(' ')[1].replace(']', '').split('[')
            arr = [[0 for _ in range(int(details[2]))] for _ in range(int(details[1]))]
        elif "{" in line and ',' in line:
            data = line.replace('{', '').replace('}', '').replace(', ', '').replace(' ', '').replace('\n', '').strip()
            row = data.split(',')
            arr[y] = [int(i) for i in row[0:-1]]
            y += 1
        elif "};" in line:
            break
    f.close()
    return arr, details

# Initialize Pygame
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('rubikbold', 20)
small_my_font = pygame.font.SysFont('rubikbold', 12)
data, details = readFile(0)
status_text = updateStatusLine(f"loaded map: level{id}.h")
yTiles = int(details[1])
xTiles = int(details[2])
screenyDim = 1280
screenxDim = 1900
screen = pygame.display.set_mode((screenxDim, screenyDim),pygame.RESIZABLE)
Window.from_display_module().maximize()
sprite_size = (DIMENSION_X, DIMENSION_Y)
spritemap = load_tiles(tile_file,tile_size)
tile_selector = TileSelector(tile_file, TILE_SIZE, screen, position=(screenxDim, 0))


# Main loop
running = True
mouse1Held = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
           # print(event.scancode)
            if event.key == pygame.K_F11:
                writeToFile(id) #save map before loading a new one
                mapSearch = prompt_for_integer()
                id = mapSearch
                data = readFile(id)
                data = data[0]
            if event.key == pygame.K_F6 or event.scancode == 45 or event.scancode == 86:
                #print("Zoom out")
                writeToFile(id)
                try:
                    os.remove('./levels.h')
                    statusTimeout = 0
                    status_text = updateStatusLine("removed old levels.h")
                    time.sleep(1) #give it a chance to clean up file                    
                except:
                    statusTimeout = 0
                    status_text = updateStatusLine("unable to remove old levels.h?")
                statusTimeout = 0
                status_text = updateStatusLine("packed all levels")
                concat_and_pack()
                bigMap = True
            if event.key == pygame.K_F7 or event.scancode == 46 or event.scancode == 87:
                #print("Zoom in")
                bigMap = False


            if event.scancode == 41:
                writeToFile(id)
                status_text = updateStatusLine("saved map: " + str(id) + ", exiting editor")
                running = False
            if event.scancode == 75: #pgup
                if not bigMap:
                    DIMENSION_X = DIMENSION_X + 1
                    DIMENSION_Y = DIMENSION_Y + 1
                    if DIMENSION_Y > 64:
                        DIMENSION_Y = 64
                    if DIMENSION_X > 64:
                        DIMENSION_X = 64
                    tile_size = (DIMENSION_X, DIMENSION_Y)
                    tiles = load_tiles(tile_file, tile_size)
            
            if event.scancode == 78: #pgdn
                if not bigMap:
                    DIMENSION_X = DIMENSION_X - 1
                    DIMENSION_Y = DIMENSION_Y - 1
                    if DIMENSION_Y < 16:
                        DIMENSION_Y = 16
                    if DIMENSION_X < 16:
                        DIMENSION_X = 16
                    tile_size = (DIMENSION_X, DIMENSION_Y)
                    tiles = load_tiles(tile_file, tile_size)

            if event.scancode == 62:
#                print("zip functionality disabled")
                try:
                    os.remove('./levels.h')
                    statusTimeout = 0
                    status_text = updateStatusLine("removed old levels.h")
                    time.sleep(1) #give it a chance to clean up file                    
                except:
                    statusTimeout = 0
                    status_text = updateStatusLine("unable to remove old levels.h?")
                statusTimeout = 0
                status_text = updateStatusLine("packed all levels")
                concat_and_pack()
                #zip files back up
                #create_zip_with_headers("./levels.zip","./")
                #remove_all_h_files("./")
            if event.scancode == 61:
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id))
                writeToFile(id)
            if event.scancode == 69:
                proceed = messagebox.askokcancel("PROCESSING","Generating maps may take a moment.\n\nClick OK to begin, or CANCEL to abort\n\nYou will be prompted for configuration details\nrecommended starting values are provided.\n\nYou will be notified when\nmap generation has completed.")
                if proceed:
                    settings = prompt_for_details()
                    #print(settings)
                    status_text = updateStatusLine("generated maps" )
                    generate_and_save_maps(NUM_MAPS,settings)
                    concat_and_pack()
                    messagebox.showinfo("PROCESSING","Done generating maps!")
                else:
                    break
             #arrow keys
            if event.scancode == 82:
            #up
                id2 = id
                id = id - COLUMNS
                if id < 0:
                    id = id2
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id2) + ", loaded map: " + str(id))
                #writeToFile(id)
                if newLevel == True:
                    concat_and_pack()
                    newLevel = False
            if event.scancode == 81:
            #DOWN
                writeToFile(id)
                id2 = id
                id = id + COLUMNS
                if id > NUM_MAPS:
                    id = id2     
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id2) + ", loaded map: " + str(id))
                #writeToFile(id)
                if newLevel == True:
                    concat_and_pack()
                    newLevel = False
            if event.scancode == 79:
                id2 = id
                #RIGHT
                writeToFile(id)
                #remove_all_h_files("./")
                id = id + 1
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id2) + ", loaded map: " + str(id))
                #writeToFile(id)
                #print(newLevel)
                if newLevel == True:
                    concat_and_pack()
                    newLevel = False
            if event.scancode == 80:
                id2 = id
                #LEFT
                writeToFile(id)
                #remove_all_h_files("./")
                id = id - 1
                if id < 0:
                    id = 0
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id2) + ", loaded map: " + str(id))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not bigMap:
            mouse1Held = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not bigMap:
            mouse1Held = False

        if mouse1Held == True:
            if bigMap:
                break
            mousePosition = pygame.mouse.get_pos()
            try:
                tileMapPosition_x = int(mousePosition[0] / DIMENSION_X)
                tileMapPosition_y = int(mousePosition[1] / DIMENSION_Y)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
#                print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                data[tileMapPosition_y][tileMapPosition_x] = cursorState
                status_text = updateStatusLine("placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                statusTimeout = 0
            except:
                tileMapPosition_x = int(mousePosition[0] / DIMENSION_X)
                tileMapPosition_y = int(mousePosition[1] / DIMENSION_Y)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                status_text = updateStatusLine("cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                statusTimeout = 0
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if bigMap:
                    SMALL_TILE_SIZE = SMALL_TILE_SIZE + 1
                    if SMALL_TILE_SIZE > 10:
                        SMALL_TILE_SIZE = 10

    
                cursorState = cursorState + 1
                if cursorState > maxTiles:
                    cursorState = 0
            
            if event.button == 5:
                if bigMap:
                    SMALL_TILE_SIZE = SMALL_TILE_SIZE - 1
                    if SMALL_TILE_SIZE < 1:
                        SMALL_TILE_SIZE = 1

    

                cursorState = cursorState - 1
                if cursorState < 0:
                    cursorState = maxTiles
            #print(event.button)
            #mouse1
            if event.button == 1:
                result = tile_selector.handle_click(event.pos)
                print(result)
                if bigMap:
                    break
                mousePosition = pygame.mouse.get_pos()
                try:
                    tileMapPosition_x = int(mousePosition[0] / DIMENSION_X)
                    tileMapPosition_y = int(mousePosition[1] / DIMENSION_Y)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    #print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    data[tileMapPosition_y][tileMapPosition_x] = cursorState
                    status_text = updateStatusLine("placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    statusTimeout = 0
                except:
                    tileMapPosition_x = int(mousePosition[0] / DIMENSION_X)
                    tileMapPosition_y = int(mousePosition[1] / DIMENSION_Y)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    status_text = updateStatusLine("cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    statusTimeout = 0
    
    render_map(bigMap,id)
    pygame.display.flip()  # Ensure the display updates

time.sleep(1)
pygame.quit()