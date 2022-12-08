from constants import WHITE, BLACK
from piece import Piece, empty_square, get_piece

class Pawn(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Pawn')
        self.move_count = 0
        self.two_squares_move = False

    def check_pos(self, row, col, board : list[list]):
        
        #print("check_pos pawn")
        if self.color == WHITE:

            #print("white pawn")

            if (row == self.row - 1) and (col == self.col):

                if not empty_square(board, row, col):
                    return False
                return True

            if self.move_count == 0 and (row == self.row - 2) and (col == self.col):

                if not empty_square(board, row, col) or not empty_square(board, self.row - 1, col):
                    return False
                return True

            if row == self.row - 1 and (col == self.col - 1 or col == self.col + 1):

                if not empty_square(board, row, col) and (get_piece(board, row, col).color == BLACK):
                    return True
                return False
        
        elif self.color == BLACK:

            #print("black pawn")

            if (row == self.row + 1) and (col == self.col):

                if not empty_square(board, row, col):
                    return False
                return True

            if self.move_count == 0 and (row == self.row + 2) and (col == self.col):

                if not empty_square(board, row, col) or not empty_square(board, self.row + 1, col):
                    return False
                return True

            if row == self.row + 1 and (col == self.col - 1 or col == self.col + 1):

                if not empty_square(board, row, col) and (get_piece(board, row, col).color == WHITE):
                    return True
                return False
