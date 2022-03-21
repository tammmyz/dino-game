import pygame
from global_var import SCREEN
import global_var
import os
from cloud import Cloud
from large_obstacle import LargeObstacle
from small_obstacle import SmallObstacle
from bird import Bird
from character import Character
from obstacle import Obstacle
import global_var
import images
## @brief Displays the instructions page texts and graphics
def instructions():
    
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
    global_var.SCREEN.blit(press_text, (373, 140))
    global_var.SCREEN.blit(up_img, (433, 120))
    global_var.SCREEN.blit(or_text, (493, 140))
    global_var.SCREEN.blit(w_img, (518, 122))
    global_var.SCREEN.blit(jump_text, (573, 140))
    global_var.SCREEN.blit(cactus_img, (668, 120))

    global_var.SCREEN.blit(press_text, (373, 220))
    global_var.SCREEN.blit(down_img, (438, 200))
    global_var.SCREEN.blit(or_text, (493, 220))
    global_var.SCREEN.blit(s_img, (520, 200))
    global_var.SCREEN.blit(duck_text, (573, 220))
    global_var.SCREEN.blit(bird_img, (668, 200))

    global_var.SCREEN.blit(press_text, (373, 290))
    global_var.SCREEN.blit(p_img, (440, 275))
    global_var.SCREEN.blit(pause_text, (493, 290))

    global_var.SCREEN.blit(press_text, (373, 355))
    global_var.SCREEN.blit(u_img, (440, 340))
    global_var.SCREEN.blit(unpause_text, (493, 355))

    if not global_var.game_track_flag:
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
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
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
        global_var.SCREEN.blit(main_text, (320, 450))

    pygame.display.update()
import pygame
from global_var import SCREEN
import global_var
import os
from cloud import Cloud
from large_obstacle import LargeObstacle
from small_obstacle import SmallObstacle
from bird import Bird
from character import Character
from obstacle import Obstacle
import global_var
import images
## @brief Displays the instructions page texts and graphics
def instructions():
    
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
    global_var.SCREEN.blit(press_text, (373, 140))
    global_var.SCREEN.blit(up_img, (433, 120))
    global_var.SCREEN.blit(or_text, (493, 140))
    global_var.SCREEN.blit(w_img, (518, 122))
    global_var.SCREEN.blit(jump_text, (573, 140))
    global_var.SCREEN.blit(cactus_img, (668, 120))

    global_var.SCREEN.blit(press_text, (373, 220))
    global_var.SCREEN.blit(down_img, (438, 200))
    global_var.SCREEN.blit(or_text, (493, 220))
    global_var.SCREEN.blit(s_img, (520, 200))
    global_var.SCREEN.blit(duck_text, (573, 220))
    global_var.SCREEN.blit(bird_img, (668, 200))

    global_var.SCREEN.blit(press_text, (373, 290))
    global_var.SCREEN.blit(p_img, (440, 275))
    global_var.SCREEN.blit(pause_text, (493, 290))

    global_var.SCREEN.blit(press_text, (373, 355))
    global_var.SCREEN.blit(u_img, (440, 340))
    global_var.SCREEN.blit(unpause_text, (493, 355))

    if not global_var.game_track_flag:
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
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
        main_text = font.render("Press 'e' to go back to main menu", True, "black")
        global_var.SCREEN.blit(main_text, (320, 450))

    pygame.display.update()
