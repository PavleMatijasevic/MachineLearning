import pygame
import math
import sys

pygame.init()

# Dimenzije prozora
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Track Simulation")

WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Sat za FPS
clock = pygame.time.Clock()
FPS = 60

# Staza - centar i poluprecnici
TRACK_CENTER = (WIDTH // 2, HEIGHT // 2)
OUTER_RADIUS = 200
INNER_RADIUS = 100

# Auto
car_pos = [WIDTH // 2, HEIGHT // 2 - 150]
car_angle = 0  # U stepenima
car_speed = 2
car_length = 20
car_width = 10

def draw_track():
    # Spoljasnji krug
    pygame.draw.circle(screen, GRAY, TRACK_CENTER, OUTER_RADIUS)
    # Unutrasnji krug (briše deo staze)
    pygame.draw.circle(screen, WHITE, TRACK_CENTER, INNER_RADIUS)

def draw_car(x, y, angle):
    # Proracun pravougaonika
    radians = math.radians(angle)
    dx = math.cos(radians) * car_length
    dy = math.sin(radians) * car_length

    car_rect = pygame.Rect(0, 0, car_length, car_width)
    car_rect.center = (x, y)

    rotated_car = pygame.transform.rotate(pygame.Surface((car_length, car_width)), -angle)
    rotated_car.fill(RED)
    screen.blit(rotated_car, rotated_car.get_rect(center=car_rect.center))

def move_car(keys, x, y, angle):
    if keys[pygame.K_LEFT]:
        angle -= 3
    if keys[pygame.K_RIGHT]:
        angle += 3
    if keys[pygame.K_UP]:
        x += math.cos(math.radians(angle)) * car_speed
        y += math.sin(math.radians(angle)) * car_speed
    return x, y, angle

def is_on_track(x, y):
    dx = x - TRACK_CENTER[0]
    dy = y - TRACK_CENTER[1]
    dist = math.sqrt(dx**2 + dy**2)
    return INNER_RADIUS < dist < OUTER_RADIUS

# Glavna petlja
running = True
while running:
    screen.fill(WHITE)
    draw_track()

    # Prikupimo trenutno stanje tastera
    keys = pygame.key.get_pressed()

    # Izracunamo novu poziciju i ugao automobila
    new_x, new_y, new_angle = move_car(keys, car_pos[0], car_pos[1], car_angle)

    # Proverimo da li je automobil na stazi
    if is_on_track(new_x, new_y):
        car_pos[0], car_pos[1], car_angle = new_x, new_y, new_angle
        draw_car(car_pos[0], car_pos[1], car_angle)
    else:
        # Ako auto izadje sa staze, prikažemo poruku i zaustavimo simulaciju
        draw_car(car_pos[0], car_pos[1], car_angle)
        font = pygame.font.SysFont(None, 48)
        text = font.render('Izlazak sa staze!', True, (255, 0, 0))
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    pygame.display.flip()
    clock.tick(FPS)

    # Provera za zatvaranje prozora
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
