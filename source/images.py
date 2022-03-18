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
    RUNNING_THEME = [
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

#
# # DEFAULT - setting up the default lists
# RUNNING = [
#     pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
#     pygame.image.load(os.path.join("assets/Dino", "DinoRun2.png")),
# ]
# JUMPING = pygame.image.load(os.path.join("assets/Dino", "DinoJump.png"))
# DUCKING = [
#     pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png")),
#     pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png")),
# ]
#
# SMALL_CACTUS = [
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
