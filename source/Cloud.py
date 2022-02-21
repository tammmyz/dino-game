import pygame
import random
import global_var
import images

class Cloud:
    def __init__(self):
        self.x = global_var.SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = images.CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= global_var.game_speed
        if self.x < -self.width:
            self.x = global_var.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))