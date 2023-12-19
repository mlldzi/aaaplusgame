import pygame
import random
# import sys
# import os
#
# from enemy.enemy import Enemy
from enemy.enemy_types import EnemyType1, EnemyType2
from functions import *


class EnemySpawning:
    def __init__(self, game_size, enemy_size, enemy_speed, wave_size, enemy_spawn_delay, wave_delay, enemies):
        self.game_size = game_size
        self.enemy_size = enemy_size
        self.enemy_speed = enemy_speed
        self.enemies = enemies

        self.wave_size = wave_size
        self.enemy_spawn_delay = enemy_spawn_delay
        self.wave_delay = wave_delay

        self.enemies_spawned = 0
        self.last_enemy_spawn_time = pygame.time.get_ticks()
        self.current_wave = 0
        self.last_wave_time = pygame.time.get_ticks()

        self.center = self.game_size // 2

    def spawn_new_enemy(self):
        if self.current_wave == 1:
            current_type = EnemyType1
            wave_x, wave_y, size, speed = get_enemy_coordinates(current_type)

            enemy = current_type(wave_x, wave_y, size, speed, self.center, self.center)
            self.enemies.append(enemy)
        elif self.current_wave == 2:
            current_type = EnemyType2
            wave_x, wave_y, size, speed = get_enemy_coordinates(current_type)

            enemy = current_type(wave_x, wave_y, size, speed, self.center, self.center)
            self.enemies.append(enemy)
        else:
            pass

        self.enemies_spawned += 1

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
