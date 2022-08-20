import pygame
from constants import *
from piece import Piece, empty_square, get_piece, check_boundaries

class Rook(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Torre')

    def check_pos(self, row, col, board : list[list]):
        
        for n in range(1,8):    #sinistra
            
            if row != self.row:
                break

            if not check_boundaries(self.row, self.col - n):
                break

            if not empty_square(board, self.row, self.col - n) and get_piece(board, self.row, self.col - n).color == self.color:
                break

            if not empty_square(board, self.row, self.col - n) and get_piece(board, self.row, self.col - n).color != self.color:
                if col == self.col - n:
                    return True
                break

            if col == self.col - n:
                return True

        for n in range(1,8):    #destra
            
            if row != self.row:
                break

            if not check_boundaries(self.row, self.col + n):
                break

            if not empty_square(board, self.row, self.col + n) and get_piece(board, self.row, self.col + n).color == self.color:
                break

            if not empty_square(board, self.row, self.col + n) and get_piece(board, self.row, self.col + n).color != self.color:
                if col == self.col + n:
                    return True
                break

            if col == self.col + n:
                return True

        for n in range(1,8):    #su
            
            if col != self.col:
                break

            if not check_boundaries(self.row - n, self.col):
                break

            if not empty_square(board, self.row - n, self.col) and get_piece(board, self.row - n, self.col).color == self.color:
                break

            if not empty_square(board, self.row - n, self.col) and get_piece(board, self.row - n, self.col).color != self.color:
                if row == self.row - n:
                    return True
                break

            if row == self.row - n:
                return True

        for n in range(1,8):    #giu
            
            if col != self.col:
                break

            if not check_boundaries(self.row + n, self.col):
                break

            if not empty_square(board, self.row + n, self.col) and get_piece(board, self.row + n, self.col).color == self.color:
                break

            if not empty_square(board, self.row + n, self.col) and get_piece(board, self.row + n, self.col).color != self.color:
                if row == self.row + n:
                    return True
                break

            if row == self.row + n:
                return True

        return False
