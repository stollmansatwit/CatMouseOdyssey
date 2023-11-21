# Client 1
import sys
import pygame
import socket
import pickle

#Clock
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
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.bind(('0.0.0.0', 1234))
client1.listen(1)


# Accept client 2 connection
client2, addr = client1.accept()

# Player 1 circle 
player1 =  pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while True:
  
  # Check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
      
  # Movement keys
  keys = pygame.key.get_pressed()
  
  if keys[pygame.K_w]:
    player1.y -= 400*dt
  if keys[pygame.K_s]:  
    player1.y += 400*dt
  if keys[pygame.K_a]:
    player1.x -= 400*dt
  if keys[pygame.K_d]:
    player1.x += 400*dt
    
  # Send player 1 to client 2
  data = pickle.dumps(player1)
  client2.sendall(data)
  
  # Get player 2 from client 2
  data = client2.recv(4096)
  player2 = pickle.loads(data)
  
  # Draw screen
  screen.fill((255,255,255)) 
  pygame.draw.circle(screen, (255,0,0), player1, 50)
  pygame.draw.rect(screen, (0,255,0), player2)
  
  pygame.display.flip()
  dt = clock.tick(24) / 1000