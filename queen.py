from piece import Piece, empty_square, get_piece, check_boundaries

class Queen(Piece):

    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'Queen')

    def check_pos(self, row, col, board : list[list]):
        
        for n in range(1,8):    #northwest diagonal
            
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

        for n in range(1,8):    #southwest diagonal
            
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

        for n in range(1,8):    #southeast diagonal
            
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

        for n in range(1,8):    #northeast diagonal
            
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

        for n in range(1,8):    #left
            
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

        for n in range(1,8):    #right
            
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

        for n in range(1,8):    #up
            
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

        for n in range(1,8):    #down
            
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
