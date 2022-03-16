## @file obstacle.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the Character class which is used to generate objects in chromedino.py
#  @date 03/18/2022

import global_var


## @brief Obstacle is a class that implements a game obstacle
#  @details the obstacle class draws an obstacle to the screen and is used as the
#   parent class for small and large obstacle.

class Obstacle:

    ## @brief Constructor method for Character
    #  @param image a list of obstacle object images
    #  @param type  an integer value of 1 or 2 to determine which obstacle gets shown to the screen
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = global_var.SCREEN_WIDTH

    ## @brief determines the x location of the obstacle and pops the current obstacle off the obstacle list.
    def update(self):
        self.rect.x -= global_var.game_speed
        if self.rect.x < -self.rect.width:
            global_var.obstacles.pop()

    ## @brief draws the obstacle to the screen
    #  @param SCREEN the screen image
    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)