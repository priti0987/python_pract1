import pygame
import time
from pygame.locals import *


def draw_block():
    surface.fill((200,150,8))
    surface.blit(bloc,(block_x,block_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((800,650))
    surface.fill((200,150,8))

    bloc = pygame.image.load("resources/block.png").convert()
    block_x = 100
    block_y = 100
    surface.blit(bloc,(50,50))
    pygame.display.flip()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_DOWN:
                    block_y = block_y + 10
                    draw_block()

                if event.key == K_UP:
                    block_y = block_y - 10
                    draw_block()

                if event.key == K_LEFT:
                    block_x = block_x - 10
                    draw_block()

                if event.key == K_RIGHT:
                    block_x = block_x + 10
                    draw_block()

            elif event.type == QUIT:
                run = False
