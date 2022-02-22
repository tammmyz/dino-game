# !/usr/bin/python
# -*- coding: utf-8 -*-

# importing standard libraries
import datetime
import os
import random
import threading
import pygame
import time

# importing local application/library specific imports
from cloud import Cloud
from large_cactus import LargeCactus
from small_cactus import SmallCactus
from obstacle import Obstacle
import global_var
import images

# initializing the game
pygame.init()

# Global Constants
# global_var.SCREEN_HEIGHT = 600
# global_var.global_var.SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((global_var.SCREEN_WIDTH, global_var.SCREEN_HEIGHT))

# setting up the window - title and setting the game icon (top left corner)
pygame.display.set_caption("Chrome Dino Runner")

Ico = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Ico)


# # setting up images for different icons and putting them in a list
# images.RUNNING = [
#     pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
#     pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
# ]
# JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
# images.images.DUCKING = [
#     pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
#     pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
# ]
#
# images.SMALL_CACTUS = [
#     pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
#     pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
#     pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
# ]
# LARGE_CACTUS = [
#     pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
#     pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
#     pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
# ]
#
# BIRD = [
#     pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
#     pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
# ]
#
# CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))
#
# # putting in the ground graphic
# BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

# FONT_COLOR = (0, 0, 0)  # setting font to black


# setting up the dinosaur class - need to separate into it's own module
class Dinosaur:
    # setting constants for the dinosaur position on screen and velocity
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    # initializing dinosaur images
    def __init__(self):
        self.duck_img = images.DUCKING  # list of ducking images
        self.run_img = images.RUNNING
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


#
# class Cloud:
#     def __init__(self):
#         self.x = global_var.SCREEN_WIDTH + random.randint(800, 1000)
#         self.y = random.randint(50, 100)
#         self.image = CLOUD
#         self.width = self.image.get_width()
#
#     def update(self):
#         self.x -= game_speed
#         if self.x < -self.width:
#             self.x = global_var.SCREEN_WIDTH + random.randint(2500, 3000)
#             self.y = random.randint(50, 100)
#
#     def draw(self, SCREEN):
#         SCREEN.blit(self.image, (self.x, self.y))
#
#
# class Obstacle:
#     def __init__(self, image, type):
#         self.image = image
#         self.type = type
#         self.rect = self.image[self.type].get_rect()
#         self.rect.x = global_var.SCREEN_WIDTH
#
#     def update(self):
#         self.rect.x -= global_var.game_speed
#         if self.rect.x < -self.rect.width:
#             obstacles.pop()
#
#     def draw(self, SCREEN):
#         SCREEN.blit(self.image[self.type], self.rect)


# class SmallCactus(Obstacle):
#     def __init__(self, image):
#         self.type = random.randint(0, 2)
#         super().__init__(image, self.type)
#         self.rect.y = 325

#
# class LargeCactus(Obstacle):
#     def __init__(self, image):
#         self.type = random.randint(0, 2)
#         super().__init__(image, self.type)
#         self.rect.y = 300


class Bird(Obstacle):
    BIRD_HEIGHTS = [250, 290, 320]

    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


def main():
    print("main: length: ",len(global_var.obstacles))
    # global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    # global obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud()
    # game_speed = 20
    # x_pos_bg = 0
    # y_pos_bg = 380
    # points = 0
    font = pygame.font.Font("freesansbold.ttf", 20)
    global_var.obstacles = []
    death_count = 0
    pause = False

    def score():
        global_var.points, global_var.game_speed
        global_var.points += 1
        if global_var.points % 100 == 0:
            global_var.game_speed += 1
        current_time = datetime.datetime.now().hour
        with open("score.txt", "r") as f:
            score_ints = [int(x) for x in f.read().split()]
            highscore = max(score_ints)
            if global_var.points > highscore:
                highscore = global_var.points
            text = font.render("High Score: " + str(highscore) + "  Points: " + str(global_var.points), True,
                               global_var.FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (900, 40)
        SCREEN.blit(text, textRect)

    def background():
        # global_var.x_pos_bg, global_var.y_pos_bg
        image_width = images.BG.get_width()
        SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))
        SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
        if global_var.x_pos_bg <= -image_width:
            SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
            global_var.x_pos_bg = 0
        global_var.x_pos_bg -= global_var.game_speed

    def unpause():
        nonlocal pause, run
        pause = False
        run = True

    def paused():
        nonlocal pause
        pause = True
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render("Game Paused, Press 'u' to Unpause", True, global_var.FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                run = False
                paused()

        current_time = datetime.datetime.now().hour
        if 7 < current_time < 19:
            SCREEN.fill((255, 255, 255))
        else:
            SCREEN.fill((0, 0, 0))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)  # player is an object of dinosaur that is always looking for input

        if len(global_var.obstacles) == 0:
            if random.randint(0, 2) == 0:
                global_var.obstacles.append(SmallCactus(images.SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                global_var.obstacles.append(LargeCactus(images.LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                global_var.obstacles.append(Bird(images.BIRD))

        for obstacle in global_var.obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    run = True
    while run:
        current_time = datetime.datetime.now().hour
        if 7 < current_time < 19:
            global_var.FONT_COLOR = (0, 0, 0)
            SCREEN.fill((255, 255, 255))
        else:
            global_var.FONT_COLOR = (255, 255, 255)
            SCREEN.fill((128, 128, 128))
        font = pygame.font.Font("freesansbold.ttf", 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, global_var.FONT_COLOR)
        elif death_count > 0:
            print("made it here")
            text = font.render("Press any Key to Restart", True, global_var.FONT_COLOR)
            score = font.render("Your Score: " + str(global_var.points), True, global_var.FONT_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
            f = open("score.txt", "a")
            f.write(str(global_var.points) + "\n")
            f.close()
            with open("score.txt", "r") as f:
                score = (
                    f.read()
                )  # Read all file in case values are not on a single line
                score_ints = [int(x) for x in score.split()]  # Convert strings to ints
            highscore = max(score_ints)  # sum all elements of the list
            hs_score_text = font.render(
                "High Score : " + str(highscore), True, global_var.FONT_COLOR
            )
            hs_score_rect = hs_score_text.get_rect()
            hs_score_rect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 100)
            SCREEN.blit(hs_score_text, hs_score_rect)
        textRect = text.get_rect()
        textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(images.RUNNING[0], (global_var.SCREEN_WIDTH // 2 - 20, global_var.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            print("EVENT")
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                print("keydown?")
                main()


t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()
