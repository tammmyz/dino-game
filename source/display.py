## @file display.py 
# @author Anjola Adewale, Sheridan Fong, Chelsea Maramot  
# @brief Contains the display interface for the game
# @date 04/12/2022

# importing standard libraries
import pygame
import global_var
import os
import datetime

# importing local file/applications
from cloud import Cloud
from large_obstacle import LargeObstacle
from small_obstacle import SmallObstacle
from bird import Bird
from character import Character
from obstacle import Obstacle
import global_var
from global_var import SCREEN
import images
from leader import * 

## @brief Displays the instructions page texts and graphics
def instructions():
   global_var.instructions_flag = True
   # Adding background
   global_var.SCREEN.fill((255,255,255))

   track = pygame.image.load(os.path.join("assets/Other", "Track.png"))
   global_var.SCREEN.blit(track, (0, 400))
  
   # Setting up title
   font = pygame.font.Font("freesansbold.ttf", 30)
   title = font.render("INSTRUCTIONS", True, "black")
   titleRect = title.get_rect()
   titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
   global_var.SCREEN.blit(title, titleRect)

   # Instruction Body
   body_font = pygame.font.Font("freesansbold.ttf", 20)
   press_text = body_font.render("Press", True, "black")
   jump_text = body_font.render("to JUMP", True, "black")
   duck_text = body_font.render("to DUCK", True, "black")
   or_text = body_font.render("or", True, "black")
   pause_text = body_font.render("to PAUSE the game", True, "black")
   unpause_text = body_font.render("to UNPAUSE the game", True, "black")

   # Display instuction body
   global_var.SCREEN.blit(press_text, (373, 140))
   global_var.SCREEN.blit(images.up_img, (433, 120))
   global_var.SCREEN.blit(or_text, (493, 140))
   global_var.SCREEN.blit(images.w_img, (518, 122))
   global_var.SCREEN.blit(jump_text, (573, 140))
   global_var.SCREEN.blit(images.cactus_img, (668, 120))

   global_var.SCREEN.blit(press_text, (373, 220))
   global_var.SCREEN.blit(images.down_img, (438, 200))
   global_var.SCREEN.blit(or_text, (493, 220))
   global_var.SCREEN.blit(images.s_img, (520, 200))
   global_var.SCREEN.blit(duck_text, (573, 220))
   global_var.SCREEN.blit(images.bird_img, (668, 200))

   global_var.SCREEN.blit(press_text, (373, 290))
   global_var.SCREEN.blit(images.p_img, (440, 275))
   global_var.SCREEN.blit(pause_text, (493, 290))

   global_var.SCREEN.blit(press_text, (373, 355))
   global_var.SCREEN.blit(images.u_img, (440, 340))
   global_var.SCREEN.blit(unpause_text, (493, 355))

   if not global_var.game_track_flag:
       main_text = font.render("Press 'b' to go back to main menu", True, "black")
       global_var.SCREEN.blit(main_text, (320, 450))

   pygame.display.update()

