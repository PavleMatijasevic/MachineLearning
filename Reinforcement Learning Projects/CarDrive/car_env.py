import gymnasium as gym
from gymnasium import spaces
import numpy as np
import pygame
import math
import random

WIDTH, HEIGHT = 800, 600

NUM_SENSORS = 5
MAX_SENSOR_DISTANCE = 150
SENSOR_ANGLES = [-60, -30, 0, 30, 60]  # Uglovi u odnosu na pravac kretanja


class CarEnv(gym.Env):
    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode
        self.screen = None
        self.clock = None

        # Parametri za randomizaciju staze
        self.min_inner_radius = 80
        self.max_inner_radius = 120
        self.min_outer_radius = 180
        self.max_outer_radius = 240

        # Akcije: 0 = levo, 1 = pravo, 2 = desno
        self.action_space = spaces.Discrete(3)

        # Opservacija: 5 senzora + ugao
        low = np.array([0.0] * NUM_SENSORS + [0.0], dtype=np.float32)
        high = np.array([1.0] * NUM_SENSORS + [1.0], dtype=np.float32)
        self.observation_space = spaces.Box(low, high, dtype=np.float32)

        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        # Randomizuj stazu
        self.inner_radius = random.randint(self.min_inner_radius, self.max_inner_radius)
        self.outer_radius = random.randint(self.min_outer_radius, self.max_outer_radius)

        # Randomizuj centar staze
        margin = self.max_outer_radius + 20
        self.track_center = (
            random.randint(margin, WIDTH - margin),
            random.randint(margin, HEIGHT - margin)
        )

        # Početna pozicija auta: iznad centra, između krugova
        start_r = (self.inner_radius + self.outer_radius) // 2
        self.car_x = self.track_center[0]
        self.car_y = self.track_center[1] - start_r
        self.car_angle = 0
        self.car_speed = 2

        if self.render_mode == "human":
            self._init_pygame()

        return self._get_obs(), {}

    def _get_obs(self):
        sensors = [self._cast_sensor(angle) / MAX_SENSOR_DISTANCE for angle in SENSOR_ANGLES]
        return np.array(sensors + [self.car_angle / 360.0], dtype=np.float32)

    def _is_on_track(self):
        dx = self.car_x - self.track_center[0]
        dy = self.car_y - self.track_center[1]
        dist = math.sqrt(dx**2 + dy**2)
        return self.inner_radius < dist < self.outer_radius

    def step(self, action):
        if action == 0:
            self.car_angle -= 5
        elif action == 2:
            self.car_angle += 5

        self.car_angle %= 360

        radians = math.radians(self.car_angle)
        self.car_x += math.cos(radians) * self.car_speed
        self.car_y += math.sin(radians) * self.car_speed

        dx = self.car_x - self.track_center[0]
        dy = self.car_y - self.track_center[1]
        dist = math.sqrt(dx**2 + dy**2)
        ideal_radius = (self.inner_radius + self.outer_radius) / 2
        dist_from_center = abs(dist - ideal_radius)

        terminated = not self._is_on_track()
        reward = 1.0

        if terminated:
            reward = -100.0
        else:
            reward += max(0, 0.5 - dist_from_center / 50)
            if action != 1:
                reward -= 0.1

        truncated = False

        if self.render_mode == "human":
            self.render()

        return self._get_obs(), reward, terminated, truncated, {}

    def _cast_sensor(self, angle_offset_deg):
        angle = math.radians(self.car_angle + angle_offset_deg)
        x, y = self.car_x, self.car_y

        for dist in range(0, MAX_SENSOR_DISTANCE, 2):
            test_x = int(x + math.cos(angle) * dist)
            test_y = int(y + math.sin(angle) * dist)

            if test_x < 0 or test_x >= WIDTH or test_y < 0 or test_y >= HEIGHT:
                return dist

            dx = test_x - self.track_center[0]
            dy = test_y - self.track_center[1]
            d = math.sqrt(dx**2 + dy**2)

            if not (self.inner_radius < d < self.outer_radius):
                return dist

        return MAX_SENSOR_DISTANCE

    def render(self):
        if self.screen is None:
            self._init_pygame()

        self.screen.fill((255, 255, 255))
        pygame.draw.circle(self.screen, (50, 50, 50), self.track_center, self.outer_radius)
        pygame.draw.circle(self.screen, (255, 255, 255), self.track_center, self.inner_radius)

        car_rect = pygame.Rect(0, 0, 20, 10)
        car_rect.center = (self.car_x, self.car_y)
        rotated = pygame.transform.rotate(pygame.Surface((20, 10)), -self.car_angle)
        rotated.fill((255, 0, 0))
        self.screen.blit(rotated, rotated.get_rect(center=car_rect.center))

        for angle in SENSOR_ANGLES:
            dist = self._cast_sensor(angle)
            rad = math.radians(self.car_angle + angle)
            end_x = int(self.car_x + math.cos(rad) * dist)
            end_y = int(self.car_y + math.sin(rad) * dist)
            pygame.draw.line(self.screen, (0, 255, 0), (self.car_x, self.car_y), (end_x, end_y), 1)

        pygame.display.flip()
        self.clock.tick(60)

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def close(self):
        if self.screen:
            pygame.quit()
            self.screen = None
