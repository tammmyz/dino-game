## @file character.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the Character class which is used to generate objects in chromedino.py
#  @date 03/18/2022

import images
import pygame


## @brief Character is a class that implements a game character
#  @details the character class defines the position and the images for
#   the character movements such as duck, jump and run. It is responsible for drawing
#   the character to the screen.


class Character:
    # setting constants for the dinosaur position on screen and velocity
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    ## @brief Constructor method for Character
    def __init__(self):
        self.duck_img = images.DUCKING  # list of ducking images
        self.run_img = images.RUNNING_THEME
        self.jump_img = images.JUMPING

        # starting dino positions
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL  # setting jump velocity
        self.image = self.run_img[0]  # setting first run image
        self.dino_rect = self.image.get_rect()  # getting the dimensions of the 1st image
        self.dino_rect.x = self.X_POS  # setting the x-position of the dino rectangle
        self.dino_rect.y = self.Y_POS  # setting the y-position of the dino rectangle

    ## @brief updates the current dinosaur image based off user input
    #  @param userInput keyboard input (whatever key is pressed)
    #  @return updates screen
    def update(self, userInput):

        # updating the current status and changing the images
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        # resetting the index to 0 if necessary
        if self.step_index >= 10:
            self.step_index = 0

        # updates duck, run, jump images based off the userInput (key pressed)

        # if user pressing up, space and not already jumping, put the jump image
        if (userInput[pygame.K_UP] or userInput[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True

        # if user is pressing down and the dino is not jumping the dino ducks
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False

        # if user is not pressing down or is not jumping then the dino is images.RUNNING
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

    ## @brief changes the duck image and the position of the dino rectangle
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]  # updating the image according to remainder
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS  # setting the positions
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    ## @brief changes the run image and the position of the dino rectangle
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    ## @brief changes the jump image and the position of the dino rectangle
    def jump(self):
        self.image = self.jump_img  # setting it to the only jumping image
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4  # changing the height of y according to the velocity
            self.jump_vel -= 0.8  # changing the velocity
        if self.jump_vel < -self.JUMP_VEL:  # once the velocity passes 0 (it resets jump velocity) - because we are on the ground
            self.dino_jump = False  # set jump to false
            self.jump_vel = self.JUMP_VEL  # resets velocity value to constant

    ## @brief draws the dinosaur to the screen
    #  @param SCREEN screen object from the pygame library
    def draw(self, SCREEN):
        # blit draws the image to the screen (that we set)
        # in the specific destination (x, y coordinates)
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
