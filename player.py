import math
import pygame
from bullet import Bullet
import time


class Player:
    def __init__(self, size, x, y, speed, bullet_speed, bullet_cooldown_time, clock):
        self.size = size
        self.x = x
        self.y = y
        self.speed = speed
        self.bullet_speed = bullet_speed
        self.bullet_cooldown_time = bullet_cooldown_time
        self.bullets = []
        self.last_shot_time = 0
        self.clock = clock

    def move(self, center_x, center_y):
        keys = pygame.key.get_pressed()
        dx = center_x - self.x
        dy = center_y - self.y
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        radius = math.sqrt((self.x - center_x) ** 2 + (self.y - center_y) ** 2)

        if distance_to_center > 1:
            if keys[pygame.K_a]:
                angle = math.atan2(self.y - center_y, self.x - center_x)
                angle += math.radians(self.speed)
                self.x = center_x + radius * math.cos(angle)
                self.y = center_y + radius * math.sin(angle)

            if keys[pygame.K_d]:
                angle = math.atan2(self.y - center_y, self.x - center_x)
                angle -= math.radians(self.speed)
                self.x = center_x + radius * math.cos(angle)
                self.y = center_y + radius * math.sin(angle)

    def create_bullets(self):
        current_time = time.time()
        if current_time - self.last_shot_time >= 0.15:
            bullet1 = Bullet(self.x - 10, self.y, self.bullet_speed, 3)
            bullet2 = Bullet(self.x + 10, self.y, self.bullet_speed, 3)
            self.last_shot_time = current_time
            return [bullet1, bullet2]
        else:
            return []
