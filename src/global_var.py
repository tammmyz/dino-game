## @file global_var.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the global variables for chromedino.py
#  @date 03/18/2022

import pygame


# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FONT_COLOR = (0, 0, 0)  # setting font to black
KIPLING_COLOR = (0, 100, 255) 

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
leaderboard_flag = False

# testing variables
test_leaderboard = False
test_leaderboard2 = False
test_settings = False
test_instructions = False
test_pause = False
