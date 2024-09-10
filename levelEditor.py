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
# Tile types
WATER = 0
SAND = 1
GRASS = 2
STONE = 3

# Define colors for each tile ID
TILE_COLORS = {
    WATER: (0, 0, 128),
    SAND: (96, 64, 0),
    GRASS: (0, 128, 0),
    STONE: (96, 96, 96),
    # Add more colors as needed
}

# Define constants
COLUMNS = 20 #number of columns of tilemaps to make big map
NUM_MAPS = 300 #total number of maps

TILE_SIZE = 32
SMALL_TILE_SIZE = 2
TILEMAP_WIDTH = 40
TILEMAP_HEIGHT = 32

# Global Variables
bigMap = False
cursorState = 0
statusString = "test"
statusTimeout = 0
statusLimit = 100
id = 0
#random terrain generation function
#adjust octaves, persistence, lacunarity for different results
import numpy as np
import random
from noise import snoise2

# Define terrain types
WATER = 0
SAND = 1
GRASS = 2
STONE = 3

def prompt_for_details():
        details = {}
        details['buildings'] = messagebox.askyesno("Configuration", "Include buildings? (yes/no)")
        details['building_count'] = int(simpledialog.askstring("Configuration", "Max buildings/map [3] (integer):").strip())
        details['rivers'] = messagebox.askyesno("Configuration", "Include rivers? (yes/no)")
        details['river_width'] = float(simpledialog.askstring("Configuration", "River width [1] (integer):").strip())
        details['terrain_scale'] = float(simpledialog.askstring("Configuration", "Terrain scale [10.0] (float):").strip())
        details['octaves'] = int(simpledialog.askstring("Configuration", "Octaves [6] (integer):").strip())
        details['persistence'] = float(simpledialog.askstring("Configuration", "Persistence [0.5] (float):").strip())
        return details

def create_terrain_map(width, height,settings, scale=10.0, octaves=6, persistence=0.5, lacunarity=2.0, num_rivers=5, num_buildings=10):
    
    """Generate a terrain map with given dimensions using Perlin noise and add buildings."""
    terrain_map = np.zeros((height, width), dtype=np.int32)
    if settings["buildings"] == True:
        num_buildings=random.randint(0,int(settings["building_count"]))
    elif settings["buildings"] == False:
        num_buildings = 0
    if settings["rivers"] == True:
        num_rivers=random.randint(0,4)
    elif settings["rivers"] == False:
        num_rivers = 0
    scale = settings["terrain_scale"]
    octaves = settings["octaves"]
    persistence = settings["persistence"]
    river_width = int(settings["river_width"])
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
            #else:
            #    terrain_map[y, x] = STONE
    
    # Add rivers to the terrain map
    for _ in range(num_rivers):
        start_pos = (random.randint(0, width-1), random.randint(0, height-1))
        
        terrain_map = add_river(terrain_map, start_pos, width, height,river_width)
    
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

    return terrain_map

def add_river(terrain_map, start_pos, width, height,river_width):
    """Add a river to the terrain map from the start position."""
    x, y = start_pos
    river_width = river_width
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
            terrain_map[y, x] = STONE

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

