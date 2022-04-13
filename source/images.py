## @file images.py
#  @author Anjola Adewale, Chelsea Maramot, Sheridan Fong
#  @brief Contains the images for chromedino.py
#  @date 03/18/2022

import pygame
import os
import global_var

# putting in the ground graphic
BG = pygame.image.load(os.path.join("assets/Other", "Track.png"))

if global_var.theme == "default":
    print("default here")
    # RUNNING_THEME = [
    RUNNING = [
        pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
        pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
    ]
    JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
    DUCKING = [
        pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
        pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
    ]

    OBSTACLE_ONE = [
        pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
        pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
        pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
    ]
    OBSTACLE_TWO = [
        pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
        pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
        pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
    ]

    OBSTACLE_FLYING = [
        pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
    ]

    CLOUD = pygame.image.load(os.path.join("assets/Other", "Cloud.png"))

# ------------- Theme 1: Default Dino ----------------------
RUNNING_THEME1 = [
    pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
]
JUMPING_THEME1 = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
DUCKING_THEME1 = [
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
    pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
]

OBSTACLE_ONE_THEME1 = [
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png")),
]
OBSTACLE_TWO_THEME1 = [
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus2.png")),
    pygame.image.load(os.path.join("assets/Cactus", "LargeCactus3.png")),
]

OBSTACLE_FLYING_THEME1 = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

# ------------------ Theme 2: Student
RUNNING_THEME2 = [
    pygame.image.load(os.path.join("assets/Student", "student1.png")),
    pygame.image.load(os.path.join("assets/Student", "student2.png")),
]
JUMPING_THEME2 = pygame.image.load(os.path.join("assets/Student", "student_jump.png"))
DUCKING_THEME2 = [
    pygame.image.load(os.path.join("assets/Student", "duck1.png")),
    pygame.image.load(os.path.join("assets/Student", "duck1.png")),
]

OBSTACLE_ONE_THEME2 = [
    pygame.image.load(os.path.join("assets/Student_Obstacles", "failed_test.png")),
    pygame.image.load(os.path.join("assets/Student_Obstacles", "wetsign.png")),
    pygame.image.load(os.path.join("assets/Student_Obstacles", "failed_test.png")),
]
OBSTACLE_TWO_THEME2 = [
    pygame.image.load(os.path.join("assets/Student_Obstacles", "desk.png")),
    pygame.image.load(os.path.join("assets/Student_Obstacles", "desk.png")),
    pygame.image.load(os.path.join("assets/Student_Obstacles", "desk.png")),
]

OBSTACLE_FLYING_THEME2 = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

# -------- THEME 3 : CORONA ----------------------------------------------------------

RUNNING_THEME3 = [
    pygame.image.load(os.path.join("assets/Corona", "corona.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona2.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona3.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona4.png"))
]
JUMPING_THEME3 = pygame.image.load(os.path.join("assets/Corona", "corona.png"))

DUCKING_THEME3 = [
    pygame.image.load(os.path.join("assets/Corona", "corona_duck1.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona_duck2.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona_duck3.png")),
    pygame.image.load(os.path.join("assets/Corona", "corona_duck4.png")),
]

OBSTACLE_ONE_THEME3 = [
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "vaccine1.png")),
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "first_aid.png")),
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "magnifying.png")),
]
OBSTACLE_TWO_THEME3 = [
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "bandaid.png")),
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "bandaid.png")),
    pygame.image.load(os.path.join("assets/Corona_Obstacles", "bandaid.png")),
]

OBSTACLE_FLYING_THEME3 = [
    pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
    pygame.image.load(os.path.join("assets/Bird", "Bird2.png")),
]

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
