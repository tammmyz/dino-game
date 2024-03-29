## @file username.py 
# @author Anjola Adewale, Sheridan Fong, Chelsea Maramot  
# @brief Contains the algorithm for getting username
# @date 04/12/2022

# importing libraries
import pygame
import sys
import global_var
import images

# pygame.init() will initialize all
pygame.init()
font3 = pygame.font.Font("freesansbold.ttf", 22) 
invalid_input_text = font3.render(" ", True, "black") 
bad_word = ['FCUK', 'BITCH', 'SHIT', 'STUPID']
user_text = ''

## @brief Gets the username and displays the username
def get_username():
    global invalid_input_text, font3, user_text
    clock = pygame.time.Clock()

    # it will display on screen
    screen = SCREEN = pygame.display.set_mode((global_var.SCREEN_WIDTH, global_var.SCREEN_HEIGHT))

    # basic font for user typed
    base_font = pygame.font.Font(None, 32)

    user_text = ''

    # create rectangle
    input_rect = pygame.Rect(500, 250, 400, 45)

    color_active = pygame.Color('lightskyblue3')

    color_passive = pygame.Color('lightgrey')
    color = color_passive

    active = False

    while True:
        for event in pygame.event.get():

       
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_BACKSPACE:

                    user_text = user_text[:-1]
          
                elif event.key == pygame.K_RETURN:

                    if (user_text.upper() in bad_word):
                        invalid_input_text = font3.render("This is a bad word, please enter a new username", True, "red") 
                        user_text = ''
                    elif (" " in user_text):
                        invalid_input_text = font3.render("Username cannot contain a space,  please enter a new username", True, "red") 
                        user_text = ''
                    elif (len(user_text) > 15):
                        invalid_input_text = font3.render("Username too long,  please enter a new username", True, "red") 
                        user_text = ''
                    elif (len(user_text) < 2):
                        invalid_input_text = font3.render("Username too short,  please enter a new username", True, "red") 
                        user_text = ''
                    else:
                        return(user_text)
            
                else:
                    user_text += event.unicode
        
        
        screen.fill((255, 255, 255))

        if active:
            color = color_active
        else:
            color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))
        
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        font = pygame.font.Font("freesansbold.ttf", 20)   
        font2 = pygame.font.Font("freesansbold.ttf", 32)  
        title = font2.render("Please select the grey box to enter your username", True, "black")
        
        titleRect = title.get_rect()
        titleRect.center = (global_var.SCREEN_WIDTH // 2, 70)
        screen.blit(title, titleRect)

        main_text = font.render("Press Enter(Return) when you're done", True, "black")
        screen.blit(main_text, (470, 320))

        screen.blit(invalid_input_text, (400, 420))

        temp = pygame.transform.scale(images.RUNNING[0], (200,200))
        global_var.SCREEN.blit(temp, (200, 200))
        input_rect.w = max(300, text_surface.get_width()+10)
        
        pygame.display.flip()
        
        clock.tick(60)