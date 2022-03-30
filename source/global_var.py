## @file global_var.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the global variables for chromedino.py
#  @date 03/18/2022

import pygame


# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FONT_COLOR = (0, 0, 0)  # setting font to black

# global variables
game_speed = 20
x_pos_bg = 0
y_pos_bg = 380
points = 0
obstacles = []
username = ""
high_score = 0
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# global variables used for settings
audio = True  # default is that sound will play
theme = 'default'  # options include "student" and "corona" version.


start_flag = False 
restart_flag = False
game_track_flag = False
instructions_flag = False