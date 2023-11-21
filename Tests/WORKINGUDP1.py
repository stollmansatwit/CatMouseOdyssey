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
pygame.display.set_caption("Client 1") #Sets title

# Create socket
client1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client1.settimeout(20.0)
client1.bind(('0.0.0.0', 2346))

client2_ip = '127.0.0.1'
client2_port = 2345




# Player 1 circle 
player1 =  pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while True:
  
  # Check for quit
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
      
  # Movement keys
  keys = pygame.key.get_pressed()
  speed = 600
  if keys[pygame.K_w]:
    player1.y -= speed*dt
  if keys[pygame.K_s]:  
    player1.y += speed*dt
  if keys[pygame.K_a]:
    player1.x -= speed*dt
  if keys[pygame.K_d]:
    player1.x += speed*dt

  if player1.x > WIDTH:
    player1.x = 0
  if player1.x <0:
    player1.x = WIDTH
  if player1.y > HEIGHT:
    player1.y = 0
  if player1.y <0:
    player1.y = HEIGHT
    
  # Send player 1 to client 2
  datasent = pickle.dumps(player1)
  client1.sendto(datasent, (client2_ip, client2_port))
  
  # Get player 2 from client 2
  MAX_RETRIES = 50

  for i in range(MAX_RETRIES):
    try:
      data, addr = client1.recvfrom(4096)
      player2 = pickle.loads(data) 
      break
    except TimeoutError:
      print("connection ended")
    except ConnectionResetError:
      if i < MAX_RETRIES-1:
        continue
      else:
        raise
      
  # Draw screen
  screen.fill((255,255,255)) 
  pygame.draw.rect(screen, (0,255,0), player2)
  pygame.draw.circle(screen, (255,0,0), player1, 50)
  
  pygame.display.flip()
  dt = clock.tick(60) / 1000