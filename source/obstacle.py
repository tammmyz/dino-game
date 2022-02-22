import pygame
import random
import global_var
import images

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = global_var.SCREEN_WIDTH

    def update(self):
        self.rect.x -= global_var.game_speed
        if self.rect.x < -self.rect.width:
            global_var.obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)