import socket
import pygame
import gameV1
from time import *
import keyboard  # using module keyboard


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
hostname = socket.gethostname()
ip = (socket.gethostbyname(hostname))

# pygame.init()

# keys = pygame.key.get_pressed()
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# pressed = {'left': False, 'right': False, 'up': False, 'down': False}

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sock.close()
#             exit()
            
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 pressed['left'] = True
#             elif event.key == pygame.K_RIGHT:
#                 pressed['right'] = True  
#             elif event.key == pygame.K_UP:
#                 pressed['up'] = True
#             elif event.key == pygame.K_DOWN:
#                 pressed['down'] = True
                
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 pressed['left'] = False
#             elif event.key == pygame.K_RIGHT:
#                 pressed['right'] = False
#             elif event.key == pygame.K_UP:
#                 pressed['up'] = False
#             elif event.key == pygame.K_DOWN:
#                 pressed['down'] = False
                
#         if pressed['left']:
#             sock.sendto(b"left", (ip, 1234))
#         if pressed['right']:
#             sock.sendto(b"right", (ip, 1234))
#         if pressed['up']:
#             sock.sendto(b"up", (ip, 1234))
#         if pressed['down']:
#             sock.sendto(b"down", (ip, 1234))





def on_press(key):
    if key.name == keyboard.KEY_UP:
        sock.sendto((b'\x01'), (ip, 1234))
        print('Up pressed')

    if key.name == keyboard.KEY_DOWN:
        sock.sendto((b'\x02'), (ip, 1234))
        print('down pressed')

    if key.name == "left":
        sock.sendto((b'\x03'), (ip, 1234))
        print('left pressed')


    if key.name == "right":
        sock.sendto((b'\x04'), (ip, 1234))
        print('right pressed') 

while True:

    if keyboard.is_pressed(keyboard.KEY_UP):
        while keyboard.is_pressed(keyboard.KEY_UP):
            print ("moving up")
            sock.sendto((b'\x01'), (ip, 1234))
            sleep(.01)
    if keyboard.is_pressed(keyboard.KEY_DOWN):
        while keyboard.is_pressed(keyboard.KEY_DOWN):
            print ("moving down")
            sock.sendto((b'\x02'), (ip, 1234))
            sleep(.01)
    if keyboard.is_pressed("left"):
        while keyboard.is_pressed("left"):
            print ("moving left")
            sock.sendto((b'\x03'), (ip, 1234))
            sleep(.01)
    if keyboard.is_pressed("right"):
        while keyboard.is_pressed("right"):
            print ("moving right")
            sock.sendto((b'\x04'), (ip, 1234))
            sleep(.01)
    

        


