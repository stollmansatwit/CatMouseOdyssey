import socket
import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect(('10.220.40.179', 9999))

while True:

    # Get input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        client.send("up".encode())  
    elif keys[pygame.K_LEFT]:
        client.send("left".encode())
    elif keys[pygame.K_DOWN]:
        client.send("down".encode())
    elif keys[pygame.K_RIGHT]:
        client.send("right".encode())

    # Receive circle position
    data = client.recv(1024).decode()
    circle2_x, circle2_y = data.split(",")
    circle2_x = int(circle2_x)
    circle2_y = int(circle2_y)

    # Draw circle
    screen.fill((0,0,0)) 
    pygame.draw.circle(screen, (0,0,255), (circle2_x, circle2_y), 25)
    pygame.display.update()