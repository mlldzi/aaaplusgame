import pygame

from game import Game


def start():
    game = Game()

    running = True
    while running:
        game.window.fill(game.BLACK)

        game.move_enemies()
        game.check_enemy_collisions()
        game.handle_enemy_spawning()
        game.handle_wave_transition()
        game.update_background()

        pygame.draw.circle(game.window, game.WHITE, (int(game.player.x), int(game.player.y)), game.player.size)

        for bullet in game.bullets:
            bullet.move(game.size // 2, game.size // 2)
            if bullet.y < 0:
                game.bullets.remove(bullet)
            else:
                pygame.draw.circle(game.window, game.WHITE, (int(bullet.x), int(bullet.y)), bullet.radius)

        for enemy in game.enemy_handler.enemies:
            pygame.draw.circle(game.window, game.WHITE, (int(enemy.x), int(enemy.y)), int(enemy.size))

        game.player.move(game.size // 2, game.size // 2)
        pygame.display.update()
        game.clock.tick(60)

        running = game.handle_events()
        if not running:
            break

    pygame.quit()


if __name__ == "__main__":
    start()
