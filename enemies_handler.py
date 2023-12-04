import math

class EnemyHandler:
    def __init__(self, size, enemy_size, enemy_speed, wave_size, enemy_spawn_delay, wave_delay, enemies):
        self.size = size
        self.enemy_size = enemy_size
        self.enemy_speed = enemy_speed
        self.wave_size = wave_size
        self.enemy_spawn_delay = enemy_spawn_delay
        self.wave_delay = wave_delay
        self.enemies = enemies

    def move_enemies(self):
        for enemy in self.enemies:
            enemy.move()

    def check_enemy_collisions_bullet(self, bullets):
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