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
import time
from username import get_username 

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


# Global Constants
# global_var.SCREEN_HEIGHT = 600
# global_var.global_var.SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((global_var.SCREEN_WIDTH, global_var.SCREEN_HEIGHT))

# setting up the window - title and setting the game icon (top left corner)
pygame.display.set_caption("Chrome Dino Runner")

Ico = pygame.image.load("assets/DinoWallpaper.png")
pygame.display.set_icon(Ico)

# variable used to track if you are on the main page or not?
global_var.game_track_flag = False

## @brief Displays the instructions page texts and graphics
def instructions():
    
    # Adding background
    SCREEN.fill((255,255,255))

    track = pygame.image.load(os.path.join("assets/Other", "Track.png"))
    SCREEN.blit(track, (0, 400))
    
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

    if not global_var.game_track_flag:
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
        SCREEN.blit(main_text, (320, 450))

    pygame.display.update()

## @brief Displays the settings page texts and graphics
def settings():

    # Adding background
    SCREEN.fill((255,255,255))
    image_width = images.BG.get_width()
    SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))

    # Setting up title
    font = pygame.font.Font("freesansbold.ttf", 30)
    title = font.render("SETTINGS", True, "black")
    titleRect = title.get_rect()
    titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
    SCREEN.blit(title, titleRect)

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
    SCREEN.blit(default_text, (250, 95))
    # rendering no audio text to screen
    SCREEN.blit(press_text, (373, 140))
    SCREEN.blit(n_img, (433, 120))
    SCREEN.blit(no_audio_text, (493, 140))
    # insert audio image  here
    SCREEN.blit(no_audio_img, (625, 120))

    # rendering audio text to screen
    SCREEN.blit(press_text, (373, 220))
    SCREEN.blit(a_img, (438, 200))
    SCREEN.blit(audio_text, (493, 220))
    SCREEN.blit(audio_img, (625, 200))

    # themed options - option 1 (default)
    SCREEN.blit(press_text, (140, 290))
    SCREEN.blit(one_img, (205, 270))
    SCREEN.blit(default_theme_text, (260, 290))
    SCREEN.blit(dino_img, (475, 265))

    # themed options - option 2 (student version)
    SCREEN.blit(press_text, (140, 355))
    SCREEN.blit(two_img, (205, 330))
    SCREEN.blit(student_theme_text, (260, 355))
    SCREEN.blit(student_img, (475, 330))

    # themed options - option 3 (corona version)
    SCREEN.blit(press_text, (555, 290))
    SCREEN.blit(three_img, (620, 270))
    SCREEN.blit(corona_theme_text, (675, 290))
    SCREEN.blit(corona_img, (890, 265))

    # themed options - new options coming soon
    SCREEN.blit(new_options_text, (555,355))

    if not global_var.game_track_flag:
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
        SCREEN.blit(main_text, (320, 450))

    pygame.display.update()

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
        SCREEN.blit(text, textRect)

    ## @brief Updates the background of the game according to game speed 
    def background():
        # global_var.x_pos_bg, global_var.y_pos_bg
        image_width = images.BG.get_width()
        SCREEN.blit(images.BG, (global_var.x_pos_bg, global_var.y_pos_bg))
        SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
        if global_var.x_pos_bg <= -image_width:
            SCREEN.blit(images.BG, (image_width + global_var.x_pos_bg, global_var.y_pos_bg))
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

            if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                jump_sound.play()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                duck_sound.play()
           
        
        #if global_var.points % 1000 == 0 and global_var.points != 0:
        #    print("REACHED")
        #    milestone_sound.play()

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
                global_var.obstacles.append(SmallObstacle(images.OBSTACLE_ONE))
            elif random.randint(0, 2) == 1:
                global_var.obstacles.append(LargeObstacle(images.OBSTACLE_TWO))
            elif random.randint(0, 2) == 2:
                global_var.obstacles.append(Bird(images.OBSTACLE_FLYING))

        for obstacle in global_var.obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                death_sound.play()
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        background()

        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

## @brief Adds the user's username and score to score.txt after each death 
def update_score():
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
    SCREEN.blit(score, scoreRect)
    leader_board_text = font.render("Leader Board", True, global_var.FONT_COLOR)
    leader_board_text_rect = leader_board_text.get_rect()
    leader_board_text_rect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 150)
    SCREEN.blit(leader_board_text, leader_board_text_rect)
    x_lead, y_lead, w_lead, h_lead = leader_board_text.get_rect(center=(global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 150))
    hs_score_text = font.render(
        "Your High Score : " + str(global_var.high_score), True, global_var.FONT_COLOR
    )
    hs_score_rect = hs_score_text.get_rect()
    hs_score_rect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + 100)
    SCREEN.blit(hs_score_text, hs_score_rect)

    return( x_lead, y_lead, w_lead, h_lead)    

