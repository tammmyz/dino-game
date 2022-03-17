## @file small_obstacle.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the small obstacle class which is used to generate objects in chromedino.py
#  @date 03/18/2022

from obstacle import Obstacle
import random

## @brief small_obstacle is a class that implements a small obstacle
#  @details the small obstacle class which inherits the Obstacle class and sets the y-position of the image

class SmallObstacle(Obstacle):

    ## @brief Constructor method for SmallObstacle
    #  @param image a list of small obstacle images
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325