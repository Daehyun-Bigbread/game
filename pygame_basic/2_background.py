import pygame

pygame.init() # Initialization (Must need)

# Set screen size
screen_width = 480 # width size
screen_height = 640 # height size
screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title
pygame.display.set_caption("Nado Game") #GameTitle

# Background Image upload
background = pygame.image.load("C:/Users/bigda/Desktop/Pythonworkspace/pygame_basic/background.png")

# event loop
running = True #Game is running?
while running:
    for event in pygame.event.get(): # What event is playing?
        if event.type == pygame.QUIT: # The event is playing when the window is closing?
            running = False # Game is not running

    #screen.fill((0, 0, 255)) - # filling background (색갈 칠하기)
    screen.blit(background, (0, 0)) # drawing background

    pygame.display.update() # redrawing background!

# pygame finish
pygame.quit()