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
from bird import Bird
from dinosaur import Dinosaur
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

main_flag = False

def instructions():
    global main_flag
    # Adding background
    SCREEN.fill((255,255,255))
    image_width = images.BG.get_width()
    SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))

    # Setting up title
    font = pygame.font.Font("freesansbold.ttf", 30)
    title = font.render("INSTRUCTIONS", True, "black")
    titleRect = title.get_rect()
    titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
    SCREEN.blit(title, titleRect)

    # importing images --> transfer to img.py
    up_img = pygame.image.load(os.path.join("assets/Keys", "up.jpg"))
    up_img = pygame.transform.scale(up_img, (50,50))

    w_img = pygame.image.load(os.path.join("assets/Keys", "w.jpg"))
    w_img = pygame.transform.scale(w_img, (46,46))

    cactus_img = pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png"))
    cactus_img = pygame.transform.scale(cactus_img, (46,47))

    down_img = pygame.image.load(os.path.join("assets/Keys", "down.jpg"))
    down_img = pygame.transform.scale(down_img, (42,47))

    s_img = pygame.image.load(os.path.join("assets/Keys", "s.jpg"))
    s_img = pygame.transform.scale(s_img, (45,47))

    bird_img = pygame.image.load(os.path.join("assets/Bird", "Bird1.png"))
    bird_img = pygame.transform.scale(bird_img, (46,47))

    p_img = pygame.image.load(os.path.join("assets/Keys", "p.png"))
    p_img = pygame.transform.scale(p_img, (38,40))

    u_img = pygame.image.load(os.path.join("assets/Keys", "u.png"))
    u_img = pygame.transform.scale(u_img, (38,40))

    # Instruction Body
    body_font = pygame.font.Font("freesansbold.ttf", 20)
    press_text = body_font.render("Press", True, "black")
    jump_text = body_font.render("to JUMP", True, "black")
    duck_text = body_font.render("to DUCK", True, "black")
    or_text = body_font.render("or", True, "black")
    pause_text = body_font.render("to PAUSE the game", True, "black")
    unpause_text = body_font.render("to UNPAUSE the game", True, "black")

    # Display instuction body 
    SCREEN.blit(press_text, (373, 140))
    SCREEN.blit(up_img, (433, 120))
    SCREEN.blit(or_text, (493, 140))
    SCREEN.blit(w_img, (518, 122))
    SCREEN.blit(jump_text, (573, 140))
    SCREEN.blit(cactus_img, (668, 120))

    SCREEN.blit(press_text, (373, 220))
    SCREEN.blit(down_img, (438, 200))
    SCREEN.blit(or_text, (493, 220))
    SCREEN.blit(s_img, (520, 200))
    SCREEN.blit(duck_text, (573, 220))
    SCREEN.blit(bird_img, (668, 200))

    SCREEN.blit(press_text, (373, 290))
    SCREEN.blit(p_img, (440, 275))
    SCREEN.blit(pause_text, (493, 290))

    SCREEN.blit(press_text, (373, 355))
    SCREEN.blit(u_img, (440, 340))
    SCREEN.blit(unpause_text, (493, 355))

    if not main_flag:
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
        SCREEN.blit(main_text, (320, 450))
    

    pygame.display.update()


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
    global_var.points = 0
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
        instruction_text = font.render("Press 'i' to see instructions", True, global_var.FONT_COLOR)
        textRect = text.get_rect()
        textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 3)
        SCREEN.blit(text, textRect)
        SCREEN.blit(instruction_text, (global_var.SCREEN_WIDTH // 3, global_var.SCREEN_HEIGHT // 3 + 50))
        pygame.display.update()

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                    unpause()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    print("pressed i")
                    instructions()

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
    global main_flag
    main_flag = False
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

        instructions_text = font.render("How to play", True, global_var.FONT_COLOR)
        x, y, w, h = instructions_text.get_rect(center=(global_var.SCREEN_WIDTH // 2 ,global_var.SCREEN_HEIGHT // 1.5))

        SCREEN.blit(text, textRect)
        SCREEN.blit(images.RUNNING[0], (global_var.SCREEN_WIDTH // 2 - 20, global_var.SCREEN_HEIGHT // 2 - 140))

        # Adding instuctions button on menu
        if death_count == 0:
            SCREEN.blit(instructions_text, (global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6))
            mouse_pos = pygame.mouse.get_pos() #get mouse cursor position
        
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
                main_flag = True
                main()

            #Check if instructions was pressed
            if death_count == 0 and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x, x+w) and mouse_pos[1] in range(y, y+h):
                print("How to play")
                instructions()
                while not main_flag:
                    for event in pygame.event.get():
                        print("EVENT")
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            print("keydown?")
                            menu(0)

                    
            
                    
        
t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()
