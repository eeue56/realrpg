from pygame.surface import Surface
import pygame


class Floor(Surface):
    
    def __init__(self, image, movement_speed):
        Surface.__init__(self, image.get_size())

        self.image = image
        self.blit(self.image, (0, 0))

        self.movement_speed = movement_speed


class Water(Floor):

    def __init__(self, image):
        Floor.__init__(self, image, 0.5)


class Ground(Floor):

    def __init__(self, image):
        Floor.__init__(self, image, 1)
