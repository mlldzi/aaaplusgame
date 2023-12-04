import pygame

from game import Game
from render import render_game


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

        render_game(game)

        game.player.move(game.size // 2, game.size // 2)
        pygame.display.update()
        game.clock.tick(60)

        running = game.handle_events()
        if not running:
            break

    pygame.quit()


if __name__ == "__main__":
    start()
