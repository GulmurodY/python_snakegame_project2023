import time
import pygame
import sys
import random
from pygame.math import Vector2

top_score = [[], [], []]

file = open('record.txt', 'r')
for i, s in enumerate(file):
    top_score[i] = s.split()
    top_score[i][1] = int(top_score[i][1])
file.close()

username = input('Print your Username:')
color = int(input('Chose your snake color 1:black 2:blue 3:red'))


class SNAKE:
    def __init__(self, some_color):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.get_over_here = pygame.mixer.Sound(
            'Sound/scorpion-get-over-here.mp3')
        self.head_up = pygame.image.load(
            'black_snake_graphics/head_up.png'
        ).convert_alpha()
        self.head_down = pygame.image.load(
            'black_snake_graphics/head_down.png'
        ).convert_alpha()
        self.head_right = pygame.image.load(
            'black_snake_graphics/head_right.png'
        ).convert_alpha()
        self.head_left = pygame.image.load(
            'black_snake_graphics/head_left.png'
        ).convert_alpha()

        self.tail_up = pygame.image.load(
            'black_snake_graphics/tail_up.png'
        ).convert_alpha()
        self.tail_down = pygame.image.load(
            'black_snake_graphics/tail_down.png'
        ).convert_alpha()
        self.tail_right = pygame.image.load(
            'black_snake_graphics/tail_right.png'
        ).convert_alpha()
        self.tail_left = pygame.image.load(
            'black_snake_graphics/tail_left.png'
        ).convert_alpha()

        self.body_vertical = pygame.image.load(
            'black_snake_graphics/body_vertical.png'
        ).convert_alpha()
        self.body_horizontal = pygame.image.load(
            'black_snake_graphics/body_horizontal.png'
        ).convert_alpha()

        self.body_top_to_right = pygame.image.load(
            'black_snake_graphics/body_tr.png'
        ).convert_alpha()
        self.body_top_to_left = pygame.image.load(
            'black_snake_graphics/body_tl.png'
        ).convert_alpha()
        self.body_bottom_to_right = pygame.image.load(
            'black_snake_graphics/body_br.png'
        ).convert_alpha()
        self.body_bottom_to_left = pygame.image.load(
            'black_snake_graphics/body_bl.png'
        ).convert_alpha()

        if some_color == 2:
            self.head_up = pygame.image.load(
                'blue_snake_graphics/head_up.png'
            ).convert_alpha()
            self.head_down = pygame.image.load(
                'blue_snake_graphics/head_down.png'
            ).convert_alpha()
            self.head_right = pygame.image.load(
                'blue_snake_graphics/head_right.png'
            ).convert_alpha()
            self.head_left = pygame.image.load(
                'blue_snake_graphics/head_left.png'
            ).convert_alpha()

            self.tail_up = pygame.image.load(
                'blue_snake_graphics/tail_up.png'
            ).convert_alpha()
            self.tail_down = pygame.image.load(
                'blue_snake_graphics/tail_down.png'
            ).convert_alpha()
            self.tail_right = pygame.image.load(
                'blue_snake_graphics/tail_right.png'
            ).convert_alpha()
            self.tail_left = pygame.image.load(
                'blue_snake_graphics/tail_left.png'
            ).convert_alpha()

            self.body_vertical = pygame.image.load(
                'blue_snake_graphics/body_vertical.png'
            ).convert_alpha()
            self.body_horizontal = pygame.image.load(
                'blue_snake_graphics/body_horizontal.png'
            ).convert_alpha()

            self.body_top_to_right = pygame.image.load(
                'blue_snake_graphics/body_tr.png'
            ).convert_alpha()
            self.body_top_to_left = pygame.image.load(
                'blue_snake_graphics/body_tl.png'
            ).convert_alpha()
            self.body_bottom_to_right = pygame.image.load(
                'blue_snake_graphics/body_br.png'
            ).convert_alpha()
            self.body_bottom_to_left = pygame.image.load(
                'blue_snake_graphics/body_bl.png'
            ).convert_alpha()

        elif some_color == 3:
            self.head_up = pygame.image.load(
                'red_snake_graphics/head_up.png'
            ).convert_alpha()
            self.head_down = pygame.image.load(
                'red_snake_graphics/head_down.png'
            ).convert_alpha()
            self.head_right = pygame.image.load(
                'red_snake_graphics/head_right.png'
            ).convert_alpha()
            self.head_left = pygame.image.load(
                'red_snake_graphics/head_left.png'
            ).convert_alpha()

            self.tail_up = pygame.image.load(
                'red_snake_graphics/tail_up.png'
            ).convert_alpha()
            self.tail_down = pygame.image.load(
                'red_snake_graphics/tail_down.png'
            ).convert_alpha()
            self.tail_right = pygame.image.load(
                'red_snake_graphics/tail_right.png'
            ).convert_alpha()
            self.tail_left = pygame.image.load(
                'red_snake_graphics/tail_left.png'
            ).convert_alpha()

            self.body_vertical = pygame.image.load(
                'red_snake_graphics/body_vertical.png'
            ).convert_alpha()
            self.body_horizontal = pygame.image.load(
                'red_snake_graphics/body_horizontal.png'
            ).convert_alpha()

            self.body_top_to_right = pygame.image.load(
                'red_snake_graphics/body_tr.png'
            ).convert_alpha()
            self.body_top_to_left = pygame.image.load(
                'red_snake_graphics/body_tl.png'
            ).convert_alpha()
            self.body_bottom_to_right = pygame.image.load(
                'red_snake_graphics/body_br.png'
            ).convert_alpha()
            self.body_bottom_to_left = pygame.image.load(
                'red_snake_graphics/body_bl.png'
            ).convert_alpha()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or \
                            previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_top_to_left, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or \
                            previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bottom_to_left, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or \
                            previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_top_to_right, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or \
                            previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_bottom_to_right, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        elif self.direction != Vector2(0, 0):
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.get_over_here.play()



