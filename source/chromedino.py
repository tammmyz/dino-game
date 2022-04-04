## @file chromedino.py
#  @author Anjola Adewale, Sheridan Fong, Chelsea Maramot 
# @brief Contains the main controller for the game
# @date 03/18/2022
# importing libraries
import datetime
import os
import random
import threading
from turtle import update
import pygame
from display import *
import time
from username import get_username
from leader import *
# importing local application/library specific imports
from cloud import Cloud
from large_obstacle import LargeObstacle
from small_obstacle import SmallObstacle
from bird import Bird
from character import Character
from obstacle import Obstacle
import global_var
import images

# initializing the game
pygame.init()
pygame.font.init()
pygame.mixer.init()

jump_sound = pygame.mixer.Sound("assets/audio/jump.mp3")
milestone_sound = pygame.mixer.Sound("assets/audio/milestone.mp3")
death_sound = pygame.mixer.Sound("assets/audio/death.mp3")
duck_sound = pygame.mixer.Sound("assets/audio/duck.mp3")
corona_sound = pygame.mixer.Sound("assets/audio/corona_theme.mp3")
dinosaur_sound = pygame.mixer.Sound("assets/audio/dino_theme.mp3")
student_sound = pygame.mixer.Sound("assets/audio/student_theme.mp3")
audio_on_sound = pygame.mixer.Sound("assets/audio/audio_on.mp3")
audio_off_sound = pygame.mixer.Sound("assets/audio/audio_off.mp3")


# Global Constants
# global_var.SCREEN_HEIGHT = 600
# global_var.global_var.SCREEN_WIDTH = 1100
# SCREEN = pygame.display.set_mode((global_var.SCREEN_WIDTH, global_var.SCREEN_HEIGHT))

# setting up the window - title and setting the game icon (top left corner)
pygame.display.set_caption("Chrome Dino Runner")

Ico = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Ico)

# variable used to track if you are on the main page or not?
global_var.game_track_flag = False

