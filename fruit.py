import pygame
import random
from pygame.math import Vector2
from globals import cell_size, cell_number


class FRUIT:
    def __init__(self, screen):
        self.screen = screen
        self.randomize()
        self.apple = pygame.image.load('Fruit/apple.png').convert_alpha()
        self.orange = pygame.image.load('Fruit/orange.png').convert_alpha()
        self.watermelon = pygame.image.load('Fruit/watermelone.png'
                                            ).convert_alpha()

    def draw_apple(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        self.screen.blit(self.apple, fruit_rect)

    def draw_orange(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        self.screen.blit(self.orange, fruit_rect)

    def draw_watermelon(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        self.screen.blit(self.watermelon, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)