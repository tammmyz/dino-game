## @file large_obstacle.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the large obstacle class which is used to generate objects in chromedino.py
#  @date 03/18/2022

import random
from obstacle import Obstacle

## @brief LargeObstacle is a class that implements a large obstacle
#  @details the LargeObstacle class inherits the Obstacle class and sets the y-position

class LargeObstacle(Obstacle):

    ## @brief Constructor method for a LargeObstacles
    #  @param image a list of large obstacle images
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300