## @brief Displays the restart page texts and graphics 
#  @return A list containing the formatted leader text
def get_leaders():
    font = pygame.font.Font("freesansbold.ttf", 25) # make font a global var
    score_dict = {}
    ## score: Players []
    leaders_text = []
    with open("score.txt", "r") as f:
            score = (
                f.read()
            ) 
    score_list = score.split("\n")
    # ["Anjola 3", "Chel 200"]
    curr_user_scores = [] # the current users score
    for score in score_list:
        temp = score.split()
        # temp = [Anjola, 3]
        if temp[1] in score_dict:
            score_dict[int(temp[1])].append(temp[0])
            '''
            {100 : [Anjola, Sheridan]}
            '''
        else:
            score_dict[int(temp[1])] = [temp[0]]
            ## if it's a score we've never seen, we'll make that a key
        if temp[0] == global_var.username:
            curr_user_scores.append(int(temp[1]))

    ## sort scores in descending order
    sorted_scores = sorted(score_dict, reverse=True) 
    ## a list of sorted score from score_dict
    sorted_top_scores = []  # 2-D list of top scores
    count = 0 ## ensure that only five score are added to sorted top scoresS
    for score in sorted_scores:
        if count < 5:
            ## if more than one person has the top score
            if len(score_dict[score]) > 1:
                for person in score_dict[score]:
                    if count < 5:
                        sorted_top_scores.append([person, score])
                        count+= 1
            else:
                person = score_dict[score][0]
                sorted_top_scores.append([person, score])
                count+= 1

    ## first index is the highest score
    for pair in sorted_top_scores:
        leaders_text.append(font.render(f"{pair[0]}: {pair[1]}", True, global_var.FONT_COLOR))
        ## formating the leader text
    
    ## high score displayed is curent user's high score
    if len(curr_user_scores) > 0:
        global_var.high_score =  max(curr_user_scores)
    else:
        global_var.high_score = 0
    
    return (leaders_text)

## @brief Displays the leaderboard page texts and graphics
def display_leaderboad():  
    current_time = datetime.datetime.now().hour
    if 7 < current_time < 19:     
        SCREEN.fill((255, 255, 255)) 
    else:
        SCREEN.fill((128, 128, 128))

    font = pygame.font.Font("freesansbold.ttf", 30)    
    title = font.render("LeaderBoard", True, global_var.FONT_COLOR)
    titleRect = title.get_rect()
    titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
    SCREEN.blit(title, titleRect)
    leaders= get_leaders()
    leader_rect = []
    c = -20
    for i in range(len(leaders)):
        leader_rect.append(leaders[i].get_rect())
        leader_rect[i].center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2 + c)
        SCREEN.blit(leaders[i], leader_rect[i])
        c += 30

    main_text = font.render("Press 'b' to go back to restart menu", True,  global_var.FONT_COLOR)
    SCREEN.blit(main_text, (320, 450))
    

    pygame.display.update()


