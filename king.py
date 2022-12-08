from piece import Piece, empty_square, get_piece

class King(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'King')
        self.moved = False

    def check_pos(self, row, col, board : list[list]):
        
        if col == self.col and (row == self.row - 1 or row == self.row + 1):

            if not empty_square(board, row, col) and get_piece(board, row, col).color == self.color:
                return False
            return True

        if col == self.col - 1 and (row == self.row or row == self.row - 1 or row == self.row + 1):

            if not empty_square(board, row, col) and get_piece(board, row, col).color == self.color:
                return False
            return True

        if col == self.col + 1 and (row == self.row or row == self.row - 1 or row == self.row + 1):

            if not empty_square(board, row, col) and get_piece(board, row, col).color == self.color:
                return False
            return True

        return False