## @brief Displays the settings page texts and graphics
def settings():

   # Adding background
   global_var.SCREEN.fill((255,255,255))
   image_width = images.BG.get_width()
   global_var.SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))

   # Setting up title
   font = pygame.font.Font("freesansbold.ttf", 30)
   title = font.render("SETTINGS", True, "black")
   titleRect = title.get_rect()
   titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
   global_var.SCREEN.blit(title, titleRect)

   # importing images --> transfer to img.py
   a_img = pygame.image.load(os.path.join("assets/Keys", "a.png"))
   a_img = pygame.transform.scale(a_img, (50,50))

   n_img = pygame.image.load(os.path.join("assets/Keys", "n.png"))
   n_img = pygame.transform.scale(n_img, (50,50))


   one_img = pygame.image.load(os.path.join("assets/Keys", "1.png"))
   one_img = pygame.transform.scale(one_img, (50,50))

   two_img = pygame.image.load(os.path.join("assets/Keys", "2.png"))
   two_img = pygame.transform.scale(two_img, (50,50))

   three_img = pygame.image.load(os.path.join("assets/Keys", "3.png"))
   three_img = pygame.transform.scale(three_img, (50,50))

   audio_img = pygame.image.load(os.path.join("assets/Other", "audio.png"))
   audio_img = pygame.transform.scale(audio_img, (50,50))

   no_audio_img = pygame.image.load(os.path.join("assets/Other", "no_audio.png"))
   no_audio_img = pygame.transform.scale(no_audio_img, (50,50))

   dino_img = pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png"))
   dino_img = pygame.transform.scale(dino_img, (50,50))

   student_img = pygame.image.load(os.path.join("assets/Student", "student.png"))
   student_img = pygame.transform.scale(student_img, (50,50))

   corona_img = pygame.image.load(os.path.join("assets/Corona", "corona.png"))
   corona_img = pygame.transform.scale(corona_img, (50,50))

   # Instruction Body
   body_font = pygame.font.Font("freesansbold.ttf", 20)
   default_text = body_font.render("The default settings have the audio on and the original theme", True, "black")
   press_text = body_font.render("Press", True, "black")
   no_audio_text = body_font.render("for no audio", True, "black")
   audio_text = body_font.render("for audio", True, "black")
   default_theme_text = body_font.render("for the default theme", True, "black")
   student_theme_text = body_font.render("for the student theme", True, "black")
   corona_theme_text = body_font.render("for the corona theme", True, "black")
   new_options_text = body_font.render("New themes coming soon...", True, "black")

   # Display instruction body (x , y)
   global_var.SCREEN.blit(default_text, (250, 95))
   # rendering no audio text to global_var.SCREEN
   global_var.SCREEN.blit(press_text, (373, 140))
   global_var.SCREEN.blit(n_img, (433, 120))
   global_var.SCREEN.blit(no_audio_text, (493, 140))
   # insert audio image  here
   global_var.SCREEN.blit(no_audio_img, (625, 120))

   # rendering audio text to global_var.SCREEN
   global_var.SCREEN.blit(press_text, (373, 220))
   global_var.SCREEN.blit(a_img, (438, 200))
   global_var.SCREEN.blit(audio_text, (493, 220))
   global_var.SCREEN.blit(audio_img, (625, 200))

   # themed options - option 1 (default)
   global_var.SCREEN.blit(press_text, (140, 290))
   global_var.SCREEN.blit(one_img, (205, 270))
   global_var.SCREEN.blit(default_theme_text, (260, 290))
   global_var.SCREEN.blit(dino_img, (475, 265))

   # themed options - option 2 (student version)
   global_var.SCREEN.blit(press_text, (140, 355))
   global_var.SCREEN.blit(two_img, (205, 330))
   global_var.SCREEN.blit(student_theme_text, (260, 355))
   global_var.SCREEN.blit(student_img, (475, 330))

   # themed options - option 3 (corona version)
   global_var.SCREEN.blit(press_text, (555, 290))
   global_var.SCREEN.blit(three_img, (620, 270))
   global_var.SCREEN.blit(corona_theme_text, (675, 290))
   global_var.SCREEN.blit(corona_img, (890, 265))

   # themed options - new options coming soon
   global_var.SCREEN.blit(new_options_text, (555,355))

   if not global_var.game_track_flag:
       main_text = font.render("Press 'b' to go back to main menu", True, "black")
       global_var.SCREEN.blit(main_text, (320, 450))

   pygame.display.update()

## @brief Displays the leaderboard page texts and graphics
def display_leaderboad(): 
   current_time = datetime.datetime.now().hour
   if 7 < current_time < 19:    
       global_var.SCREEN.fill((255, 255, 255))
   else:
       global_var.SCREEN.fill((128, 128, 128))

   font = pygame.font.Font("freesansbold.ttf", 30)   
   title = font.render("Leaderboard", True, global_var.FONT_COLOR)
   titleRect = title.get_rect()
   titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
   global_var.SCREEN.blit(title, titleRect)
   leaders= get_leaders()
   leader_rect = []
   c = -20

   global_var.SCREEN.blit(images.RUNNING[0], (global_var.SCREEN_WIDTH // 2 - 20, global_var.SCREEN_HEIGHT // 2 - 140))
   for i in range(len(leaders)):
       leader_rect.append(leaders[i].get_rect())
       leader_rect[i].center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + c)
       global_var.SCREEN.blit(leaders[i], leader_rect[i])
       c += 30

   main_text = font.render("Press 'b' to go back", True,  global_var.FONT_COLOR)
   global_var.SCREEN.blit(main_text, (420, 450))
   global_var.leaderboard_flag = True
   global_var.restart_flag = False

   pygame.display.update()