import pygame
import math

from bullet import Bullet
from stars import StarBackground
from enemies_spawning import EnemyHandler
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.size = 1000
        self.window = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Gyruss-inspired Game")
        self.clock = pygame.time.Clock()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.player_size = 40
        self.player_x = self.size // 2 # стартовые координаты, потом использую координаты из класса игрока
        self.player_y = self.size - 100
        self.player_speed = 3

        self.max_enemies = 10

        self.bullets = []
        self.bullet_speed = 20
        self.bullet_cooldown = 100
        self.bullet_cooldown_time = 200

        self.killed_enemies = 0
        self.spawned_enemies = 0

        self.scaling_factor = 0.02

        self.background = StarBackground(self.size)
        self.enemy_handler = EnemyHandler(self.size, 30, 3, 6, 200, 2000)
        self.player = Player(self.player_size, self.player_x, self.player_y, self.player_speed, self.bullet_speed, self.bullet_cooldown_time, self.clock)

    def calculate_distance_to_center(self):
        dx = abs(self.size // 2 - self.player.x)
        dy = abs(self.size // 2 - self.player.y)
        distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
        return distance_to_center

    def scale_objects(self):
        max_distance = 700
        for enemy in self.enemy_handler.enemies:
            dx = abs(self.size // 2 - enemy.x)
            dy = abs(self.size // 2 - enemy.y)
            distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
            percentage = 10 - (distance_to_center / max_distance) * 100
            scaling_factor = self.scaling_factor * percentage
            enemy.size = 30 * (1 - scaling_factor)

    def move_enemies(self):
        self.enemy_handler.move_enemies()
        self.scale_objects()

    def check_enemy_collisions(self):
        self.enemy_handler.check_enemy_collisions(self.bullets)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullets.extend(self.player.create_bullets())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def handle_enemy_spawning(self):
        self.enemy_handler.handle_enemy_spawning()

    def handle_wave_transition(self):
        self.enemy_handler.handle_wave_transition()

    def update_background(self):
        self.background.update(self.clock.get_time() / 1000)
        self.background.draw()