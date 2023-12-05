import pygame
from stars import StarBackground
from player import Player
from functions import *
import sys
import os

module_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(module_dir)

from enemy.enemies_handler import EnemyHandler
from enemy.enemies_spawning import EnemySpawning


class Game:
    def __init__(self):
        pygame.init()
        self.size = 1000
        self.window = pygame.display.set_mode((self.size, self.size))
        pygame.display.set_caption("Gyruss-inspired Game")
        self.clock = pygame.time.Clock()

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.player_size = 50
        self.player_x = self.size // 2  # стартовые координаты, потом использую координаты из класса игрока
        self.player_y = self.size - 100
        self.player_speed = 3

        self.max_enemies = 10
        self.enemies = []
        self.enemy_size = 30

        self.bullets = []
        self.bullet_speed = 20
        self.bullet_cooldown = 100
        self.bullet_cooldown_time = 200

        self.killed_enemies = 0
        self.spawned_enemies = 0

        self.background = StarBackground(self.size)
        self.enemy_spawning = EnemySpawning(self.size, self.enemy_size, 3, 6, 200, 2000, self.enemies)
        self.enemy_handler = EnemyHandler(self.size, self.enemy_size, 3, 6, 200, 2000, self.enemies)
        self.player = Player(self.player_size, self.player_x, self.player_y, self.player_speed, self.bullet_speed,
                             self.bullet_cooldown_time, self.clock)

    def scale_objects(self):
        scale_objects(self.size, self.enemies, self.enemy_size)

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullets.extend(self.player.create_bullets())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def move_enemies(self):
        self.enemy_handler.move_enemies()
        self.scale_objects()

    def check_enemy_collisions(self):
        self.enemy_handler.check_enemy_collisions_bullet(self.bullets)
        self.enemy_handler.check_enemy_collision_player(self.player)

    def handle_enemy_spawning(self):
        self.enemy_spawning.handle_enemy_spawning()

    def handle_wave_transition(self):
        self.enemy_spawning.handle_wave_transition()

    def update_background(self):
        self.background.update(self.clock.get_time() / 1000)
        self.background.draw()
