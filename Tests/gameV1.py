# Example file showing a circle moving on screen
import random
import pygame
import math

running = True

clock = pygame.time.Clock()

# Input Handling
speed = 500



def goLeft(position, dt = clock.tick(60)/1000):
        position.x -= speed * dt
def goRight(position, dt = clock.tick(60)/1000):
        position.x += speed * dt
def goUp(position, dt = clock.tick(60)/1000):
        position.y -= speed * dt
def goDown(position, dt = clock.tick(60)/1000):
        position.y += speed * dt



def handle_input(position, dt = clock.tick(60)/1000):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        goUp(position, dt)
    if keys[pygame.K_s]:
        goDown(position, dt)
    if keys[pygame.K_a]:
        goLeft(position, dt)
    if keys[pygame.K_d]:
        goRight(position, dt)


def setup():
    global red_position, blue_position, screen
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    red_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    blue_position = pygame.Vector2(screen.get_width() / 2-100, screen.get_height() / 2-100)




def main():
    

    setup()
    dt = 0
   
    def wallHandler(position):
        if position.x>screen.get_width():
            position.x = 0
        if position.x<0:
            position.x = screen.get_width()
        if position.y>screen.get_height():
            position.y = 0
        if position.y<0:
            position.y = screen.get_height()

    def respawn(position):
        if position.x >= 100 and position.x <= 500 and position.y >= 200 and position.y <= 470:
            position.x = random.randint(0,screen.get_width())
            position.y = random.randint(0,screen.get_height())


     





    global running
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        rectValue = pygame.Rect(100, 200, 400, 270)

        pygame.draw.circle(screen, "blue", blue_position, 50)
        pygame.draw.circle(screen, "red", red_position, 40)
        line = pygame.draw.aaline(screen, "yellow", (500, 500), (600, 600))
        pygame.draw.circle(screen, "cyan", red_position, 30)
        pygame.draw.circle(screen, "green", blue_position, 20)
        pygame.draw.circle(screen, "pink", red_position, 10)

        rect = pygame.draw.rect(screen, "yellow", (rectValue))
        
        distance = math.hypot(blue_position.x - red_position.x, 
                    blue_position.y - red_position.y)

        # Get sum of circle radii  
        radii_sum = 70

        # If distance is less than sum of radii, there is a collision
        if distance <= radii_sum:
            print("GAME OVER")
            running = False

        # flip() the display to put your work on screen
        pygame.display.flip()

        wallHandler(red_position)
        wallHandler(blue_position)
        respawn(red_position)
        respawn(blue_position)
        

        


        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.

        dt = clock.tick(60) / 1000
        handle_input(blue_position, dt)

    pygame.quit()

running = False   