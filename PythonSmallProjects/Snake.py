import pygame
import time
import random

pygame.init()

# Postavke prozora
width = 800
height = 600
snake_block = 20
speed = 13

# Boje
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Font
font_style = pygame.font.SysFont(None, 50)

# Funkcija za prikaz poruka na ekranu
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [width / 6, height / 3])

# Funkcija za crtanje zmije
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], snake_block, snake_block])

# Glavna funkcija igre
def gameLoop():
    game_over = False
    game_close = False

    # Pocetna pozicija zmije
    x1 = width / 2
    y1 = height / 2

    # Pocetna duzina zmije
    snake_list = []
    length_of_snake = 1

    # Smer kretanja zmije
    x1_change = 0
    y1_change = 0

    # Polozaj hrane
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            gameDisplay.fill(blue)
           
            message("Pritisnite C-ponovo igrati ili Q-izlaz", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Provera granica prozora
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay, green, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Provera sudara s hranom
        if pygame.Rect(x1, y1, snake_block, snake_block).colliderect(pygame.Rect(foodx, foody, snake_block, snake_block)):
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1


        # Provera sudara s telom zmije
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        # Brzina igre
        clock.tick(speed)

    pygame.quit()
    quit()

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake igra')
clock = pygame.time.Clock()

gameLoop()
