import pygame
import sys
import time

WIDTH = 1150
HEIGHT = 600
LINE_WIDTH = 5
BG_COLOR = (65,105,225) #   rgb royal blue  
LINE_COLOR = (95,158,160) # rgb cadet blue
RED = (255, 0, 0) # rgb red
GREEN = (0, 255, 0)
BLACK = (0, 0, 0) # rgb black

shipBoard = [[[0 for i in range(8)] for j in range(8)] for k in range(2)]
shotBoard = [[[0 for i in range(8)] for j in range(8)] for k in range(2)]

#   printing the board
def drawLines():
    for i in range(9):
        #   player 1 board
        pygame.draw.line(screen, LINE_COLOR, (100, 150 + 50 * i), (500, 150 + 50 * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (100 + 50 * i, 150), (100 + 50 * i, 550), LINE_WIDTH)
        
        #player 2 board
        pygame.draw.line(screen, LINE_COLOR, (650, 150 + 50 * i), (1050, 150 + 50 * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (650 + 50 * i, 150), (650 + 50 * i, 550), LINE_WIDTH)

#   drawing shot
def drawShot(x, y, player):
    addX = 100
    addY = 150
    shotColor = BLACK
    if player == 1:
        addX = addX + 550
    if hit(x, y, player):
        shotColor = RED
    pygame.draw.line(screen, shotColor, (addX + 10 + 50 * x, addY + 10 + 50 * y), (addX + 40 + 50 * x, addY + 40 + 50 * y), LINE_WIDTH)
    pygame.draw.line(screen, shotColor, (addX + 40 + 50 * x, addY + 10 + 50 * y), (addX + 10 + 50 * x, addY + 40 + 50 * y), LINE_WIDTH)
    pygame.display.update()

def drawShip(x, y, player):
    addX = 100
    addY = 150
    shotColor = BLACK
    if player == 1:
        addX = addX + 550
    pygame.draw.line(screen, shotColor, (addX + 10 + 50 * x, addY + 10 + 50 * y), (addX + 40 + 50 * x, addY + 40 + 50 * y), LINE_WIDTH)
    pygame.draw.line(screen, shotColor, (addX + 40 + 50 * x, addY + 10 + 50 * y), (addX + 10 + 50 * x, addY + 40 + 50 * y), LINE_WIDTH)
    pygame.display.update()

def markShot(row, col, player):
    shotBoard[player][row][col] = 1

def availablSquare(row, col, player):
    return shotBoard[player][row][col] == 0

def hit(row, col, player):
    return shipBoard[1 - player][row][col] == 1

def gameOver(player):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if shipBoard[1 - player][i][j] == 1 and shotBoard[player][i][j] == 1:
                cnt = cnt + 1
    return cnt == 5

def displayPlayer(player):
    font = pygame.font.Font('freesansbold.ttf', 32)
    if player == 0:
        player1Text = font.render('Player 1', True, BLACK, GREEN)
        player2Text = font.render('Player 2', True, BLACK, RED)
    else:
        player1Text = font.render('Player 1', True, BLACK, RED)
        player2Text = font.render('Player 2', True, BLACK, GREEN)
    textRect = player1Text.get_rect()
    textRect.center = (WIDTH // 4, HEIGHT // 7)
    screen.blit(player1Text, textRect)
    textRect = player2Text.get_rect()
    textRect.center = (WIDTH // 4 * 3, HEIGHT // 7)
    screen.blit(player2Text, textRect)
    pygame.display.update()

def displayWiner(player):
    font = pygame.font.Font('freesansbold.ttf', 32)
    if player == 0:
        player1Text = font.render('Player 1 wins', True, BLACK, GREEN)
        player2Text = font.render('Player 2 loses', True, BLACK, RED)
    else:
        player1Text = font.render('Player 1 loses', True, BLACK, RED)
        player2Text = font.render('Player 2 wins', True, BLACK, GREEN)
    textRect = player1Text.get_rect()
    textRect.center = (WIDTH // 4, HEIGHT // 7)
    screen.blit(player1Text, textRect)
    textRect = player2Text.get_rect()
    textRect.center = (WIDTH // 4 * 3, HEIGHT // 7)
    screen.blit(player2Text, textRect)
    pygame.display.update()

def displayPlacing(player):
    font = pygame.font.Font('freesansbold.ttf', 32)
    if player == 0:
        player1Text = font.render('Player 1 placing ship...', True, BLACK, GREEN)
        player2Text = font.render('Player 2 waiting', True, BLACK, RED)
    else:
        player1Text = font.render('Player 1 ship placed', True, BLACK, RED)
        player2Text = font.render('Player 2 placing ship...', True, BLACK, GREEN)
    textRect = player1Text.get_rect()
    textRect.center = (WIDTH // 4, HEIGHT // 7)
    screen.blit(player1Text, textRect)
    textRect = player2Text.get_rect()
    textRect.center = (WIDTH // 4 * 3, HEIGHT // 7)
    screen.blit(player2Text, textRect)
    pygame.display.update()

def placeShip(player):
    ok = False
    k = 0
    mouse = []
    #   player 1 ship placing
    while ok == False:
        if k == 0:
            screen.fill(BG_COLOR)
            drawLines()
            displayPlacing(player)
            pygame.display.update()
        for event in pygame.event.get():
            #   quit event
            if event.type == pygame.QUIT:
                sys.exit()
            #   click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   mouse position
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                playerTable = -1
                #   player board
                if mouseX in range(100, 501) and mouseY in range(150, 551):
                    playerTable = 0
                elif mouseX in range(650, 1051) and mouseY in range(150, 551):
                    playerTable = 1
                else:
                    playerTable = -1
                #   board position
                boardX = -1
                boardY = -1
                if playerTable == 0:
                    mouseX = mouseX - 100
                    mouseY = mouseY - 150
                    boardX = mouseX // 50
                    boardY = mouseY // 50
                elif playerTable == 1:
                    mouseX = mouseX - 650
                    mouseY = mouseY - 150
                    boardX = mouseX // 50
                    boardY = mouseY // 50
                if playerTable == player:
                    mouse.append((boardX, boardY))
                    k += 1
                    if k == 1:
                        drawShip(mouse[0][0], mouse[0][1], player)
                        pygame.display.update()
                    if k == 2:
                        drawShip(mouse[1][0], mouse[1][1], player)
                        pygame.display.update()
                        time.sleep(0.5)
                        if mouse[0][0] == mouse[1][0]:
                            if abs(mouse[0][1] - mouse[1][1]) + 1 == 5:
                                x = mouse[0][0]
                                y = min(mouse[0][1], mouse[1][1])
                                for i in range(0, 5):
                                    drawShip(x, y + i, player)
                                    shipBoard[player][x][y + i] = 1
                                time.sleep(1)
                                return
                            else:
                                k = 0
                                mouse = []
                        elif mouse[0][1] == mouse[1][1]:
                            if abs(mouse[0][0] - mouse[1][0]) + 1 == 5:
                                x = min(mouse[0][0], mouse[1][0])
                                y = mouse[0][1]
                                for i in range(0, 5):
                                    drawShip(x + i, y, player)
                                    shipBoard[player][x + i][y] = 1
                                time.sleep(1)
                                return
                            else:
                                k = 0
                                mouse = []
                        else:
                            k = 0
                            mouse = []

if __name__ == "__main__":
    #   initial game state
    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption('BATTLESHIPS')
    placeShip(0)
    placeShip(1)
    print(shipBoard[1])
    #   set table for playing
    screen.fill(BG_COLOR)
    drawLines()
    pygame.display.update()
    player = 0
    #   main loop
    while True:
        displayPlayer(player)
        #   events handler  
        for event in pygame.event.get():
            #   quit event
            if event.type == pygame.QUIT:
                sys.exit()
            #   click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   mouse position
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                playerTable = -1
                #   player board
                if mouseX in range(100, 501) and mouseY in range(150, 551):
                    playerTable = 0
                elif mouseX in range(650, 1051) and mouseY in range(150, 551):
                    playerTable = 1
                else:
                    playerTable = -1
                #   board position
                boardX = -1
                boardY = -1
                if playerTable == 0:
                    mouseX = mouseX - 100
                    mouseY = mouseY - 150
                    boardX = mouseX // 50
                    boardY = mouseY // 50
                elif playerTable == 1:
                    mouseX = mouseX - 650
                    mouseY = mouseY - 150
                    boardX = mouseX // 50
                    boardY = mouseY // 50
                if playerTable == player:
                    if availablSquare(boardX, boardY, player):
                        markShot(boardX, boardY, player)
                        drawShot(boardX, boardY, player)
                        if hit(boardX, boardY, player) == False:
                            player = 1 - player
                        if gameOver(player):
                            displayWiner(player)
                            print("Player " + str(player + 1) + " win!")
                            time.sleep(3)
                            sys.exit()
                print(mouseX, mouseY, playerTable, boardX, boardY)