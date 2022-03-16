## @file large_obstacle.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the Character class which is used to generate objects in chromedino.py
#  @date 03/18/2022

import random
from obstacle import Obstacle

class LargeObstacle(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300