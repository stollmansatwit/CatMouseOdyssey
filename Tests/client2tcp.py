# Client 2 
import sys
import pygame
import socket
import pickle

clock = pygame.time.Clock()
dt = 0

# Init Pygame 
pygame.init()

# Screen constants
WIDTH = 800  
HEIGHT = 600

# Create screen surface 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create socket
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client2.connect(('10.220.24.202', 1234))

# Player 2 rect
player2 = pygame.Rect(500, 500, 50, 50)

while True:

  # Check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
      
  # Movement keys
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_UP]:
    player2.y -= 400*dt
  if keys[pygame.K_DOWN]:
    player2.y += 400*dt
  if keys[pygame.K_LEFT]:
    player2.x -= 400*dt
  if keys[pygame.K_RIGHT]:
    player2.x += 400*dt
    
  # Send player 2 to client 1
  data = pickle.dumps(player2)
  client2.sendall(data)
  
  # Get player 1 from client 1
  data = client2.recv(4096)
  player1 = pickle.loads(data)
  
  # Draw screen
  screen.fill((255,255,255))
  pygame.draw.rect(screen, (0,255,0), player2)
  pygame.draw.circle(screen, (255,0,0), player1, 50)
  
  pygame.display.flip()
  dt = clock.tick(24)/1000