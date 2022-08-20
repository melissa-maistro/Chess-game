import pygame
from constants import *
from piece import Piece, empty_square, get_piece

class Pawn(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Pedone')
        self.first_move = True

    def check_pos(self, row, col, board : list[list]):
        
        #print("check_pos pawn")
        if self.color == WHITE:

            #print("Pedone bianco")

            if (row == self.row - 1) and (col == self.col):

                if not empty_square(board, row, col):
                    return False
                return True

            if self.first_move and (row == self.row - 2) and (col == self.col):

                if not empty_square(board, row, col) or not empty_square(board, self.row - 1, col):
                    return False
                return True

            if row == self.row - 1 and (col == self.col - 1 or col == self.col + 1):

                if not empty_square(board, row, col) and (get_piece(board, row, col).color == BLACK):
                    return True
                return False
        
        elif self.color == BLACK:

            #print("Pedone nero")

            if (row == self.row + 1) and (col == self.col):

                if not empty_square(board, row, col):
                    return False
                return True

            if self.first_move and (row == self.row + 2) and (col == self.col):

                if not empty_square(board, row, col) or not empty_square(board, self.row + 1, col):
                    return False
                return True

            if row == self.row + 1 and (col == self.col - 1 or col == self.col + 1):

                if not empty_square(board, row, col) and (get_piece(board, row, col).color == WHITE):
                    return True
                return False
