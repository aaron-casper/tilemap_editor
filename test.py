import tkinter as tk
from tkinter import simpledialog
import pygame
import sys

def get_configurations():
    # Initialize Tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Define a function to prompt for configuration details
    def prompt_for_details():
        details = {}
        details['buildings'] = simpledialog.askstring("Configuration", "Include buildings? (yes/no)").strip().lower() == 'yes'
        details['building_count'] = int(simpledialog.askstring("Configuration", "Building count (integer):").strip())
        details['rivers'] = simpledialog.askstring("Configuration", "Include rivers? (yes/no)").strip().lower() == 'yes'
        details['river_width'] = float(simpledialog.askstring("Configuration", "River width (integer):").strip())
        details['terrain_scale'] = float(simpledialog.askstring("Configuration", "Terrain scale (float):").strip())
        details['octaves'] = int(simpledialog.askstring("Configuration", "Octaves (integer):").strip())
        details['persistence'] = float(simpledialog.askstring("Configuration", "Persistence (float):").strip())
        return details

    # Get configuration details from user
    config = prompt_for_details()
    print(config)
    # Close Tkinter root window
    root.destroy()
    
    return config

def run_pygame_app(config):
    pygame.init()

    # Set up display
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Application")

    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with white
        screen.fill(WHITE)

        # Display configuration details
        font = pygame.font.Font(None, 36)
        y_offset = 10
        for key, value in config.items():
            text_surface = font.render(f"{key}: {value}", True, BLACK)
            screen.blit(text_surface, (10, y_offset))
            y_offset += 40

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def main():
    config = get_configurations()
    run_pygame_app(config)

if __name__ == "__main__":
    main()
