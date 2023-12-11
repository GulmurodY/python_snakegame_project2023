import time
import pygame
import sys
from pygame.math import Vector2
from game import MAIN
from globals import username, color, cell_size, cell_number

screen = pygame.display.set_mode((cell_number * cell_size,
                                  cell_number * cell_size))
clock = pygame.time.Clock()
# pygame.mixer.pre_init(44100, -16, 2, 512)
# pygame.mixer.music.load("Sound/theme_song.mp3")
# pygame.mixer.music.play(-1)
main_game = MAIN(color, username, screen)

prev_keytime = time.time() - 1
prev_key = pygame.K_c


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            if event.key == pygame.K_ESCAPE:
                main_game.pause()
            current_keytime = time.time()
            if current_keytime - prev_keytime < 0.1:
                continue
            else:
                prev_keytime = current_keytime
                prev_key = event.key
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
    main_game.update()
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(main_game.snake.speed)
