import pickle
import pygame
from Tiles import Tile, WinningTile
from Settings import tile_size, screen_width, screen_height

from Player import Player2
import sys

class Level:
    def __init__(self, level_structure, surface):
        #level setup
        self.display_surf = surface
        self.setup_level(level_structure)

        self.thecam_shift = 0
        self.thecam_shift2 = 0
        

    def setup_level(self, map_num):
        self.tiles = pygame.sprite.Group()
        # self.player = pygame.sprite.GroupSingle()
        # self.player2 = pygame.sprite.GroupSingle()

        self.players = pygame.sprite.Group()    #ADDED THE TWO SPRITES TO A GROUP TO MANAGE THEM TOGETHER
        self.winbound = pygame.sprite.Group()
        
        #nested for loop using enumerate to get the col/row index
        for row_index,row in enumerate(map_num):
            for col_index, cell in enumerate(row):
                if cell== 'X':
                    #multiply index by tile size pixels to find location to place tile
                    x= col_index*tile_size
                    y= row_index*tile_size
                    tile = Tile(tile_size, (x,y))
                    self.tiles.add(tile)
                #print(f'{row_index},{col_index}:{cell}')
                # if cell=='P':
                #     x= col_index*tile_size
                #     y= row_index*tile_size
                #     player_sprite = Player((x,y))
                #     self.players.add(player_sprite)
                if cell=='U':
                    x= col_index*tile_size
                    y= row_index*tile_size
                    player_sprite2 = Player2((x,y))
                    self.players.add(player_sprite2)
                if cell == 'W':
                    x= col_index*tile_size
                    y= row_index*tile_size
                    boundary = WinningTile(tile_size, (x,y))
                    self.winbound.add(boundary)

        global client2_socket
        client2_socket = player_sprite2.client2


        
                
                

    def scroll_x(self):
        
        #player = self.player.sprite
        for player in self.players.sprites():
            if player == self.players.sprites()[0]:
                player_x = player.rect.centerx #track x coordinate of player
                direction_x = player.direction.x

        

                if player_x < (screen_width/5) and direction_x < 0: #direction < 0 means left
                    self.thecam_shift=6
                    player.speed = 0
                elif player_x > (screen_width/5*4) and direction_x >0:
                    self.thecam_shift = -6
                    player.speed = 0
                else:
                    self.thecam_shift = 0
                    player.speed = 6


    def horizontal_collision(self):
        #player = self.player.sprite
        for player in self.players.sprites():

            player.rect.x += player.direction.x*player.speed
            
            

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                    #if player.direction.y >0:

                    

    def vertical_collision(self):
        #player = self.player.sprite
        #player.rect.x += player.direction.x*player.speed
        for player in self.players.sprites():
            player.gravity()
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                    elif player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0


    
    def end_map_collision(self):
        for player in self.players.sprites():
            for sprite in self.winbound.sprites():
                if player == self.players.sprites()[0]:
                    if sprite.rect.colliderect(player.rect):
                        pygame.quit()
                        print("PLAYER 1 (M) WINS")
                        sys.exit()
                        

    def sprite_colllision(self):
        if self.players.sprites()[0].rect.colliderect(self.players.sprites()[1]):
            print("PLAYER 1 (M) GOT CAUGHT, PLAYER 2 (C) WINS")
            pygame.quit()
            sys.exit()
                    
    def fall_off_map(self):
        for player in self.players.sprites():
            if player.rect.top > screen_height:
                if player == self.players.sprites()[0]:
                    pygame.quit()
                    print("PLAYER 1 (M) FELL, SO PLAYER 2 (C) WINS")
                    sys.exit()
                elif player == self.players.sprites()[1]:
                    pygame.quit()
                    print("PLAYER 2 (C) FELL, SO PLAYER 1 (M) WINS")
                    sys.exit()

    def recvFromNet(self):
        # Get player 2 from client 2
    
        try:
            data, addr = client2_socket.recvfrom(16384)
            global player1
            player1 = pickle.loads(data)
            
            
        except TimeoutError:
            print("connection ended")
        rect= player1
        pygame.draw.rect(self.display_surf, 'red', rect)
        

    def run(self):
        #level tiles
        self.tiles.update(self.thecam_shift)
        self.tiles.draw(self.display_surf)
        self.scroll_x()
        
        
        
        #player
        # self.player.update()
        #self.player2.update()
        
        
        self.end_map_collision()
        self.fall_off_map()
        # self.sprite_colllision()
        
        self.horizontal_collision()
        self.vertical_collision()

        self.players.draw(self.display_surf)
        self.players.update()
        self.recvFromNet()
        # rect= player1
        # pygame.draw.rect(self.display_surf, 'red', rect)
        
        # self.player.draw(self.display_surf)
        # self.player2.draw(self.display_surf)
        

        