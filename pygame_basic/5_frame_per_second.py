import pygame

pygame.init() # Initialization(초기화) (Must need(반드시 필요))

# Set screen size (화면 크기 설정)
screen_width = 480 # width size (가로 크기)
screen_height = 640 # height size (세로 크기)
screen = pygame.display.set_mode((screen_width, screen_height))

# Set Screen Title (화면 타이틀 설정)
pygame.display.set_caption("Nado Game") # Game Title (게임 이름)

# FPS
clock = pygame.time.Clock()

# Background Image upload (배경 이미지 불러오기)
background = pygame.image.load("C:/Users/bigda/Desktop/Pythonworkspace/pygame_basic/background.png")

# character(sprite) calling up (캐릭터(스프라이트) 불러오기)
character =  pygame.image.load("C:/Users/bigda/Desktop/Pythonworkspace/pygame_basic/character.png")
character_size = character.get_rect().size # Obtaining the size of the image (이미지의 크기를 구해옴)
character_width = character_size[0] # character_width (캐릭터 가로 크기)
character_height = character_size[1] # character_height (캐릭터 세로 크기)
character_x_pos = (screen_width / 2) - (character_width / 2) # Located half the width of the screen (width)
character_y_pos = screen_height - character_height # Located at the bottom of the screen's vertical size (height)

# Moving Location (이동할 좌표)
to_x = 0
to_y = 0

# 이동 속도 (Moving Speed)
character_speed = 0.6

# event loop (이벤트 루프)
running = True # Game is running? (게임이 진행중인가?)
while running:
    dt = clock.tick(30) # The number of frames per second of the game screen settings (게임화면의 초당 프레임 수는 설정)

    print("fps : " + str(clock.get_fps()))

 # 캐릭터가 100 만큼 이동을 해야함
 # 10 fps : 1초 동안에 10번 동작 -> 1번에 몇만큼 이동? 10만큼! 10 * 10 = 100 
 # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼! 5 * 20 = 100

    for event in pygame.event.get(): # What event is playing? (어떤 이벤트가 발생하였는가?)
        if event.type == pygame.QUIT: # The event is playing when the window is closing? (창이 닫히는 이벤트가 발생하였는가?)
            running = False # Game is not running (게임이 진행중이 아님)

        if event.type == pygame.KEYDOWN: # check the key is pressed (키가 눌렸는지 확인)
            if event.key == pygame.K_LEFT: # character left (캐릭터를 왼쪽으로)
                    to_x -= character_speed # to_x = to_x - character_speed
            elif event.key == pygame.K_RIGHT: # character right (캐릭터를 오른쪽으로)
                    to_x += character_speed # to_x = to_x + character_speed 
            elif event.key == pygame.K_UP: # character going up (캐릭터를 위로)
                    to_y -= character_speed # to_y = to_y - character_speed
            elif event.key == pygame.K_DOWN: # character going down (캐릭터를 아래로)
                    to_y += character_speed # to_y = to_y + character_speed

        if event.type == pygame.KEYUP: # STOP when direction key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # lateral boundary value processing (가로 경계값 처리)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # longitudinal boundary value processing (세로 경계값 처리)
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #screen.fill((0, 0, 255)) - # filling background (색갈 칠하기)
    screen.blit(background, (0, 0)) # drawing background (배경 그리기)

    screen.blit(character, (character_x_pos, character_y_pos)) # drawing character (캐릭터 그리기)

    pygame.display.update() # redrawing background! (게임화면을 다시 그리기!)

# pygame finish (pygame 종료)
pygame.quit()