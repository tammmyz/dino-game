## @file bird.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the small obstacle class which is used to generate objects in small_obstacle.py
#  @date 03/18/2022


from obstacle import Obstacle
import random

## @brief Bird is a class that implements a bird obstacle to the screen
#  @details the obstacle class draws an obstacle to the screen and is a child class
#   of obstacle.

class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    ## @brief Constructor method for Bird
    #  @param image a list of bird obstacle images
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0

    ## @brief draws the obstacle to the screen
    #  @param SCREEN the screen image
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1