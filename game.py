import pygame
import sys
import time

WIDTH = 1150
HEIGHT = 600

BG_COLOR = (65,105,225) #   rgb royal blue  
LINE_COLOR = (95,158,160) # rgb cadet blue
RED = (255, 0, 0)
BLACK = (0, 0, 0)
LINE_WIDTH = 5

def drawLines():

    for i in range(9):
        #   player 1 board
        pygame.draw.line(screen, LINE_COLOR, (100, 150 + 50 * i), (500, 150 + 50 * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (100 + 50 * i, 150), (100 + 50 * i, 550), LINE_WIDTH)
        
        #player 2 board
        pygame.draw.line(screen, LINE_COLOR, (650, 150 + 50 * i), (1050, 150 + 50 * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (650 + 50 * i, 150), (650 + 50 * i, 550), LINE_WIDTH)


shipBoard = [[[0 for i in range(8)] for j in range(8)] for k in range(2)]
shotBoard = [[[0 for i in range(8)] for j in range(8)] for k in range(2)]



if __name__ == "__main__":

    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('BATTLESHIPS')
    screen.fill(BG_COLOR)
    drawLines()
    pygame.display.update()
    
    player = 0
    #   main loop
    while True:
        #   events handler
            
        for event in pygame.event.get():
            #   quit event
            if event.type == pygame.QUIT:
                sys.exit()
           