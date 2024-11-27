import pygame
import random
import numpy as np

SIZE = 500
DIMENSION = 3
BACKGROUND = "#000000"
COMPUTER = "#FF0000"
PLAYER = "#00FF00"
white = (255,255,255)
black = (0,0,0)
screen_color = black


class Board:
    def __init__(self):
        
        self.dim = DIMENSION
        self.level = 1
        self.tiles = np.zeros((self.level))

        self.block_size = SIZE//self.dim

    def create_level(self):
        for i in range(self.level):
            self.tiles[i] = (random.randint(0,self.dim-1), random.randint(0,self.dim-1))

    def reset(self):
        self.tiles = np.zeros((self.level))
        
    def get_board(board):
        return board.tiles

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()
running = True
screen.fill(screen_color)
board = Board()

def draw_grid(board):
    block_size = board.block_size
    for x in range(0, SIZE, block_size):
        for y in range(0, SIZE, block_size):
            rect = pygame.Rect(x,y, block_size, block_size)
            pygame.draw.rect(screen, white, rect, 1)

while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    draw_grid(board)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()