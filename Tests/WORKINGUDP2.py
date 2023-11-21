# Client 2 
import sys
import pygame
import socket
import pickle
import json

clock = pygame.time.Clock()
dt = 0

# Init Pygame 
pygame.init()

# Screen constants
WIDTH = 800  
HEIGHT = 600

# Create screen surface 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#Set title
pygame.display.set_caption("Client 2") 

# Create socket
client2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Setting amount of time socket has to create connection
client2.settimeout(1.0)
client2.bind(('0.0.0.0', 2345))

client1_ip = '127.0.0.1'
client1_port = 2346
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

  if player2.x > WIDTH:
    player2.x = 0
  if player2.x <0:
    player2.x = WIDTH
  if player2.y > HEIGHT:
    player2.y = 0
  if player2.y <0:
    player2.y = HEIGHT
    
  #Sending player2 information using pickle
  datasent = pickle.dumps(player2)
  client2.sendto(datasent, (client1_ip, client1_port))

  #Try to recieve data and when connection ends, break
  try:
    data, addr = client2.recvfrom(4096)
  except(TimeoutError):
    print("Connection ended")
    break
  
  #After data is recieved, load it
  player1 = pickle.loads(data)
  
  # Draw screen
  screen.fill((255,255,255))
  pygame.draw.rect(screen, (0,255,0), player2)
  pygame.draw.circle(screen, (255,0,0), player1, 50)
  
  pygame.display.flip()
  dt = clock.tick(60)/1000