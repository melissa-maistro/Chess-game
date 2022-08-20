import pygame
from constants import *
from piece import Piece, empty_square, get_piece, check_boundaries

class Bishop(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Alfiere')

    def check_pos(self, row, col, board : list[list]):
        
        for n in range(1,8):    #diagonale nord-ovest
            
            if not check_boundaries(self.row - n, self.col - n):
                break

            if not empty_square(board, self.row - n, self.col - n) and get_piece(board, self.row - n, self.col - n).color == self.color:
                break

            if not empty_square(board, self.row - n, self.col - n) and get_piece(board, self.row - n, self.col - n).color != self.color:
                if row == self.row - n and col == self.col - n:
                    return True
                break

            if row == self.row - n and col == self.col - n:
                return True

        for n in range(1,8):    #diagonale sud-ovest
            
            if not check_boundaries(self.row + n, self.col - n):
                break

            if not empty_square(board, self.row + n, self.col - n) and get_piece(board, self.row + n, self.col - n).color == self.color:
                break

            if not empty_square(board, self.row + n, self.col - n) and get_piece(board, self.row + n, self.col - n).color != self.color:
                if row == self.row + n and col == self.col - n:
                    return True
                break

            if row == self.row + n and col == self.col - n:
                return True

        for n in range(1,8):    #diagonale sud-est
            
            if not check_boundaries(self.row + n, self.col + n):
                break

            if not empty_square(board, self.row + n, self.col + n) and get_piece(board, self.row + n, self.col + n).color == self.color:
                break

            if not empty_square(board, self.row + n, self.col + n) and get_piece(board, self.row + n, self.col + n).color != self.color:
                if row == self.row + n and col == self.col + n:
                    return True
                break

            if row == self.row + n and col == self.col + n:
                return True

        for n in range(1,8):    #diagonale nord-est
            
            if not check_boundaries(self.row - n, self.col + n):
                break

            if not empty_square(board, self.row - n, self.col + n) and get_piece(board, self.row - n, self.col + n).color == self.color:
                break

            if not empty_square(board, self.row - n, self.col + n) and get_piece(board, self.row - n, self.col + n).color != self.color:
                if row == self.row - n and col == self.col + n:
                    return True
                break

            if row == self.row - n and col == self.col + n:
                return True

        return False
