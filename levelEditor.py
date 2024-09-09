import pygame
import zipfile
import os
import glob
import time

#tile types
WATER = 0
SAND = 1
GRASS = 2
STONE = 3

maxTiles = 3 #should equal the index of the last tile


tileSize = 32
cursorState = 0
id = 1
statusString = "test"
statusTimeout = 0
statusLimit = 100

def concat_and_pack():
    filenames = glob.glob('./*h')
    #filenames = fileList
    with open('./levels.h', 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write('\n')

def remove_all_h_files(directory):
    # Use glob to find all .h files recursively
    pattern = os.path.join(directory, '**', '*.h')
    for file_path in glob.iglob(pattern, recursive=True):
        try:
            os.remove(file_path)
            print(f"Deleted {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

def extract_files(zip_filename, files_to_extract, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    with zipfile.ZipFile(zip_filename, 'r') as zipf:
        # Ensure files_to_extract is a list
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
        # Walk through the directory
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.h'):
                    file_path = os.path.join(root, file)
                    # Add file to zip, store with its relative path
                    arcname = os.path.relpath(file_path, directory)
                    zipf.write(file_path, arcname=arcname)
    print(f"Created ZIP archive: {zip_filename}")


def writeToFile(id):
    levelname = "./level" + str(id) + ".h"
    f = open(levelname, 'w')
    outputString = "int lvl" + str(id) + "[" + str(int(yTiles)) + "][" + str(int(xTiles)) + "] =\n{\n"
    
    for rowIndex, row in enumerate(data):
        outputString += "    { "
        for colIndex, element in enumerate(row):
            outputString += str(element)
            if colIndex < len(row) - 1:
                outputString += ","
        if rowIndex == len(data) - 1:
            outputString += "," + str(element)
        outputString += " }"
        if rowIndex < len(data) - 1:
            outputString += ",\n"
        else:
            outputString += "\n"
    
    outputString += "};"
    f.write(outputString)
    #print(outputString)
    #create_zip_with_headers("./levels.zip","./")
    f.close()
    

def readFile(id):
    
    newLevel = False
    levelname = str("level" + str(id) + ".h")
    print("zip functionality disabled")
    #print("extracting " + levelname)
    try:
        #extract_files("levels.zip",levelname,"./")
        #extract_files("levels.zip",'level0.h',"./") #always grab level 0, so it doesn't disappear from the zip
        f = open(levelname, 'r')
    except FileNotFoundError:
        #extract_files("levels.zip",'level0.h',"./")
        statusString = str(levelname) + " not found, blank template loaded"
        print(str(levelname) + " not found, blank template loaded")
        f = open("level0.h", 'r')
        newLevel = True
    y = 0

    arr = None
    details = []
    print("reading file " + str(levelname))
    for line in f:
        if newLevel == True:
            id = 0
            newLevel = False
        levelName = "lvl" + str(id)
        if levelName in line:
            details = line.split(' ')[1].replace(']', '').split('[')
            arr = [[0 for _ in range(int(details[2]) )] for _ in range(int(details[1]))]
        elif "{" in line and ',' in line:
            data = line.replace('{', '').replace('}', '').replace(', ','').replace(' ','').replace('\n','').strip()
            row = data.split(',')
            arr[y] = [int(i) for i in row[0:-1]]
            y += 1
        elif "};" in line:
            break
    
    f.close()
    #os.remove(levelname)
    return arr, details


data = readFile(0)
statusTimeout = 0
statusString = "loaded map: level" + str(id) + ".h"
yTiles = int(data[1][1])
xTiles = int(data[1][2])
#print(data)
yDim = (yTiles ) * tileSize
xDim = (xTiles ) * tileSize
#print(xDim)
screenyDim = (yTiles - 2) * tileSize
screenxDim = (xTiles - 2) * tileSize
data = data[0]
mouse1Held = False
screen = pygame.display.set_mode((screenxDim,screenyDim))
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 30)
running = True
pygame.mouse.set_visible(False)
#rows, cols = (20, 40)
#arr = [[0 for _ in range(cols)] for _ in range(rows)]  # initialize the array



#main UI loop
while running:
    statusTimeout = statusTimeout + 1
    if statusTimeout >= statusLimit:
        statusString = ""
        statusTimeout = 0
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            #print(event.scancode)
            if event.scancode == 41:
                writeToFile(id)
                statusString = "saved map: level" + str(id) + ".h, exiting editor"
                running = False
            if event.scancode == 63:
                statusTimeout = 0
                statusString = "zoom out"
                bigMap = True
            if event.scancode == 64:
                statusTimeout = 0
                statusString = "zoom in"
                
            if event.scancode == 62:
#                print("zip functionality disabled")
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
                
        text_surface = my_font.render("map: " + str(id), False, (0, 0, 0))
        text_surface2 = my_font.render("F2/F3 select map | F4 save current map | F5 pack all maps into levels.h", False, (0, 0, 0))
        statusText = my_font.render(statusString, False, (0, 0, 0))
       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse1Held = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse1Held = False

        if mouse1Held == True:
            mousePosition = pygame.mouse.get_pos()
            try:
                tileMapPosition_x = int(mousePosition[0] / tileSize)
                tileMapPosition_y = int(mousePosition[1] / tileSize)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*tileSize+tileSize,y*tileSize+tileSize))
