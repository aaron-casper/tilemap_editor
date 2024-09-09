import re
import numpy as np
import pygame
from pygame.locals import *

# Define constants
TILE_SIZE = 4
TILEMAP_WIDTH = 40
TILEMAP_HEIGHT = 32

# Define colors for each tile ID
TILE_COLORS = {
    0: (0, 0, 128),
    1: (96, 64, 0),
    2: (0, 128, 0),
    3: (96, 96, 96),
    # Add more colors as needed
}

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

        # Clean the data by removing curly braces and splitting by commas
        data = data.strip('{}')
        data = data.replace('},{', ' ').replace(',', ' ')

        # Debugging: Print extracted data and its length
        print(f"Tilemap Name: {name}")
        print(f"Height: {height}, Width: {width}")
        print(f"Data Length: {len(data)}")
        print(f"Data: {data[:100]}...")  # Print first 100 characters for brevity

        if not data:
            print(f"No data found for tilemap {name}.")
            continue

        # Convert the cleaned data into a numpy array
        try:
            expected_size = height * width
            data_array = np.fromstring(data, dtype=np.int32, sep=' ')
            if data_array.size != expected_size:
                print(f"Data size mismatch: expected {expected_size}, got {data_array.size}")
                continue
            
            tiles = data_array.reshape((height, width))
            tilemaps[name] = tiles
        except ValueError as e:
            print(f"Error parsing tilemap {name}: {e}")

    return tilemaps

# Function to create smaller tilemaps from the tilemap data
def create_small_tilemaps(tilemaps):
    small_tilemaps = []

    for name, tilemap in tilemaps.items():
        height, width = tilemap.shape
        for y in range(0, height, TILEMAP_HEIGHT):
            for x in range(0, width, TILEMAP_WIDTH):
                small_tilemap = tilemap[y:y+TILEMAP_HEIGHT, x:x+TILEMAP_WIDTH]
                small_tilemaps.append(small_tilemap)

    return small_tilemaps

# Function to generate a large tilemap from small tilemaps
def generate_large_tilemap(small_tilemaps):
    num_tiles = len(small_tilemaps)
    num_columns = 10
    num_rows = (num_tiles + num_columns - 1) // num_columns

    large_tilemap = np.zeros((num_rows * TILEMAP_HEIGHT, num_columns * TILEMAP_WIDTH), dtype=np.int32)

    for idx, small_tilemap in enumerate(small_tilemaps):
        row = idx // num_columns
        col = idx % num_columns
        large_tilemap[row*TILEMAP_HEIGHT:(row+1)*TILEMAP_HEIGHT, col*TILEMAP_WIDTH:(col+1)*TILEMAP_WIDTH] = small_tilemap

    return large_tilemap

# Function to render the tilemap using Pygame
def render_tilemap(tilemap, small_tilemaps):
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Arial', 30)
    screen_width, screen_height = tilemap.shape[1] * TILE_SIZE, tilemap.shape[0] * TILE_SIZE
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Predefine rects with colors
    tile_rects = {}
    for tile_id, color in TILE_COLORS.items():
        tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        tile_surface.fill(color)
        tile_rects[tile_id] = tile_surface

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.scancode == 62:
                    reload_map()


        
        # Draw the tilemap
        for y in range(tilemap.shape[0]):
            for x in range(tilemap.shape[1]):
                tile_id = tilemap[y, x]
                if tile_id in tile_rects:
                    screen.blit(tile_rects[tile_id], (x * TILE_SIZE, y * TILE_SIZE))
        
        # Draw the index for each small tilemap
        num_tiles = len(small_tilemaps)
        num_columns = 10
        for idx in range(num_tiles):
            row = idx // num_columns
            col = idx % num_columns
            tile_rect = pygame.Rect(col * TILEMAP_WIDTH * TILE_SIZE, row * TILEMAP_HEIGHT * TILE_SIZE, TILEMAP_WIDTH * TILE_SIZE, TILEMAP_HEIGHT * TILE_SIZE)
            pygame.draw.rect(screen, (128, 128, 128), tile_rect, 2)  # Draw rectangle around the tilemap
            index_text = my_font.render(str(idx), True, (255, 255, 255))
            screen.blit(index_text, (col * TILEMAP_WIDTH * TILE_SIZE + 5, row * TILEMAP_HEIGHT * TILE_SIZE + 5))
        
        pygame.display.flip()

    pygame.quit()

def reload_map():
        tilemaps = parse_tilemap_data('levels.h')
        small_tilemaps = create_small_tilemaps(tilemaps)

        # Generate a large tilemap
        large_tilemap = generate_large_tilemap(small_tilemaps)

        # Render the large tilemap using Pygame
        render_tilemap(large_tilemap, small_tilemaps)

if __name__ == "__main__":
    # Parse the tilemap data from the file
    tilemaps = parse_tilemap_data('levels.h')

    # Check if tilemaps is populated
    if not tilemaps:
        print("No tilemaps found. Check the file and regular expression.")
    else:
        # Create smaller tilemaps
        reload_map()
