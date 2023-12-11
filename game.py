import pygame
import time
from Snake import SNAKE
from grass import Grass
from fruit import FRUIT
from globals import cell_size, cell_number

top_score = [[], [], []]

file = open('record.txt', 'r')
for i, s in enumerate(file):
    top_score[i] = s.split()
    top_score[i][1] = int(top_score[i][1])
file.close()


class MAIN:
    def __init__(self, some_color, some_username, screen):
        self.game_score = 0
        self.screen = screen
        self.best_record = False
        self.snake_color = some_color
        self.username = some_username
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        # pygame.mixer.Sound('Sound/round_one.mp3').play()

        self.game_font = pygame.font.Font('Fonts/Snowy Winter.otf', 25)
        self.game_over_font = pygame.font.Font('Fonts/Snowy Winter.otf', 50)

        self.snake = SNAKE(self.snake_color, self.screen)
        self.fruit = FRUIT(screen)
        self.grass = Grass(screen)

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
        if self.fruit.pos == self.snake.body[0]:
            if self.game_score in [5, 15, 25, 35, 44]:
                self.game_score += 5
            else:
                self.game_score += 1
            self.snake.speed += 1
            self.fruit.randomize()
            self.snake.add_block()
            # self.snake.play_crunch_sound()
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
        self.snake.speed = 6
        del self.snake
        self.screen.fill(pygame.Color('black'))
        # game_over_surface = self.game_over_font.render('ROUND 2', True,
        #                                                pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.mixer.Sound('Sound/round2.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color, self.screen)

    def pass_to_lvl3(self):
        self.snake.speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color, self.screen)
        self.screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('ROUND 3', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)
        # pygame.mixer.Sound('Sound/round3.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color, self.screen)

    def pass_to_lvl4(self):
        self.snake.speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color, self.screen)
        self.screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('ROUND 4', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)
        # pygame.mixer.Sound('Sound/round4.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color, self.screen)

    def pass_to_lvl5(self):
        self.snake.speed = 6
        del self.snake
        self.snake = SNAKE(self.snake_color, self.screen)
        self.screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render('FINAL ROUND', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2, cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)
        # pygame.mixer.Sound('Sound/final_round .mp3').play()
        # pygame.mixer.Sound('Sound/finish_him.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        self.pause()
        self.snake = SNAKE(self.snake_color, self.screen)

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
        global top_score, top_score, top_score
        self.snake.speed = 6
        self.update_record()
        del self.snake
        self.snake = SNAKE(self.snake_color, self.screen)
        self.screen.fill(pygame.Color('black'))
        game_over_surface = self.game_over_font.render(
            'Your Score is : ' + str(self.game_score), True,
            pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.center = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)
        # pygame.mixer.music.stop()
        # pygame.mixer.Sound('Sound/laugh.mp3').play()
        # pygame.mixer.Sound('Sound/you_suck.mp3').play()
        pygame.display.flip()
        pygame.mixer.music.play()
        self.game_score = 0
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        time.sleep(2)
        if self.best_record:
            self.screen.fill(pygame.Color('white'))
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
            self.screen.blit(pause_surface, pause_rect)
            self.screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()
            time.sleep(2)
            self.best_record = False
        self.draw_top_score()
        self.pause("PAUSED", 'Press C to restart')
        # pygame.mixer.Sound('Sound/round_one.mp3').play()

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
            self.screen.fill(pygame.Color('white'))
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

            self.screen.blit(pause_surface, pause_rect)
            self.screen.blit(first_surface, first_surface_rect)
            self.screen.blit(second_surface, second_surface_rect)
            self.screen.blit(third_surface, third_surface_rect)
            self.screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()

    def draw_current_score(self):
        score_text = 'Your Score: ' + str(self.game_score)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 100)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        self.screen.blit(score_surface, score_rect)

    def game_won(self):
        global top_score, top_score, top_score
        self.screen.fill(pygame.Color('white'))
        game_over_surface = self.game_over_font.render(
            'YOU WON!', True, pygame.Color('red'))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (cell_number * cell_size / 2,
                                 cell_number * cell_size / 2)
        self.screen.blit(game_over_surface, game_over_rect)

        # pygame.mixer.music.stop()
        # pygame.mixer.Sound('Sound/flawless_victory.mp3').play()
        pygame.display.flip()
        time.sleep(2)
        del self.snake
        self.snake = SNAKE(self.snake_color, self.screen)
        self.level2_pass = False
        self.level3_pass = False
        self.level4_pass = False
        self.level5_pass = False
        pygame.mixer.music.play()
        self.update_record()
        self.game_score = 0
        self.snake.speed = 6
        if self.best_record:
            self.pause('You are the champion!!!', 'press C to continue')
            self.best_record = False
        self.draw_top_score()
        self.pause("PAUSED", 'Press C to restart')
        # pygame.mixer.Sound('Sound/round_one.mp3').play()

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
            self.screen.fill(pygame.Color('white'))
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
            self.screen.blit(pause_surface, pause_rect)
            self.screen.blit(press_to_continue_surface, press_to_continue_rect)
            pygame.display.flip()

    def check_game_won(self):
        if self.game_score == 50:
            self.game_won()
