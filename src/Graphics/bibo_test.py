import pygame
import sys
from random import choice
import glob
import surfaces



def get_images():
    prefix = 'Textures'

    image_files = glob.glob(prefix + '/*.jpg')
    image_files.extend(glob.glob(prefix + '/*.png'))

    return [surfaces.Water(pygame.image.load(image))  for image in image_files ]


def main():
    pygame.init()

    size = width, height = 500, 420

    rect = (32, 32)

    screen = pygame.display.set_mode(size)

    patches = {}

    backgrounds = get_images()

    print backgrounds

    for x in xrange(0, width, rect[0]):
        for y in xrange(0, height, rect[1]):
            screen.blit(choice(backgrounds), (x, y))


    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    main()