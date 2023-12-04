import pygame
import random
import math

from enemy import Enemy


class EnemyHandler:
    def __init__(self, size, enemy_size, enemy_speed, wave_size, enemy_spawn_delay, wave_delay):
        self.size = size
        self.enemy_size = enemy_size
        self.enemy_speed = enemy_speed
        self.wave_size = wave_size
        self.enemy_spawn_delay = enemy_spawn_delay
        self.wave_delay = wave_delay
        self.enemies = []
        self.wave_x = random.choice([0, self.size - self.enemy_size])  # x coordinate for the current wave
        self.wave_y = random.randint(0, self.size - self.enemy_size)
        self.enemies_spawned = 0
        self.last_enemy_spawn_time = pygame.time.get_ticks()
        self.current_wave = 0  # Current wave number
        self.last_wave_time = pygame.time.get_ticks()

    def spawn_new_enemy(self):
        enemy_x = self.wave_x
        enemy_y = self.wave_y
        distance_to_center = math.sqrt((self.size // 2 - enemy_x) ** 2 + (self.size // 2 - enemy_y) ** 2)
        scaling_factor = 0.005
        enemy_size = self.enemy_size * (1 - scaling_factor * (distance_to_center / (self.size // 2)) ** 2)
        self.enemies.append(Enemy(enemy_x, enemy_y, enemy_size, self.enemy_speed, self.size // 2, self.size // 2))
        self.enemies_spawned += 1

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def check_enemy_collisions(self, bullets):
        bullets_to_remove = []
        for bullet in bullets:
            for enemy in self.enemies:
                distance = math.sqrt((bullet.x - enemy.x) ** 2 + (bullet.y - enemy.y) ** 2)
                if distance < (bullet.radius + enemy.size) / 2:
                    bullets_to_remove.append(bullet)
                    self.enemies.remove(enemy)
                    break

        for bullet in bullets_to_remove:
            bullets.remove(bullet)

    def handle_enemy_spawning(self):
        current_time = pygame.time.get_ticks()
        if self.enemies_spawned < self.wave_size and current_time - self.last_enemy_spawn_time > self.enemy_spawn_delay:
            self.spawn_new_enemy()
            self.last_enemy_spawn_time = current_time

    def handle_wave_transition(self):
        current_time = pygame.time.get_ticks()
        if self.enemies_spawned >= self.wave_size and len(self.enemies) == 0:
            if current_time - self.last_wave_time > self.wave_delay:
                self.current_wave += 1
                self.enemies_spawned = 0
                self.last_wave_time = current_time
                self.wave_x = random.choice([0, self.size - self.enemy_size])
                self.wave_y = random.randint(0, self.size - self.enemy_size)