## @brief Calls all classes and generates objects to play the game
def main():
   print("main: length: ",len(global_var.obstacles))
   # global game_speed, x_pos_bg, y_pos_bg, points, obstacles
   # global obstacles
   run = True
   clock = pygame.time.Clock()
   player = Character()
   cloud = Cloud()
   # game_speed = 20
   # x_pos_bg = 0
   # y_pos_bg = 380
   global_var.points = 0
   font = pygame.font.Font("freesansbold.ttf", 20)
   global_var.obstacles = []
   global_var.game_speed = 20
   death_count = 0
   pause = False

   ## @brief Updates game points and high score and displays it to the screen during game play
   def score():
       get_leaders()
       global_var.points, global_var.game_speed
       global_var.points += 1
       if global_var.points % 100 == 0:
           global_var.game_speed += 1
       current_time = datetime.datetime.now().hour
       if global_var.points > global_var.high_score:
           global_var.high_score = global_var.points
       text = font.render("High Score: " + str(global_var.high_score) + "  Points: " + str(global_var.points), True,
                       global_var.FONT_COLOR)
       textRect = text.get_rect()
       textRect.center = (900, 40)
       global_var.SCREEN.blit(text, textRect)

   ## @brief Updates the background of the game according to game speed
   def background():
       # global_var.x_pos_bg, global_var.y_pos_bg
       image_width = images.BG.get_width()
       global_var.SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))
       global_var.SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
       if global_var.x_pos_bg <= -image_width:
           global_var.SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
           global_var.x_pos_bg = 0
       global_var.x_pos_bg -= global_var.game_speed

   ## @brief Unpauses the game by setting appropriate boolean variables
   def unpause():
       nonlocal pause, run
       pause = False
       run = True

   ## @brief Pauses the game by setting appropriate boolean variables and displaying the
   # appropriate text and graphics to the screen.
   def paused():
       nonlocal pause
       pause = True
       test_pause = pause
       font = pygame.font.Font("freesansbold.ttf", 30)
       text = font.render("Game Paused, Press 'u' to Unpause", True, global_var.FONT_COLOR)
       instruction_text = font.render("Press 'i' to see instructions", True, global_var.FONT_COLOR)
       textRect = text.get_rect()
       textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 3)
       global_var.SCREEN.blit(text, textRect)
       global_var.SCREEN.blit(instruction_text, (global_var.SCREEN_WIDTH // 3, global_var.SCREEN_HEIGHT // 3 + 50))
       pygame.display.update()

       while pause and test_pause:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()
               if event.type == pygame.KEYDOWN and event.key == pygame.K_u:
                   unpause()
               if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                   print("pressed i")

                   '''
                   if global_var.test_instructions:
                       #global_var.instructions_flag = True
                       return
                   '''

                   instructions()
  
   while run:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
               run = False
               paused()

           if global_var.audio:
               if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                   jump_sound.play()
               if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                   duck_sound.play()
         
      
       #if global_var.points % 1000 == 0 and global_var.points != 0:
       #    print("REACHED")
       #    milestone_sound.play()

       current_time = datetime.datetime.now().hour
       if 7 < current_time < 19:
           global_var.SCREEN.fill((255, 255, 255))
          
       else:
           global_var.SCREEN.fill((0, 0, 0))
       userInput = pygame.key.get_pressed()

       player.draw(global_var.SCREEN)
       player.update(userInput)  # player is an object of dinosaur that is always looking for input

  
       if len(global_var.obstacles) == 0:
           if random.randint(0, 2) == 0:
               global_var.obstacles.append(SmallObstacle(images.OBSTACLE_ONE))
           elif random.randint(0, 2) == 1:
               global_var.obstacles.append(LargeObstacle(images.OBSTACLE_TWO))
           elif random.randint(0, 2) == 2:
               global_var.obstacles.append(Bird(images.OBSTACLE_FLYING))

       for obstacle in global_var.obstacles:
           obstacle.draw(global_var.SCREEN)
           obstacle.update()
           if player.dino_rect.colliderect(obstacle.rect):

               if global_var.audio:
                   death_sound.play()

               pygame.time.delay(2000)
               death_count += 1
               menu(death_count)

              

       background()

       cloud.draw(global_var.SCREEN)
       cloud.update()

       score()

       clock.tick(30)
       pygame.display.update()

## @brief Adds the user's username and score to score.txt after each death
def update_score():
   if (len(global_var.username) == 0):
               global_var.username = "No_User_Entered"
   f = open("score.txt", "a+")
   f.write("\n" + global_var.username + " " + str(global_var.points))
   f.close()

## @brief Displays the restart page texts and graphics
#  @return A tuple containing the positional coordinates of the Leaderboard text
def restart():
   leader_rect = []
   font = pygame.font.Font("freesansbold.ttf", 30)
   score = font.render("Your Score: " + str(global_var.points), True, global_var.FONT_COLOR)
   scoreRect = score.get_rect()
   scoreRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 50)
   global_var.SCREEN.blit(score, scoreRect)
   leader_board_text = font.render("Leaderboard", True, global_var.FONT_COLOR)
   x_lead, y_lead, w_lead, h_lead = leader_board_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3-10, global_var.SCREEN_HEIGHT // 2 + 150))
   global_var.SCREEN.blit(leader_board_text, (x_lead, y_lead))
   border_img = pygame.image.load(os.path.join("assets/interface", "border.png"))
   border_img = pygame.transform.scale(border_img, (350,50))
   global_var.SCREEN.blit(border_img, (x_lead-90, y_lead-11))



   hs_score_text = font.render(
       "Your High Score : " + str(global_var.high_score), True, global_var.FONT_COLOR
   )
   hs_score_rect = hs_score_text.get_rect()
   hs_score_rect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 100)
   global_var.SCREEN.blit(hs_score_text, hs_score_rect)

   return( x_lead, y_lead, w_lead, h_lead)   

