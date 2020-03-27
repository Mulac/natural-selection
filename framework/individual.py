import pygame
import numpy as np


class Individual():
    img = pygame.image.load('assets/green.png')     # Loads image for the individual

    def __init__(self, pos):
        self.pos = pos
        self.velocity = np.array([0.2, 0.15])
        self.radius = 10

        # Transforms our image to the correct size
        self.c_img = pygame.transform.scale(
            self.img, (self.radius*2, self.radius*2))

    def move(self):
        """ Moves individual at a constant velocity """
        self.pos += self.velocity
        

    def draw(self, win):
        """ Draws individual """
        win.blit(self.c_img, self.pos-self.radius)