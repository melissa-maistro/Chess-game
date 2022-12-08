from piece import Piece, empty_square, get_piece

class Horse(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Horse')

    def check_pos(self, row, col, board : list[list]):
        
        if not empty_square(board, row, col) and get_piece(board, row, col).color == self.color:
            return False

        elif col == self.col - 1 and (row == self.row - 2 or row == self.row + 2):
            return True

        elif col == self.col - 2 and (row == self.row - 1 or row == self.row + 1):
            return True

        elif col == self.col + 1 and (row == self.row - 2 or row == self.row + 2):
            return True

        elif col == self.col + 2 and (row == self.row - 1 or row == self.row + 1):
            return True

        return False