## @brief Displays the start and restart page texts and graphics
# @param death_count an integer value indication the amount of times lost (had to restsart)
def menu(death_count):

   global_var.start_flag = False
   global_var.restart_flag = False
   global_var.game_track_flag = False
   global_var.instructions_flag = False
   global_var.leaderboard_flag = False
   run = True
   updated_score = False
   while run:
       current_time = datetime.datetime.now().hour
       if 7 < current_time < 19:
           global_var.FONT_COLOR = (0, 0, 0)
           global_var.SCREEN.fill((255, 255, 255))
          
       else:
           global_var.FONT_COLOR = (255, 255, 255)
           global_var.SCREEN.fill((128, 128, 128))
       font = pygame.font.Font("freesansbold.ttf", 30)

       if death_count == 0:
           global_var.start_flag = True
           text = font.render("Press any Key to Start", True, global_var.FONT_COLOR)
           if (len(global_var.username) == 0):
               global_var.username = "No_User_Entered"
              


         
           instructions_text = font.render("How to play", True, global_var.FONT_COLOR)
           x, y, w, h = instructions_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6-90))
      
           #global_var.SCREEN.blit(instructions_text, (global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6))
           mouse_pos = pygame.mouse.get_pos() #get mouse cursor position

           username_text = font.render("Change Username", True, global_var.FONT_COLOR)
           x_u, y_u, w_u, h_u = username_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3-50, global_var.SCREEN_HEIGHT // 1.6 + 30))
      
           game_settings_text = font.render("Game Settings", True, global_var.FONT_COLOR)
           x2, y2, w2, h2 = game_settings_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3-30, global_var.SCREEN_HEIGHT // 1.6-30))

           leaderboard_text = font.render("Leaderboard", True, global_var.FONT_COLOR)
           x_l, y_l, w_l, h_l = leaderboard_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3-50, global_var.SCREEN_HEIGHT // 1.6+90))
          
          
      
       elif death_count > 0:
           text = font.render("Press any Key to Restart", True, global_var.FONT_COLOR)
           if (not updated_score):
               update_score()
               updated_score = True
           x_lead, y_lead, w_lead, h_lead = restart()
           global_var.restart_flag = True

           # we should probably add this to restart? - Anjola
           # path to main menu
           menu_text = font.render("Main Menu", True, global_var.FONT_COLOR)
           x_m, y_m, w_m, h_m = menu_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3-10, global_var.SCREEN_HEIGHT // 2 + 210))
           global_var.SCREEN.blit(menu_text, (x_m, y_m))
           border_img = pygame.image.load(os.path.join("assets/interface", "border.png"))
           border_img = pygame.transform.scale(border_img, (350,50))
           global_var.SCREEN.blit(border_img, (x_m-90, y_m-11))

           #x_menu, y_menu, w_menu, h_menu
           x_menu, y_menu, w_menu, h_menu = menu_text.get_rect(topleft=(900,25))
           mouse_pos_menu = pygame.mouse.get_pos() #get mouse cursor position
  


       ## should we have a template for ur pages so that we just diplay that
       ## instead fo reqritng it each time?
       ## setting up the main screen with appropriate text
       textRect = text.get_rect()
       textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2-50)

      
       # print(x2, y2, w2, h2)
       global_var.SCREEN.blit(text, textRect)
       global_var.SCREEN.blit(images.RUNNING[0], (global_var.SCREEN_WIDTH // 2 - 30, global_var.SCREEN_HEIGHT // 2 - 200))


      
       # Adding instuctions button on menu
       if global_var.start_flag == True:

           border_img = pygame.image.load(os.path.join("assets/interface", "border.png"))
           border_img = pygame.transform.scale(border_img, (350,50))

           big_border_img = pygame.image.load(os.path.join("assets/interface", "big_border.png"))
           big_border_img = pygame.transform.scale(big_border_img, (600,550))
           global_var.SCREEN.blit(big_border_img, (250, 20))




           global_var.SCREEN.blit(instructions_text, (global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6-90))
           global_var.SCREEN.blit(border_img, (x-100, y-11))


           #x_settings = int(global_var.SCREEN_WIDTH * 0.78)
           #y_settings = int(global_var.SCREEN_HEIGHT * 0.05)
           #global_var.SCREEN.blit(game_settings_text, (x_settings, y_settings))
           #global_var.SCREEN.blit(settings_border_img, (x_settings-50, y_settings - 11))
           global_var.SCREEN.blit(game_settings_text, (global_var.SCREEN_WIDTH // 2.3-30, global_var.SCREEN_HEIGHT // 1.6 - 30 ))
           global_var.SCREEN.blit(border_img, (x2-70, y2-11))

           global_var.SCREEN.blit(username_text, (global_var.SCREEN_WIDTH // 2.3 - 50, global_var.SCREEN_HEIGHT // 1.6 + 30))
           global_var.SCREEN.blit(border_img, (x_u - 50, y_u-11))

           global_var.SCREEN.blit(leaderboard_text, (global_var.SCREEN_WIDTH // 2.3 - 15, global_var.SCREEN_HEIGHT // 1.6 + 90))
           global_var.SCREEN.blit(border_img, (x_l - 50, y_l-11))


           #pygame.Rect(x_settings, y_settings, width, height) #- code below is for testing how to draw rect
          # pygame.draw.rect(SCREEN, (0,0,0), pygame.Rect(x_settings, y_settings, w2, h2), 2)
          # pygame.draw.rect(SCREEN, (0,0,0), (x2, x2 + w2, w2, h2))
           mouse_pos = pygame.mouse.get_pos() #get mouse cursor position


       pygame.display.update()
       mouse_pos = pygame.mouse.get_pos() #get mouse cursor position
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
               pygame.display.quit()
               pygame.quit()
               exit()
           if event.type == pygame.KEYDOWN:
               global_var.game_track_flag = True
               main()

           # Add mouse click on main menu text
           if death_count > 0 and event.type == pygame.MOUSEBUTTONDOWN  and mouse_pos_menu[0] in range(x_m, x_m+w_m) and mouse_pos_menu[1] in range(y_m, y_m+h_m):
               menu(0)
  
           #Check if instructions was pressed
           if global_var.test_instructions or global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x-100, x+250) and mouse_pos[1] in range(y-10, y-10+50):
               instructions()
               while not global_var.game_track_flag:
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                           print('pressed b')

                           # test_exit_key
                           if global_var.test_instructions:
                               global_var.start_flag = True
                               return

                           menu(0)

                          
          
            #Check if instructions was pressed
           if global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_l, x_l+w_l) and mouse_pos[1] in range(y_l, y_l+h_l):
               display_leaderboad()
               global_var.leaderboard_flag = True
               global_var.restart_flag = False
               while not global_var.game_track_flag:
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                           if global_var.test_leaderboard:
                               return
                           #b to go back
                           print("keydown?")
                           menu(death_count)
                       #Check if instructions was pressed

           # Check if settings was pressed.
           if (global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x2-70, x2 + 350-70) and \
                   mouse_pos[1] in range(y2, y2 -10 + 50)) or global_var.test_settings:
               settings()
               while not global_var.game_track_flag:
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()

                       # press n and turn off the audio settings
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                           global_var.audio = False
                           if global_var.test_settings:
                               return
                           audio_off_sound.play()

                       # press a and turn on the audio settings
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                           global_var.audio = True
                           if global_var.test_settings:
                               return
                           audio_on_sound.play()

                       # press specific numbers and change the themes
                       if (event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3)):
                           if(event.key == pygame.K_1):
                               dinosaur_sound.play()
                               global_var.theme = 'default'

                               if global_var.test_settings:
                                   # print("testing student theme")
                                   return

                               images.RUNNING = images.RUNNING_THEME1
                               images.DUCKING = images.DUCKING_THEME1
                               images.JUMPING = images.JUMPING_THEME1
                               images.OBSTACLE_ONE = images.OBSTACLE_ONE_THEME1
                               images.OBSTACLE_TWO = images.OBSTACLE_TWO_THEME1
                               images.OBSTACLE_FLYING = images.OBSTACLE_FLYING_THEME1
                           elif(event.key == pygame.K_2):
                               student_sound.play()
                               global_var.theme = 'student'

                               if global_var.test_settings:
                                   # print("testing student theme")
                                   return

                               images.RUNNING = images.RUNNING_THEME2
                               images.DUCKING = images.DUCKING_THEME2
                               images.JUMPING = images.JUMPING_THEME2
                               images.OBSTACLE_ONE = images.OBSTACLE_ONE_THEME2
                               images.OBSTACLE_TWO = images.OBSTACLE_TWO_THEME2
                               images.OBSTACLE_FLYING = images.OBSTACLE_FLYING_THEME2
                           elif(event.key == pygame.K_3):
                               corona_sound.play()
                               global_var.theme = 'corona'

                               if global_var.test_settings:
                                   # print("testing corona theme")
                                   return

                               images.RUNNING = images.RUNNING_THEME3
                               images.DUCKING = images.DUCKING_THEME3
                               images.JUMPING = images.JUMPING_THEME3
                               images.OBSTACLE_ONE = images.OBSTACLE_ONE_THEME3
                               images.OBSTACLE_TWO = images.OBSTACLE_TWO_THEME3
                               images.OBSTACLE_FLYING = images.OBSTACLE_FLYING_THEME3

                           print(global_var.theme)
                       # press b and get returned to the main page
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                           menu(0)


                  
          
           #Check if instructions was pressed
           if global_var.restart_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_lead, x_lead+w_lead) and mouse_pos[1] in range(y_lead, y_lead+h_lead):
               # print("leaderboard")
               display_leaderboad()
               if global_var.test_leaderboard:
                   return
               while not global_var.game_track_flag:
                   for event in pygame.event.get():
                       if event.type == pygame.QUIT:
                           pygame.quit()
                           quit()
                       if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                          
                           #b to go back
                           print("keydown?")
                           menu(death_count)
                       #Check if instructions was pressed

           if global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_u-50, x_u+300) and mouse_pos[1] in range(y_u, y_u - 10 + 50):
               print("username here")
               global_var.username = get_username()
               print(global_var.username)
               global_var.restart_flag = False

                    
      
t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()