## @brief Displays the start and restart page texts and graphics
# @param death_count an integer value indication the amount of times lost (had to restsart)
def menu(death_count):
    global_var.start_flag = False 
    global_var.restart_flag = False
    global_var.game_track_flag = False
    run = True
    updated_score = False
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
            global_var.start_flag = True
            text = font.render("Press any Key to Start", True, global_var.FONT_COLOR)
            if (len(global_var.username) == 0):
                # global_var.username = get_username()
                # print(global_var.username)
                global_var.username = "No_User_Entered"
                # global_var.username = input("Enter username:")
                
            instructions_text = font.render("How to play", True, global_var.FONT_COLOR)
            x, y, w, h = instructions_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6))
            SCREEN.blit(instructions_text, (global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6))
            mouse_pos = pygame.mouse.get_pos() #get mouse cursor position

            username_text = font.render("Click to enter your username", True, global_var.FONT_COLOR)
            x_u, y_u, w_u, h_u = username_text.get_rect(topleft=(global_var.SCREEN_WIDTH // 3, global_var.SCREEN_HEIGHT // 2 + 150))
            SCREEN.blit(username_text, (global_var.SCREEN_WIDTH // 3, global_var.SCREEN_HEIGHT // 2 + 150))
           


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
            SCREEN.blit(menu_text, (900, 25))
            #x_menu, y_menu, w_menu, h_menu 
            x_menu, y_menu, w_menu, h_menu = menu_text.get_rect(topleft=(900,25))
            mouse_pos_menu = pygame.mouse.get_pos() #get mouse cursor position
    

        ## should we have a template for ur pages so that we just diplay that 
        ##instead fo reqritng it each time?

        # setting up the main screen with appropriate text
        textRect = text.get_rect()
        textRect.center = (global_var.SCREEN_WIDTH // 2, global_var.SCREEN_HEIGHT // 2)

        game_settings_text = font.render("Game Settings", True, global_var.FONT_COLOR)
        x2, y2, w2, h2 = game_settings_text.get_rect(center=(global_var.SCREEN_WIDTH // 2 ,global_var.SCREEN_HEIGHT // 1.5))
        # print(x2, y2, w2, h2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(images.RUNNING[0], (global_var.SCREEN_WIDTH // 2 - 20, global_var.SCREEN_HEIGHT // 2 - 140))

        # Adding instuctions button on menu
        if global_var.start_flag == True:
            SCREEN.blit(instructions_text, (global_var.SCREEN_WIDTH // 2.3, global_var.SCREEN_HEIGHT // 1.6))

            x_settings = int(global_var.SCREEN_WIDTH * 0.78)
            y_settings = int(global_var.SCREEN_HEIGHT * 0.05)
            SCREEN.blit(game_settings_text, (x_settings, y_settings))

           # pygame.Rect(x_settings, y_settings, width, height) #- code below is for testing how to draw rect
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
                print("keydown?")
                global_var.game_track_flag = True
                main()

            # Add mouse click on main menu text
            if death_count > 0 and event.type == pygame.MOUSEBUTTONDOWN  and mouse_pos_menu[0] in range(x_menu, x_menu+w_menu) and mouse_pos_menu[1] in range(y_menu, y_menu+h_menu):
                menu(0)
    
            #Check if instructions was pressed
            if global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x, x+w) and mouse_pos[1] in range(y, y+h):
                instructions()
                while not global_var.game_track_flag:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            print('pressed e')
                            menu(0)
            

            # Check if settings was pressed.
            if global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_settings, x_settings + w2) and \
                    mouse_pos[1] in range(y_settings, y_settings + h2):
                settings()
                while not global_var.game_track_flag:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()

                        # press n and turn off the audio settings
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                            global_var.audio = False

                        # press a and turn on the audio settings
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                            global_var.audio = True

                        # press specific numbers and change the themes
                        if event.type == pygame.KEYDOWN and (event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3):
                            if(event.key == pygame.K_1):
                                global_var.theme = 'default'
                                dinosaur_sound.play()
                            elif(event.key == pygame.K_2):
                                global_var.theme = 'student'
                                student_sound.play()
                            elif(event.key == pygame.K_3):
                                corona_sound.play()
                                global_var.theme = 'corona'
                                images.RUNNING = images.RUNNING_THEME3
                                images.DUCKING = images.DUCKING_THEME3
                                images.JUMPING = images.JUMPING_THEME3
                                images.OBSTACLE_ONE = images.OBSTACLE_ONE_THEME3
                                images.OBSTACLE_TWO = images.OBSTACLE_TWO_THEME3
                                images.OBSTACLE_FLYING = images.OBSTACLE_FLYING_THEME3

                            print(global_var.theme)
                        # press e and get returned to the main page
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                            menu(0)


                    
            
            #Check if instructions was pressed
            if global_var.restart_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_lead, x_lead+w_lead) and mouse_pos[1] in range(y_lead, y_lead+h_lead):
                print("leaderboard")
                display_leaderboad()
                global_var.restart_flag = False
                while not global_var.game_track_flag:
                    for event in pygame.event.get():
                        print("EVENT")
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                            #b to go back
                            print("keydown?")
                            menu(death_count)
                        #Check if instructions was pressed

            if global_var.start_flag == True and event.type == pygame.MOUSEBUTTONDOWN and mouse_pos[0] in range(x_u, x_u+w_u) and mouse_pos[1] in range(y_u, y_u+h_u):
                print("usernameee here")
                global_var.username = get_username()
                print(global_var.username)
                global_var.restart_flag = False

                      
        
t1 = threading.Thread(target=menu(death_count=0), daemon=True)
t1.start()
