import pygame
import tkinter as tk
from tkinter import simpledialog

# Initialize Pygame
pygame.init()

# Set up the display
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Pygame App with Integer Input')

# Initialize variables
mapSearch = 0

def prompt_for_integer():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    user_input = simpledialog.askinteger("Input", "Enter an integer value:")
    if user_input is not None:
        return user_input
    return 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                mapSearch = prompt_for_integer()
                print(f"mapSearch updated to: {mapSearch}")

    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
