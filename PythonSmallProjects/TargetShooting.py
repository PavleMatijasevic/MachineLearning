import pygame
import random
import time

pygame.init()

# Postavke ekrana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pucanje mete")

# Boje
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Font i sat
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

# Meta
target_radius = 30

def draw_target(x, y):
    pygame.draw.circle(screen, red, (x, y), target_radius)

def show_text(text, x, y):
    label = font.render(text, True, black)
    screen.blit(label, (x, y))

def game_loop():
    running = True
    score = 0
    start_time = time.time()
    game_duration = 30  

    # Pocetna meta
    target_x = random.randint(target_radius, width - target_radius)
    target_y = random.randint(target_radius, height - target_radius)

    while running:
        screen.fill(white)

        current_time = time.time()
        elapsed_time = current_time - start_time

        # Provera kraja igre
        if elapsed_time > game_duration:
            screen.fill(white)
            show_text(f"Kraj igre! Poeni: {score}", width // 2 - 100, height // 2)
            pygame.display.update()
            pygame.time.wait(3000)
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5
                if distance < target_radius:
                    score += 1
                    target_x = random.randint(target_radius, width - target_radius)
                    target_y = random.randint(target_radius, height - target_radius)

        draw_target(target_x, target_y)
        show_text(f"Poeni: {score}", 10, 10)
        show_text(f"Vreme: {int(game_duration - elapsed_time)}s", 10, 50)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

game_loop()
