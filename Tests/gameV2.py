import pygame
import sys
pygame.init()


clock = pygame.time.Clock()

size = (1280,720)
screen = pygame.display.set_mode(size)

def main(window):
    screen.fill("purple")
    
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)
main(screen)    

pygame.quit()