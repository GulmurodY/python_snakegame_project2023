import pygame
from globals import cell_size, cell_number
from pygame.math import Vector2


class Grass:
    def __init__(self, screen):
        self.screen = screen
        self.borders_lvl2 = [Vector2(2, i) for i in range(2, 14)] + \
                            [Vector2(i, 13) for i in range(3, 14)] + \
                            [Vector2(13, i) for i in range(3, 9)] + \
                            [Vector2(i, 2) for i in range(3, 14)]

        self.borders_lvl3 = [Vector2(2, i) for i in range(2, 14)] + \
                            [Vector2(i, 13) for i in range(3, 14)] + \
                            [Vector2(13, i) for i in range(3, 9)] + \
                            [Vector2(i, 8) for i in range(7, 13)] + \
                            [Vector2(i, 2) for i in range(3, 14)] + \
                            [Vector2(7, i) for i in range(5, 8)]

        self.borders_lvl4 = [Vector2(3, i) for i in range(10)] + \
                            [Vector2(8, i) for i in range(8)] + \
                            [Vector2(13, i) for i in range(4)] + \
                            [Vector2(i, 6) for i in range(11, 16)] +\
                            [Vector2(i, 10) for i in range(8, 16)] + \
                            [Vector2(i, 13) for i in range(5, 16)]

        self.borders_lvl5 = [Vector2(0, i) for i in range(4, 12)] + \
                            [Vector2(1, i) for i in range(4, 12)] + \
                            [Vector2(15, i) for i in range(4, 12)] + \
                            [Vector2(14, i) for i in range(4, 12)] + \
                            [Vector2(i, 0) for i in range(4, 12)] + \
                            [Vector2(i, 1) for i in range(4, 12)] + \
                            [Vector2(i, 15) for i in range(4, 12)] + \
                            [Vector2(i, 14) for i in range(4, 12)] + \
                            [Vector2(i, 5) for i in range(5, 9)] + \
                            [Vector2(i, 6) for i in range(5, 9)] + \
                            [Vector2(i, 8) for i in range(10, 13)] + \
                            [Vector2(i, 9) for i in range(10, 13)] +\
                            [Vector2(6, i) for i in range(9, 12)] + \
                            [Vector2(7, i) for i in range(9, 12)]

    def draw_grass(self, color1=(175, 215, 70), color2=(167, 209, 61),
                   color3=(123, 124, 0), borders=[]):
        self.screen.fill(color1)
        grass_color = color2
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,
                                                 row * cell_size, cell_size,
                                                 cell_size
                                                 )
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,
                                                 row * cell_size, cell_size,
                                                 cell_size
                                                 )
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            for i in borders:
                border_rect = pygame.Rect(i.x * cell_size,
                                          i.y * cell_size, cell_size,
                                          cell_size
                                          )
                pygame.draw.rect(self.screen, pygame.Color(color3), border_rect)