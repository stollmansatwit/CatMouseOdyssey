import gameV1
import socket
import threading
import pygame



def network_handler():
    print("looking for connection")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", 1234))
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print("Received:", data)
            if data == int.to_bytes(3):
                gameV1.goLeft(gameV1.red_position)
            if data == int.to_bytes(4):
                gameV1.goRight(gameV1.red_position)
            if data == int.to_bytes(1):
                gameV1.goUp(gameV1.red_position)
            if data == int.to_bytes(2):
                gameV1.goDown(gameV1.red_position)
        except socket.timeout:
            pass

def game_loop():
    gameV1.main()
        

net_thread = threading.Thread(target=network_handler)
game_thread = threading.Thread(target=game_loop)

# Start threads
net_thread.start()
game_thread.start()