class FRUIT:
    def __init__(self):
        self.randomize()
        self.apple = pygame.image.load('Fruit/apple.png').convert_alpha()
        self.orange = pygame.image.load('Fruit/orange.png').convert_alpha()
        self.watermelon = pygame.image.load('Fruit/watermelone.png'
                                            ).convert_alpha()

    def draw_apple(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        screen.blit(self.apple, fruit_rect)

    def draw_orange(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        screen.blit(self.orange, fruit_rect)

    def draw_watermelon(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),
                                 int(self.pos.y * cell_size),
                                 cell_size, cell_size)
        screen.blit(self.watermelon, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class Grass:
    def __init__(self):
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
        screen.fill(color1)
        grass_color = color2
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size,
                                                 row * cell_size, cell_size,
                                                 cell_size
                                                 )
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size,
                                                 row * cell_size, cell_size,
                                                 cell_size
                                                 )
                        pygame.draw.rect(screen, grass_color, grass_rect)
            for i in borders:
                border_rect = pygame.Rect(i.x * cell_size,
                                          i.y * cell_size, cell_size,
                                          cell_size
                                          )
                pygame.draw.rect(screen, pygame.Color(color3), border_rect)


class MAIN:
    def __init__(self, some_color, some_username):
        self.game_score = 0
        self.best_record = False
        self.snake_color = some_color
        self.username = some_username
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        pygame.mixer.Sound('Sound/round_one.mp3').play()

        self.game_font = pygame.font.Font('Fonts/Snowy Winter.otf', 25)
        self.game_over_font = pygame.font.Font('Fonts/Snowy Winter.otf', 50)

        self.snake = SNAKE(self.snake_color)
        self.fruit = FRUIT()
        self.grass = Grass()

    def update(self):
        self.check_next_level()
        self.snake.move_snake()
        self.check_for_food()
        self.check_game_won()
        self.check_game_over()

    def draw_elements(self):
        if self.game_score < 10:
            self.grass.draw_grass()
        elif 20 > self.game_score >= 10:
            self.grass.draw_grass(pygame.Color('gold'), (255, 255, 0),
                                  (240, 0, 255), self.grass.borders_lvl2)
        elif 30 > self.game_score >= 20:
            self.grass.draw_grass((255, 100, 180), (255, 0, 230),
                                  (100, 40, 0), self.grass.borders_lvl3)
        elif 40 > self.game_score >= 10:
            self.grass.draw_grass((180, 255, 100), (180, 255, 150),
                                  (115, 0, 0), self.grass.borders_lvl4)
        else:
            self.grass.draw_grass((0, 255, 255, 255), (178, 34, 34, 255),
                                  (255, 200, 0), self.grass.borders_lvl5)
        if self.game_score in [5, 15, 25, 35, 44]:
            self.fruit.draw_orange()
        elif self.game_score == 49:
            self.fruit.draw_watermelon()
        else:
            self.fruit.draw_apple()
        self.snake.draw_snake()
        self.draw_current_score()

    def check_for_food(self):
        global snake_speed
        if self.fruit.pos == self.snake.body[0]:
            if self.game_score in [5, 15, 25, 35, 44]:
                self.game_score += 5
            else:
                self.game_score += 1
            snake_speed = snake_speed + 1
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
        if self.fruit.pos in self.snake.body[1:] or \
                (self.level2_pass and self.fruit.pos in
                 self.grass.borders_lvl2) or \
                (self.level3_pass and self.fruit.pos in
                 self.grass.borders_lvl3) or \
                (self.level4_pass and self.fruit.pos in
                 self.grass.borders_lvl4) or \
                (self.level5_pass and self.fruit.pos in
                 self.grass.borders_lvl5):
            self.fruit.randomize()

    def check_next_level(self):
        if self.game_score == 10 and not self.level2_pass:
            self.pass_to_lvl2()
            self.level2_pass = True
        if self.game_score == 20 and not self.level3_pass:
            self.pass_to_lvl3()
            self.level3_pass = True
        if self.game_score == 30 and not self.level4_pass:
            self.pass_to_lvl4()
            self.level4_pass = True
        if self.game_score == 40 and not self.level5_pass:
            self.pass_to_lvl5()
            self.level5_pass = True

    def pass_to_lvl2(self):
        global snake_speed
        snake_speed = 6
        del self.snake
        screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('ROUND 2', True,
                                                       pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.Sound('Sound/round2.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color)

    def pass_to_lvl3(self):
        global snake_speed
        snake_speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color)
        screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('ROUND 3', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.Sound('Sound/round3.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color)

    def pass_to_lvl4(self):
        global snake_speed
        snake_speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color)
        screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('ROUND 4', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.Sound('Sound/round4.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color)

    def pass_to_lvl5(self):
        global snake_speed
        snake_speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color)
        screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('FINAL ROUND', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.Sound('Sound/final_round .mp3').play()
        pygame.mixer.Sound('Sound/finish_him.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color)

    def check_game_over(self):
        if not 0 <= self.snake.body[0].x < cell_number or \
                not 0 <= self.snake.body[0].y < cell_number:
            self.game_over_output()
        for i in self.snake.body[1:]:
            if self.snake.body[0] == i:
                self.game_over_output()
        if self.level2_pass and 20 > self.game_score >= 10 and \
                self.snake.body[0] in self.grass.borders_lvl2:
            self.game_over_output()
        if self.level3_pass and 30 > self.game_score >= 20 and \
                self.snake.body[0] in self.grass.borders_lvl3:
            self.game_over_output()
        if self.level4_pass and 40 > self.game_score >= 30 and \
                self.snake.body[0] in self.grass.borders_lvl4:
            self.game_over_output()

    def update_record(self):
        global top_score, top_score, top_score
        if self.game_score >= top_score[0][1]:
            self.best_record = True
            top_score[2] = top_score[1]
            top_score[1] = top_score[0]
            top_score[0] = [self.username, self.game_score]
        elif self.game_score >= top_score[1][1]:
            top_score[2] = top_score[1]
            top_score[1] = [self.username, self.game_score]
        elif self.game_score >= top_score[1][1]:
            top_score[2] = [self.username, self.game_score]
        open('record.txt', 'w').close()
        with open('record.txt', 'w') as f:
            f.write(f'{top_score[0][0]} {top_score[0][1]} \n')
            f.write(f'{top_score[1][0]} {top_score[1][1]} \n')
            f.write(f'{top_score[2][0]} {top_score[2][1]} \n')

    def game_over_output(self):
        global top_score, top_score, top_score, snake_speed
        self.update_record()
        del self.snake
        self.snake = SNAKE(self.snake_color)
        snake_speed = 6
        screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render(
            'Your Score is : ' + str(self.game_score), True,
            pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.center = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.music.stop()
        pygame.mixer.Sound('Sound/laugh.mp3').play()
        pygame.mixer.Sound('Sound/you_suck.mp3').play()
        pygame.display.flip()
        pygame.mixer.music.play()
        self.game_score = 0
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        time.sleep(2)
        if self.best_record:
            screen.fill(pygame.Color('white'))
            pause_surface = self.game_over_font.render('Congrats', True,
                                                       pygame.Color('red'))
            pause_rect = pause_surface.get_rect()
            pause_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
            press_to_continue_surface = self.game_font.render(
                "You own the best record", True, pygame.Color('blue'))
            press_to_continue_rect = press_to_continue_surface.get_rect()
            press_to_continue_rect.midtop = (cell_number * cell_size / 2,
                                             cell_number * cell_size / 2 + 50)
            screen.blit(pause_surface, pause_rect)
            screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()
            time.sleep(2)
            self.best_record = False
        self.draw_top_score()
        self.pause("PAUSED", 'Press C to restart')
        pygame.mixer.Sound('Sound/round_one.mp3').play()

    def draw_top_score(self):
        wait = True
        while wait:
            for some_event in pygame.event.get():
                if some_event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if some_event.type == pygame.KEYDOWN:
                    if some_event.key == pygame.K_c:
                        wait = False

                    elif some_event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            screen.fill(pygame.Color('white'))
            pause_surface = self.game_over_font.render('Top Scores', True,
                                                       pygame.Color('red'))
            pause_rect = pause_surface.get_rect()
            pause_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 4)

            first_surface = self.game_font.render(f'1: {top_score[0][0]} '
                                                  f'{top_score[0][1]}',
                                                  True, pygame.Color('blue'))
            first_surface_rect = first_surface.get_rect()
            first_surface_rect.midtop = (cell_number * cell_size / 2,
                                         cell_number * cell_size / 4 + 50)

            second_surface = self.game_font.render(f'2: {top_score[1][0]} '
                                                   f'{top_score[1][1]}',
                                                   True, pygame.Color('blue'))
            second_surface_rect = second_surface.get_rect()
            second_surface_rect.midtop = (cell_number * cell_size / 2,
                                          cell_number * cell_size / 4 + 100)

            third_surface = self.game_font.render(f'3: {top_score[2][0]} '
                                                  f'{top_score[2][1]}',
                                                  True, pygame.Color('blue'))
            third_surface_rect = third_surface.get_rect()
            third_surface_rect.midtop = (cell_number * cell_size / 2,
                                         cell_number * cell_size / 4 + 150)

            press_to_continue_surface = self.game_font.render(
                'press c to proceed', True, pygame.Color('green'))
            press_to_continue_rect = press_to_continue_surface.get_rect()
            press_to_continue_rect.midtop = (cell_number * cell_size / 2,
                                             cell_number * cell_size / 4 + 250
                                             )

            screen.blit(pause_surface, pause_rect)
            screen.blit(first_surface, first_surface_rect)
            screen.blit(second_surface, second_surface_rect)
            screen.blit(third_surface, third_surface_rect)
            screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()

    def draw_current_score(self):
        score_text = 'Your Score: ' + str(self.game_score)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 100)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rect)

    def game_won(self):
        global top_score, top_score, top_score
        screen.fill(pygame.Color('white'))
        game_over_surface = self.game_over_font.render(
            'YOU WON!', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        screen.blit(game_over_surface, game_over_rect)

        pygame.mixer.music.stop()
        pygame.mixer.Sound('Sound/flawless_victory.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        del self.snake
        self.snake = SNAKE(self.snake_color)
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        pygame.mixer.music.play()
        self.update_record()
        self.game_score = 0
        global snake_speed
        snake_speed = 10
        if self.best_record:
            self.pause('You are the champion!!!', 'press C to continue')
            self.best_record = False
        self.draw_top_score()
        self.pause("PAUSED", 'Press C to restart')
        pygame.mixer.Sound('Sound/round_one.mp3').play()

    def pause(self, text1="PAUSED", text2='Press C to continue'):
        paused = True
        while paused:
            for some_event in pygame.event.get():
                if some_event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if some_event.type == pygame.KEYDOWN:
                    if some_event.key == pygame.K_c:
                        paused = False

                    elif some_event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            screen.fill(pygame.Color('white'))
            pause_surface = self.game_over_font.render(text1, True,
                                                       pygame.Color('red'))
            pause_rect = pause_surface.get_rect()
            pause_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
            press_to_continue_surface = self.game_font.render(
                text2, True, pygame.Color('blue'))
            press_to_continue_rect = press_to_continue_surface.get_rect()
            press_to_continue_rect.midtop = (cell_number * cell_size / 2,
                                             cell_number * cell_size / 2 + 50)
            screen.blit(pause_surface, pause_rect)
            screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()

    def check_game_won(self):
        if self.game_score == 50:
            self.game_won()


cell_size = 40
cell_number = 16
pygame.init()
screen = pygame.display.set_mode((cell_number * cell_size,
                                  cell_number * cell_size))
clock = pygame.time.Clock()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.music.load("Sound/theme_song.mp3")
pygame.mixer.music.play(-1)
main_game = MAIN(color, username)

prev_keytime = time.time() - 1
prev_key = pygame.K_c

snake_speed = 6

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
    clock.tick(snake_speed)
