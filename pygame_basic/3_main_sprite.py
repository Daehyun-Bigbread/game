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

# character(sprite) calling up
character =  pygame.image.load("C:/Users/bigda/Desktop/Pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size # Obtaining the size of the image
character_width = character_size[0] # character_width
character_height = character_size[1] # character_height
character_x_pos = (screen_width / 2) - (character_width / 2) # Located half the width of the screen (width)
character_y_pos = screen_height - character_height # Located at the bottom of the screen's vertical size (height)

# event loop
running = True #Game is running?
while running:
    for event in pygame.event.get(): # What event is playing?
        if event.type == pygame.QUIT: # The event is playing when the window is closing?
            running = False # Game is not running

    #screen.fill((0, 0, 255)) - # filling background (색갈 칠하기)
    screen.blit(background, (0, 0)) # drawing background

    screen.blit(character, (character_x_pos, character_y_pos)) # drawing character

    pygame.display.update() # redrawing background!

# pygame finish
pygame.quit()