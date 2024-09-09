import pygame
from pygame.locals import *
import zipfile
import os
import glob
import time
import re
import numpy as np

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
TILE_SIZE = 32
TILEMAP_WIDTH = 40
TILEMAP_HEIGHT = 32

# Global Variables
bigMap = False
cursorState = 0
statusString = "test"
statusTimeout = 0
statusLimit = 100
id = 0

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
    num_columns = 10
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
    elif bigMap:
        TILE_SIZE = 4
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

        # Display status texts
        text_surface = my_font.render("map: " + str(id), False, (255,255,255))
        text_surface2 = my_font.render("F2/F3 select map | +/- to zoom in/out", False, (255,255,255))
        screen.blit(text_surface, (0, 0))
        screen.blit(text_surface2, (150, 0))

        pygame.draw.circle(screen, (255, 0, 0), pygame.mouse.get_pos(), 6)
        cursor_color = TILE_COLORS.get(cursorState, (255, 255, 255))  # Default to white if cursorState is unknown
        pygame.draw.circle(screen, cursor_color, pygame.mouse.get_pos(), 4)

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
        num_columns = 10
        for idx in range(num_tiles):
            row = idx // num_columns
            col = idx % num_columns
            tile_rect = pygame.Rect(col * TILEMAP_WIDTH * TILE_SIZE, row * TILEMAP_HEIGHT * TILE_SIZE, TILEMAP_WIDTH * TILE_SIZE, TILEMAP_HEIGHT * TILE_SIZE)
            pygame.draw.rect(screen, (128, 128, 128), tile_rect, 2)  # Draw rectangle around the tilemap
            index_text = my_font.render(str(idx), True, (255, 255, 255))
            screen.blit(index_text, (col * TILEMAP_WIDTH * TILE_SIZE + 5, row * TILEMAP_HEIGHT * TILE_SIZE + 5))
        text_surface = my_font.render("map: " + str(id), False, (255,255,255))
        text_surface2 = my_font.render("F2/F3 select map | +/- to zoom in/out", False, (255,255,255))
        screen.blit(text_surface, (0, 0))
        screen.blit(text_surface2, (150, 0))
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
            newLevel = False
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

data, details = readFile(0)
statusString = f"loaded map: level{id}.h"
yTiles = int(details[1])
xTiles = int(details[2])
maxTiles = 3
screenyDim = 1280
screenxDim = 1900

screen = pygame.display.set_mode((screenxDim, screenyDim),pygame.RESIZABLE)
pygame.mouse.set_visible(False)

# Main loop
running = True
mouse1Held = False
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            print(event.scancode)
            if event.key == pygame.K_F6 or event.scancode == 45 or event.scancode == 86:
                print("Zoom out")
                writeToFile(id)
                try:
                    os.remove('./levels.h')
                    statusTimeout = 0
                    statusString = "removed old levels.h"
                    time.sleep(1) #give it a chance to clean up file                    
                except:
                    statusTimeout = 0
                    statusString = "unable to remove old levels.h?"
                statusTimeout = 0
                statusString = "packed all levels"
                concat_and_pack()
                bigMap = True
            if event.key == pygame.K_F7 or event.scancode == 46 or event.scancode == 87:
                print("Zoom in")
                bigMap = False
            if event.scancode == 41:
                writeToFile(id)
                statusString = "saved map: level" + str(id) + ".h, exiting editor"
                running = False
            if event.scancode == 62:
#                print("zip functionality disabled")
                try:
                    os.remove('./levels.h')
                    statusTimeout = 0
                    statusString = "removed old levels.h"
                    time.sleep(1) #give it a chance to clean up file                    
                except:
                    statusTimeout = 0
                    statusString = "unable to remove old levels.h?"
                statusTimeout = 0
                statusString = "packed all levels"
                concat_and_pack()
                #zip files back up
                #create_zip_with_headers("./levels.zip","./")
                #remove_all_h_files("./")
            if event.scancode == 61:
                statusTimeout = 0
                statusString = "saved map: level" + str(id) + ".h"
                writeToFile(id)
            if event.scancode == 60:
                #print("next map")
                writeToFile(id)
                #remove_all_h_files("./")
                id = id + 1
                data = readFile(id)
                data = data[0]
                statusTimeout = 0
                statusString = "saved map: " + str(id) + ", loaded map: level" + str(id) + ".h"
                writeToFile(id)

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
                statusString = "saved map: " + str(id) + ", loaded map: level" + str(id) + ".h"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse1Held = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse1Held = False

        if mouse1Held == True:
            mousePosition = pygame.mouse.get_pos()
            try:
                tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
#                print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                data[tileMapPosition_y][tileMapPosition_x] = cursorState
                statusString = "placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                statusTimeout = 0
            except:
                tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                statusString = "cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                statusTimeout = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                cursorState = cursorState + 1
                if cursorState > maxTiles:
                    cursorState = 0
            if event.button == 5:
                cursorState = cursorState - 1
                if cursorState < 0:
                    cursorState = maxTiles
            #print(event.button)
            if event.button == 1:
                mousePosition = pygame.mouse.get_pos()
                try:
                    tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                    tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    data[tileMapPosition_y][tileMapPosition_x] = cursorState
                    statusString = "placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                    statusTimeout = 0
                except:
                    tileMapPosition_x = int(mousePosition[0] / TILE_SIZE)
                    tileMapPosition_y = int(mousePosition[1] / TILE_SIZE)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*TILE_SIZE+TILE_SIZE,y*TILE_SIZE+TILE_SIZE))
                    statusString = "cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                    statusTimeout = 0
    
    render_map(bigMap,id)
    pygame.display.flip()  # Ensure the display updates

time.sleep(1)
pygame.quit()