def render_tilemap(tilemap, bigMap, id):
    if not bigMap:
        TILE_SIZE = 32
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
                pygame.draw.rect(screen, color, pygame.Rect(tilePos[0], tilePos[1], TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(tilePos[0], tilePos[1], TILE_SIZE, TILE_SIZE),1)


        # Display status texts
        text_surface = my_font.render("map: " + str(id), True, (255,255,255))
        text_surface2 = my_font.render("F2/F3 select map | +/- to zoom in/out", True, (255,255,255))
        
        screen.blit(text_surface, (0, screenyDim - 50))
        screen.blit(text_surface2, (150, screenyDim - 50))
        screen.blit(status_text, (0, screenyDim - 100))

        pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), TILE_SIZE/4 + 1)
        cursor_color = TILE_COLORS.get(cursorState, (255, 255, 255))  # Default to white if cursorState is unknown
        pygame.draw.circle(screen, cursor_color, pygame.mouse.get_pos(), TILE_SIZE/4)

    else:
        # Large map rendering
        screen.fill(background_color)  # Clear the screen
        for y in range(tilemap.shape[0]):
            for x in range(tilemap.shape[1]):
                tile_id = tilemap[y, x]
                color = TILE_COLORS.get(tile_id, (255, 255, 255))  # Default to white if tile_id is unknown
                pygame.draw.rect(screen, color, pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        tilemaps = parse_tilemap_data('levels.h')
        small_tilemaps = create_small_tilemaps(tilemaps)
        num_tiles = len(small_tilemaps)
        num_columns = COLUMNS
        for idx in range(num_tiles):
            row = idx // num_columns
            col = idx % num_columns
            tile_rect = pygame.Rect(col * TILEMAP_WIDTH * TILE_SIZE, row * TILEMAP_HEIGHT * TILE_SIZE, TILEMAP_WIDTH * TILE_SIZE, TILEMAP_HEIGHT * TILE_SIZE)
            
            if idx == id:
                index_text = small_my_font.render(str(idx), True, (255, 0, 0))
                pygame.draw.rect(screen, (255, 0, 0), tile_rect, 2)  # Draw rectangle around the tilemap
            else:
                index_text = small_my_font.render(str(idx), True, (255, 255, 255))
                pygame.draw.rect(screen, (128, 128, 128), tile_rect, 1)  # Draw rectangle around the tilemap
            screen.blit(index_text, (col * TILEMAP_WIDTH * TILE_SIZE + 5, row * TILEMAP_HEIGHT * TILE_SIZE + 5))
        text_surface = my_font.render("map: " + str(id), True, (255,255,255))
        text_surface2 = my_font.render("F2/F3 select map | +/- to enter/exit map", True, (255,255,255))
        text_surface2b = my_font.render("MWHEEL scales up/down",True,(255,255,255))
        text_surface3 = my_font.render("F11 go to map [id]",True,(255,255,255))
        text_surface4 = my_font.render("F12 randomize maps",True,(255,255,255))
        #text_surface5 = my_font.render(statusString, True, (255,255,255))
        
        screen.blit(text_surface, (screenxDim - 100, screenyDim - 50))
        screen.blit(text_surface2, (screenxDim - 300, screenyDim - 100))
        screen.blit(text_surface2b, (screenxDim - 300, screenyDim - 75))
        screen.blit(text_surface3, (screenxDim - 300, screenyDim - 150))
        screen.blit(text_surface4, (screenxDim - 300, screenyDim - 200))
        screen.blit(status_text, (screenxDim - 350, screenyDim - 250))
        
    pygame.display.flip()

def render_map(bigMap,id):
    tilemaps = parse_tilemap_data('levels.h')
    small_tilemaps = create_small_tilemaps(tilemaps)
    large_tilemap = generate_large_tilemap(small_tilemaps)
    render_tilemap(large_tilemap, bigMap, id)

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
my_font = pygame.font.SysFont('Arial', 20)
small_my_font = pygame.font.SysFont('Arial', 10)
data, details = readFile(0)
status_text = updateStatusLine(f"loaded map: level{id}.h")
yTiles = int(details[1])
xTiles = int(details[2])
maxTiles = 3
screenyDim = 1280
screenxDim = 1900

screen = pygame.display.set_mode((screenxDim, screenyDim),pygame.RESIZABLE)
Window.from_display_module().maximize()


# Main loop
running = True
mouse1Held = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            #print(event.scancode)
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
                status_text = updateStatusLine("saved map: level" + str(id) + ".h, exiting editor")
                running = False
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
                status_text = updateStatusLine("saved map: level" + str(id) + ".h")
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
            if event.scancode == 60:
                #print("next map")
                writeToFile(id)
                #remove_all_h_files("./")
                id = id + 1
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id - 1) + ", loaded map: level" + str(id) + ".h")
                writeToFile(id)
                #print(newLevel)
                if newLevel == True:
                    concat_and_pack()
                    newLevel = False
            if event.scancode == 59:
                #print("prev map")
                writeToFile(id)
                #remove_all_h_files("./")
                id = id - 1
                if id < 0:
                    id = 0
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                status_text = updateStatusLine("saved map: " + str(id) + ", loaded map: level" + str(id) + ".h")
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not bigMap:
            mouse1Held = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and not bigMap:
            mouse1Held = False

        if mouse1Held == True:
            if bigMap:
                break
            mousePosition = pygame.mouse.get_pos()
            try:
                tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
#                print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                data[tileMapPosition_y][tileMapPosition_x] = cursorState
                status_text = updateStatusLine("placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                statusTimeout = 0
            except:
                tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                status_text = updateStatusLine("cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                statusTimeout = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if bigMap:
                    SMALL_TILE_SIZE = SMALL_TILE_SIZE + 1
                    if SMALL_TILE_SIZE > 5:
                        SMALL_TILE_SIZE = 5
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
            if event.button == 1:
                if bigMap:
                    break
                mousePosition = pygame.mouse.get_pos()
                try:
                    tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                    tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    #print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    data[tileMapPosition_y][tileMapPosition_x] = cursorState
                    status_text = updateStatusLine("placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    statusTimeout = 0
                except:
                    tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                    tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    status_text = updateStatusLine("cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    statusTimeout = 0
    
    render_map(bigMap,id)
    pygame.display.flip()  # Ensure the display updates

time.sleep(1)
pygame.quit()
