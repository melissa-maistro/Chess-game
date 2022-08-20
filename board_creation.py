import pygame
from pawn import Pawn
from horse import Horse
from piece import Piece
from bishop import Bishop
from rook import Rook
from king import King
from queen import Queen
from constants import *

def create_board():
    board = [[]]

    for row in range(ROWS):
        board.append([])

        for col in range(COLS):

            if row == 0:
                if col == 0:
                    board[row].append(Rook(row, col, BLACK))

                elif col == 1:
                    board[row].append(Horse(row, col, BLACK))

                elif col == 2:
                    board[row].append(Bishop(row, col, BLACK))

                elif col == 3:
                    board[row].append(Queen(row, col, BLACK))

                elif col == 4:
                    board[row].append(King(row, col, BLACK))

                elif col == 5:
                    board[row].append(Bishop(row, col, BLACK))
                
                elif col == 6:
                    board[row].append(Horse(row, col, BLACK))

                elif col == 7:
                    board[row].append(Rook(row, col, BLACK))


            elif row == 1:
                board[row].append(Pawn(row, col, BLACK))
            
            elif row == 6:
                board[row].append(Pawn(row, col, WHITE))

            elif row == 7:
                if col == 0:
                    board[row].append(Rook(row, col, WHITE))

                elif col == 1:
                    board[row].append(Horse(row, col, WHITE))

                elif col == 2:
                    board[row].append(Bishop(row, col, WHITE))

                elif col == 3:
                    board[row].append(Queen(row, col, WHITE))

                elif col == 4:
                    board[row].append(King(row, col, WHITE))

                elif col == 5:
                    board[row].append(Bishop(row, col, WHITE))
                
                elif col == 6:
                    board[row].append(Horse(row, col, WHITE))

                elif col == 7:
                    board[row].append(Rook(row, col, WHITE))

            else:
                board[row].append(0)

    print("board creata")
    return board