import pygame
import os
import math


def render_game(game):
    ship_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "ship.png"))
    ship_image = pygame.transform.scale(ship_image, (50, 50))

    ship_x = int(game.player.x)
    ship_y = int(game.player.y)

    angle = math.atan2(ship_x - game.size // 2, ship_y - game.size // 2)
    rotated_ship_image = pygame.transform.rotate(ship_image, math.degrees(angle))

    ship_rect = rotated_ship_image.get_rect(center=(ship_x, ship_y))
    game.window.blit(rotated_ship_image, ship_rect)

    for bullet in game.bullets:
        bullet.move(game.size // 2, game.size // 2)
        if abs(bullet.y - game.size // 2) < 1 and abs(bullet.x - game.size // 2) < 1:
            game.bullets.remove(bullet)
        else:
            pygame.draw.circle(game.window, game.WHITE, (int(bullet.x), int(bullet.y)), bullet.radius)

    for enemy in game.enemies:
        pygame.draw.circle(game.window, game.WHITE, (int(enemy.x), int(enemy.y)), int(enemy.size))
