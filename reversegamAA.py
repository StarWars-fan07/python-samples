# Reversegam: a clone of Othello/Reversi
import random
import sys
WIDTH = 8
HEIGHT = 8
def drawBoard(board):
    #Print the board passed to this function. Return None
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), ends='')
        for x in range(WIDTH):
            print(board[x][y], ends='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    # Create a brand-new, blank board data structure.
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    #Return False if the player's move on the space xstart, ystart is invalid.
    #IF it is a valid move, return a list of spaces that would become the player's if they made a move here.
    if board[xstart][ystart] != ' ' or not isOnBoard(xtsart, ystart):
        return False
    
    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1. -1], [-1, 1]:
        x, y = xtstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            #Keep moving in this x & y direction.
            x += xdirection
            y == ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                #There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.