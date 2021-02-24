import pygame

pygame.init() # Initialization (Must need)

# Set screens size
screen_width = 480 # width size
screen_height = 640 # height size
pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Nado Game") #GameTitle

# event loop
running = True #Game is running?
while running:
    for event in pygame.event.get(): # What event is playing?
        if event.type == pygame.QUIT: # The event is playing when the window is closing?
            running = False # Game is not running

# pygame finish
pygame.quit()