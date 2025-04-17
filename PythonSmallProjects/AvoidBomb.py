import pygame
import random
import time 

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
gray = (200, 200, 200)

# Igrac
player_width = 50
player_height = 10
player_x = width // 2
player_y = height - 40
player_speed = 7

# Bomba i zvezda
object_size = 40
num_bombs = 5
num_stars = 3


scale_factor = 1.2 # povecanje 30%
scaled_size = int(object_size*scale_factor)

scale_factor1 = 1.5 # povecanje 90%
scaled_size1 = int(object_size*scale_factor1)

bombs = []
stars = []

backgrounds = [
    pygame.image.load("background1.png"),
    pygame.image.load("background2.png"),
    pygame.image.load("background3.png"),
]


backgrounds = [
    pygame.transform.scale(pygame.image.load("background1.png"), (width, height)),
    pygame.transform.scale(pygame.image.load("background2.png"), (width, height)),
    pygame.transform.scale(pygame.image.load("background3.png"), (width, height)),

]


end_screen = pygame.image.load("gameOver.jpg")
end_screen = pygame.transform.scale(end_screen, (width, height))


for _ in range(num_bombs):
    bombs.append([random.randint(0, width - object_size), random.randint(-300, -20)])

for _ in range(num_stars):
    stars.append([random.randint(0, width - object_size), random.randint(-500, -20)])

bomb_speed = 5
star_speed = 4
score = 0
running = True

star_img = pygame.image.load("star3.png").convert_alpha()
star_img = pygame.transform.scale(star_img, (scaled_size, scaled_size))

bomb_img = pygame.image.load("bomb1.png").convert_alpha()
bomb_img = pygame.transform.scale(bomb_img, (scaled_size1, scaled_size1))

def draw_player(x):
    pygame.draw.rect(screen, black, (x, player_y, player_width, player_height))

def draw_bomb(x, y):
    #pygame.draw.circle(screen, red, (x + object_size // 2, y + object_size // 2), object_size // 2)
    screen.blit(bomb_img, (x, y))

def draw_star(x, y):
    #pygame.draw.circle(screen, yellow, (x + object_size // 2, y + object_size // 2), object_size // 2)
    #star_img = pygame.image.load("star.jpg")
    #star_img = pygame.transform.scale(star_img, (object_size, object_size))
    screen.blit(star_img, (x, y))

def show_text(text, x, y, color=black):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def show_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, gray, rect)
    label = font.render(text, True, black)
    screen.blit(label, (x + (w - label.get_width()) // 2, y + (h-label.get_height()) // 2))
    return rect

def show_centered_message_with_button(text, restart_game=False):
    while True:
        msg = font.render(text, True, red)
        #screen.blit(msg, (width // 2 - msg.get_width() // 2, height // 2 - 60))
        screen.blit(end_screen, (0,0))
        screen.blit(msg, (width // 2 - msg.get_width() // 2, height // 2 - 60))


        btn_text = "Igraj ponovo" if restart_game else "Nastavi"
        btn_rect = show_button(btn_text, width // 2 - 80, height // 2, 160, 50)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if btn_rect.collidepoint(mouse_pos):
                    return restart_game  # True ako restart, False ako nastavi


def run_level(level_num, num_bombs):
    player_x = width // 2
    score = 0
    start_time = time.time()
    level_duration = 30
    bg = backgrounds[level_num - 1]  # Pozadina za nivo

    bombs = [[random.randint(0, width - object_size), random.randint(-300, -20)] for _ in range(num_bombs)]
    stars = [[random.randint(0, width - object_size), random.randint(-500, -20)] for _ in range(3)]

    running = True
    while running:
        screen.blit(bg, (0, 0))  # Pozadina nivoa

        elapsed = time.time() - start_time
        remaining = int(level_duration - elapsed)
        progress = max(0, (level_duration - elapsed) / level_duration)
        draw_progress_bar(150, 10, 300, 20, progress)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed

        for i in range(len(bombs)):
            bombs[i][1] += bomb_speed
            draw_bomb(bombs[i][0], bombs[i][1])

            if bombs[i][1] > height:
                bombs[i][1] = random.randint(-300, -20)
                bombs[i][0] = random.randint(0, width - object_size)

            if (player_y < bombs[i][1] + object_size and
                player_y + player_height > bombs[i][1] and
                player_x < bombs[i][0] + object_size and
                player_x + player_width > bombs[i][0]):
                score -= 50
                bombs[i][1] = random.randint(-300, -20)
                bombs[i][0] = random.randint(0, width - object_size)

        for i in range(len(stars)):
            stars[i][1] += star_speed
            screen.blit(star_img, (stars[i][0], stars[i][1]))  # crtamo zvezdu

            if stars[i][1] > height:
                stars[i][1] = random.randint(-500, -20)
                stars[i][0] = random.randint(0, width - object_size)

            if (player_y < stars[i][1] + object_size and
                player_y + player_height > stars[i][1] and
                player_x < stars[i][0] + object_size and
                player_x + player_width > stars[i][0]):
                score += 5
                stars[i][1] = random.randint(-500, -20)
                stars[i][0] = random.randint(0, width - object_size)

        draw_player(player_x)
        show_text(f"Poeni: {score}", 10, 10)
        show_text(f"Vreme: {remaining}s", 10, 40)
        show_text(f"Nivo: {level_num}", width - 120, 10)

        if score < 0:
            restart = show_centered_message_with_button("Izgubio si!", restart_game=True)
            return not restart

        if remaining <= 0:
            if score > 0:
                show_centered_message_with_button(f"Bravo! Prešao si nivo {level_num}", restart_game=False)
                return True
            else:
                restart = show_centered_message_with_button("Nisi uspeo. Poeni nisu dovoljni.", restart_game=True)
                return not restart

        pygame.display.update()
        clock.tick(60)


def draw_progress_bar(x, y, w, h, progress):
    pygame.draw.rect(screen, black, (x, y, w, h), 2) # okvir
    inner_width = int(w*progress)
    pygame.draw.rect(screen, blue, (x+2, y+2, inner_width - 4, h - 4)) # punjenje

def main_game():
    while True:
        for level in range(1, 4):
            num_bombs = 5 + (level - 1) * 3
            passed = run_level(level, num_bombs)
            if not passed:
                break
        show_centered_message_with_button("Kraj igre! Hvala na igranju!",restart_game=True)

main_game()
pygame.quit()
