import pygame
import os
import sys
from render import render_game

def handle_main_events(game):
    button_restart_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "restart_button.png")),(177,100))
    button_restart_rect = pygame.Rect(game.size // 2-100, game.size // 2 + 200, 177, 100)
    button_start_img = pygame.transform.scale(pygame.image.load(os.path.join("assets", "images", "start_BUTTON.png")),(217,100))
    button_start_rect = pygame.Rect(game.size // 2-100, game.size // 2 + 200, 217, 100)
    running = False

    while not running:
        game.window.fill(game.BLACK)
        game.window.blit(button_start_img, button_start_rect)
        running = game.check_click(button_start_rect)
        pygame.display.update()

    while running:
        game.window.fill(game.BLACK)

        game.update_background()
        game.move_enemies()
        game.check_enemy_collisions()
        game.handle_enemy_spawning()
        game.handle_wave_transition()

        render_game(game)
        game.player.move(game.size // 2, game.size // 2)
        pygame.display.update()
        game.clock.tick(60)

        running = game.handle_events()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit() # можно убрать если надо протестить окно рестарта

    while not running:
        game.window.fill(game.BLACK)
        game.window.blit(button_restart_img, button_restart_rect)
        running = game.check_click(button_restart_rect)
        pygame.display.update()