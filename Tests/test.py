# Import modules
import pygame
import threading

# Initialize Pygame  
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600)) 

# Game loop
def game_loop():

    # Check events 
    

    # Draw logic  
    screen.fill((0,0,0))  
    pygame.draw.rect(screen, (255,0,0), (100,100,100,100))

    # Update display
    pygame.display.flip() 

# Create thread
game_thread = threading.Thread(target=game_loop)
game_thread.start()

isTrue = True

while isTrue:
    game_loop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isTrue = False