#                print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                data[tileMapPosition_y][tileMapPosition_x] = cursorState
                statusString = "placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                statusTimeout = 0
            except:
                tileMapPosition_x = int(mousePosition[0] / tileSize)
                tileMapPosition_y = int(mousePosition[1] / tileSize)
            #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*tileSize+tileSize,y*tileSize+tileSize))
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
                    tileMapPosition_x = int(mousePosition[0] / tileSize)
                    tileMapPosition_y = int(mousePosition[1] / tileSize)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*tileSize+tileSize,y*tileSize+tileSize))
                    print(str(tileMapPosition_x) + ', ' + str(tileMapPosition_y))
                    data[tileMapPosition_y][tileMapPosition_x] = cursorState
                    statusString = "placed tile type (" + str(cursorState) + ") at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                    statusTimeout = 0
                except:
                    tileMapPosition_x = int(mousePosition[0] / tileSize)
                    tileMapPosition_y = int(mousePosition[1] / tileSize)
                #pygame.draw.rect(screen,"red",(tileMapPosition_x,tileMapPosition_y,x*tileSize+tileSize,y*tileSize+tileSize))
                    statusString = "cannot place tile at : " + str(tileMapPosition_x) + ', ' + str(tileMapPosition_y)
                    statusTimeout = 0
    y = 0
    
    for row in data:
        x = 0
        for item in row:
            tilePos = (x*tileSize,y*tileSize)
            if item == WATER:
                pygame.draw.rect(screen,"cornflowerblue",(x*tileSize,y*tileSize,x*tileSize+tileSize,y*tileSize+tileSize))
            elif item == GRASS:
                pygame.draw.rect(screen,"chartreuse4",(x*tileSize,y*tileSize,x*tileSize+tileSize,y*tileSize+tileSize))
            elif item == SAND:
                pygame.draw.rect(screen,"burlywood3",(x*tileSize,y*tileSize,x*tileSize+tileSize,y*tileSize+tileSize))
            elif item == STONE:
                pygame.draw.rect(screen,"darkgrey",(x*tileSize,y*tileSize,x*tileSize+tileSize,y*tileSize+tileSize))
            else:
                pygame.draw.rect(screen,"white",(x*tileSize,y*tileSize,x*tileSize+tileSize,y*tileSize+tileSize))
            x = x + 1
        y = y + 1
        screen.blit(text_surface, (0,0))
        screen.blit(text_surface2, (150,0))
        screen.blit(statusText, (150,screenyDim-50))
        pygame.draw.circle(screen, "red", pygame.mouse.get_pos(), 6)
        if cursorState == WATER:
            pygame.draw.circle(screen, "cornflowerblue", pygame.mouse.get_pos(), 4)
        if cursorState == GRASS:
            pygame.draw.circle(screen, "chartreuse4", pygame.mouse.get_pos(), 4)
        if cursorState == SAND:
            pygame.draw.circle(screen, "burlywood3", pygame.mouse.get_pos(), 4)
        if cursorState == STONE:
            pygame.draw.circle(screen, "darkgrey", pygame.mouse.get_pos(), 4)
       # if cursorState == 3:
       #     pygame.draw.circle(screen, "red", pygame.mouse.get_pos(), 6)
       #     pygame.draw.circle(screen, "white", pygame.mouse.get_pos(), 4)
    pygame.display.flip()
time.sleep(1)
pygame.quit()

