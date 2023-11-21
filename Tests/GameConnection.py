import socket 
import pygame
import threading
import random
import math




# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))


clock = pygame.time.Clock()
running = True
dt = 0

red_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
blue_position = pygame.Vector2(screen.get_width() / 2-100, screen.get_height() / 2-100)

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

speed = 500
def goLeft(position):
    position.x -= speed * dt
def goRight(position):
    position.x += speed * dt
def goUp(position):
    position.y -= speed * dt
def goDown(position):
    position.y += speed * dt
    

# Function definitions
def network_handler():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 1234))
    print("looking for connection")
    while True:
        data, addr = sock.recvfrom(1024) 
        print("Received:", data)
        if data == b"left":
            goLeft(red_position)
        if data == b"right":
            goRight(red_position)
        if data == b"up":
            goUp(red_position)
        if data == b"down":
            goDown(red_position)

    


def game_loop():

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
    
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        goUp(red_position)
    if keys[pygame.K_UP]:
        goUp(blue_position)
    if keys[pygame.K_s]:
        goDown(red_position)
    if keys[pygame.K_DOWN]:
        goDown(blue_position)
    if keys[pygame.K_a]:
        goLeft(red_position)
    if keys[pygame.K_LEFT]:
        goLeft(blue_position)
    if keys[pygame.K_d]:
        goRight(red_position)
    if keys[pygame.K_RIGHT]:
        goRight(blue_position)

#TODO input not working... maybe threading needs to be for these ones as well


    # flip() the display to put your work on screen
    pygame.display.flip()

    wallHandler(red_position)
    wallHandler(blue_position)
    respawn(red_position)
    respawn(blue_position)



    distance = math.hypot(blue_position.x - red_position.x, 
                    blue_position.y - red_position.y)

    # Get sum of circle radii  
    radii_sum = 70

    # If distance is less than sum of radii, there is a collision
    if distance <= radii_sum:
        print("GAME OVER")
        pygame.quit()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.

    dt = clock.tick(60) / 1000


# Create threads 
# wall_thread = threading.Thread(target=wallHandler)
# respawn_thread = threading.Thread(target=respawn)
# left_thread = threading.Thread(target=goLeft)
# right_thread = threading.Thread(target=goRight)
# down_thread = threading.Thread(target=goDown)
# up_thread = threading.Thread(target=goUp)
net_thread = threading.Thread(target=network_handler)
game_thread = threading.Thread(target=game_loop)

# Start threads

game_thread.start()
net_thread.start()


isTrue = True

while isTrue:
    game_loop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isTrue = False
            pygame.quit()

pygame.quit()




