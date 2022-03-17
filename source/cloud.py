## @file obstacle.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the cloud class class which is used in chromedino.py
#  @date 03/18/2022


import random
import global_var
import images

## @brief CLoud is a class that implements a cloud image onto the screen
#  @details the cloud is part of the aesthetics of the game track.

class Cloud:

    ## @brief Constructor method for cloud
    def __init__(self):
        self.x = global_var.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = images.CLOUD
        self.width = self.image.get_width()


    ## @brief updates the cloud image to the screen and changes it's x-position
    def update(self):
        self.x -= global_var.game_speed
        if self.x < -self.width:
            self.x = global_var.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    ## @brief draws the obstacle to the screen
    #  @param SCREEN the screen image
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))