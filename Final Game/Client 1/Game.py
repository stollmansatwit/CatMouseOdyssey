import pygame, sys
from Settings import *
from Tiles import Tile,WinningTile
from Level import Level


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(map1, screen)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('purple')
        level.run()
        
        pygame.display.flip()
        clock.tick(60)

main()