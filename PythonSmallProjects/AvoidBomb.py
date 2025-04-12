import pygame
import random

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Izbegni bombe i sakupi zvezde!")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Boje
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Igrac
player_width = 70
player_height = 10
player_x = width // 2
player_y = height - 40
player_speed = 7

# Bomba i zvezda
object_size = 20
num_bombs = 5
num_stars = 3

bombs = []
stars = []

for _ in range(num_bombs):
    bombs.append([random.randint(0, width - object_size), random.randint(-300, -20)])

for _ in range(num_stars):
    stars.append([random.randint(0, width - object_size), random.randint(-500, -20)])

bomb_speed = 5
star_speed = 4
score = 0
running = True

def draw_player(x):
    pygame.draw.rect(screen, blue, (x, player_y, player_width, player_height))

def draw_bomb(x, y):
    pygame.draw.circle(screen, red, (x + object_size // 2, y + object_size // 2), object_size // 2)

def draw_star(x, y):
    pygame.draw.circle(screen, yellow, (x + object_size // 2, y + object_size // 2), object_size // 2)

def show_score(score):
    label = font.render(f"Poeni: {score}", True, black)
    screen.blit(label, (10, 10))

while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrole
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_width:
        player_x += player_speed

    # Pomeranje i crtanje bombi
    for i in range(len(bombs)):
        bombs[i][1] += bomb_speed
        draw_bomb(bombs[i][0], bombs[i][1])

        if bombs[i][1] > height:
            bombs[i][1] = random.randint(-300, -20)
            bombs[i][0] = random.randint(0, width - object_size)

        # Kolizija sa bombom
        if (player_y < bombs[i][1] + object_size and
            player_y + player_height > bombs[i][1] and
            player_x < bombs[i][0] + object_size and
            player_x + player_width > bombs[i][0]):
            screen.fill(white)
            game_over = font.render("KRAJ IGRE!", True, red)
            screen.blit(game_over, (width//2 - 80, height//2 - 20))
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

    # Pomeranje i crtanje zvezda
    for i in range(len(stars)):
        stars[i][1] += star_speed
        draw_star(stars[i][0], stars[i][1])

        if stars[i][1] > height:
            stars[i][1] = random.randint(-500, -20)
            stars[i][0] = random.randint(0, width - object_size)

        # Kolizija sa zvezdom
        if (player_y < stars[i][1] + object_size and
            player_y + player_height > stars[i][1] and
            player_x < stars[i][0] + object_size and
            player_x + player_width > stars[i][0]):
            score += 5
            stars[i][1] = random.randint(-500, -20)
            stars[i][0] = random.randint(0, width - object_size)

    draw_player(player_x)
    show_score(score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
