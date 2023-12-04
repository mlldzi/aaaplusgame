import math


def calculate_object_size(size, scaling_factor, distance_to_center):
    max_distance = math.sqrt((size ** 2) // 2)
    scaling_factor = max(0, min(1, scaling_factor))
    scaled_size = size * (1 - scaling_factor * (distance_to_center / max_distance) ** 2)
    return int(scaled_size)


def scale_objects(size, enemies, enemy_size):
    max_distance = math.sqrt((size ** 2) // 2)
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
