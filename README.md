# Pygame snake game
This is my version of a snake game using the pygame module, which consists of five levels, and different kinds of bonus fruits. Graphics are drawn by importing pictures and placing them on the respective rectangles using pygame.
## Installing
In order to install pygame module:
Download the Python 3 installer package from the official website and install it, if not installed previously.Run the following in the terminal to install the Pygame library
```
pip3 install pygame
```
## Running the application
Download the source code from the repository and run the file just as any other Python script (.py) file.
In order to run the game use:
```
python3 main.py
```
## Snake
For initializing the snake we created a class snake which stores following methods: 

1.*Constructor*(from a color)

2.*draw_snake* - which is responsible for drawing our snake 

3.*update_head_graphics* - for knowing in which position is snake's head

4.*update_tail_graphics* - similar to prev method but its for the tail

5.*move_snake* - moves our snake along current direction, in case of collision adds another coordinate to our snakes body

6.*add_block* - checks if we need to add a block to our snake

7.*play_crunch_sound* - is used to play the sound while collision

## Fruit
Fruit class is pretty trivial, we have three types of fruits which we draw on random coordinates every time.

1.*Constructor* 

2.*draw_apple* - draws our usual fruit apple which is worth 1 poin

3.*draw_orange* - draws orange which is worth 5 points

4.*draw_watermelon* - draw a watermelon which indicates the victory

5.*randomize* - places our fruit on a random position using random module

## Grass
This class stores different level's maps.

1.*Constructor* - stores different level's borders(i.e lists with coordinates of walls)

2.*draw_grass* - responsible for drawing our maps on the screen
## Main(Logi)
In this class we simply define what our game should do in every iteration of the game loop.

1.*Constructor* - here we initialize our game elements(i.e. Snake, Frut, Grass)

2.*update* - used to update our game elements like moving snakes and checking if we lost.

3.*draw_elements* - this method is used to draw all our elements(i.e grass, snake, and fruit)

4.*check_colision* - this method checks if our snake ate the fruit, and randomizes the fruit in case it is on a wrong spot(a border, snakes body), also it increases the speed of the snake in case of collision

5.*check_next_level* - hecks if we passed to the next level

6.*pass_to_lvlv1*(2, 3, 4, 5) - in case of passing to the next level these methods reset the snake speed and snake itself, also they display the transfer to the next level

7.*check_fail* - here we check if our game is over

8.*update_record* - this method updates the top score table

9.*game_overa_output* - in this method we draw game over screen and play respective sounds also in case of beating the best record here we send a message saying that you own the best record.Also here we reset our score our level_pass fields and our snake and we update our record table.

10.*draw_top_score* - this method is used to output our score leaders 

11.*draw_score* - used to indicate current score in tge bottom right corner while playing


12.*game_won* - this function is responsible for outputing YOU Won and playing respective sounds in case of game completition. Here we also reset some values and our snake as well.

13.*pause* - this method is used in pause the game, and we can print any text we want in this pasue window by passing arguments our player wants to pasue the game, in order to continue the game we need to press c key and in order to quit it we press q key.

14.*check_game_won* - checks if we won the game
 
## Some other details

1.Our snake consists of blocks that iss why we define our screen as a grid, cell_size - size of one cell in pixels, cell_number - length of one side of our square(screen)

2. we initialize pygame, and define our screen, also we set starting snake_speed = 6.

3.later we initialize a clock instance in order to keep track of frames per second

4. we use pygame.mixer for playing sounds, and we use pygame.mixer.pre_init() in order to play those sounds without a delay
5. We keep track of time between key presses to avoid multiple key presses at once

## Game loop
Here we mainly work with pygame.event in order to process users commands, there are several if conditions which consider different cases. Also here we update the direction in each iteration, then we update main_game elements and draw them.



