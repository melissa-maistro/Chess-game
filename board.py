import pygame
from constants import BROWN, ROWS, COLS, BEIGE, SQUARE_SIZE, WHITE, BLACK
from piece import Piece, empty_square, get_piece
from board_creation import create_board


class Board:

    def __init__(self):
        self.board = create_board()
        self.white_pawn_left = self.black_pawn_left = 8
        self.white_horse_left = self.black_horses_left = 2
        self.white_bishop_left = self.black_bishop_left = 2
        self.white_rook_left = self.black_rook_left = 2
        self.white_queen_left = self.black_queen_left = 1
        self.white_king_left = self.black_king_left = 1

    def draw_squares(self, window : pygame.Surface):
        window.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))   #(X, Y, WIDTH, HEIGHT)

    def draw(self, window : pygame.Surface):
        self.draw_squares(window)
        for row in range(ROWS):

            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    def set_piece(self, piece : Piece):
        if piece != 0 and piece != None:
            self.board[piece.row][piece.col] = piece

    def move(self, piece : Piece, row, col):
        old_row = piece.row
        old_col = piece.col

        piece.update_pos(row, col)
        self.board[row][col] = piece
        self.board[old_row][old_col] = 0

        if piece.type == 'Pawn':
            piece.move_count += 1

            if piece.move_count == 1:
                if piece.color == WHITE:
                    if old_row == row+2:
                        piece.two_squares_move = True
                else:
                    if old_row == row-2:
                        piece.two_squares_move = True

        if (piece.type == 'King' or piece.type == 'Rook') and not piece.moved:
            piece.moved = True

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0

        if piece.color == WHITE:

            if piece.type == 'Pawn':
                self.white_pawn_left -= 1
            
            elif piece.type == 'Cavallo':
                self.white_horse_left -= 1

            elif piece.type == 'Alfiere':
                self.white_bishop_left -= 1

            elif piece.type == 'Rook':
                self.white_rook_left -= 1

            elif piece.type == 'King':
                self.white_king_left -= 1

            elif piece.type == 'Regina':
                self.white_queen_left -= 1 
        
        else:

            if piece.type == 'Pawn':
                self.black_pawn_left -= 1
            
            elif piece.type == 'Cavallo':
                self.black_horses_left -= 1

            elif piece.type == 'Alfiere':
                self.black_bishop_left -= 1

            elif piece.type == 'Rook':
                self.black_rook_left -= 1

            elif piece.type == 'King':
                self.black_king_left -= 1

            elif piece.type == 'Regina':
                self.black_queen_left -= 1

    def try_move_valid(self ,piece : Piece, row, col):
        valid = False
        if piece.color == WHITE:
            #if WHITE is in check
            if self.white_check():

                #print("white in check")

                temp : Piece = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                #cannot eat BLACK king
                if temp != 0 and temp.type == 'King' and temp.color == BLACK:
                    pass
                else:
                    #temporary board change
                    self.board[row][col] = piece
                    #print(f"piece moved : {get_piece(self.board, row, col)}")
                    #print(f"piece removed : {temp}")
                    self.board[y][x] = 0
                    
                    
                    #valid move only if get out of check
                    if not self.white_check():
                        #print(f"valid move : {row} , {col}")
                        valid = True
                    
                    #board returns as before
                    self.board[y][x] = piece
                    #print(f"piece returned to its place  : {get_piece(self.board, y, x)}")
                    self.board[row][col] = temp
                    #print(f"piece returned to its place : {get_piece(self.board, row, col)}")
                    
            
            #if not in check
            else:
                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                self.board[row][col] = piece
                #print(f"piece moved : {get_piece(self.board, row, col)}")
                #print(f"piece removed : {temp}")
                self.board[y][x] = 0
                
                #cannot do a move that puts it in check
                if not self.white_check():
                    #print(f"valid move : {row} , {col}")
                    valid = True
                
                #board returns as before
                self.board[y][x] = piece
                #print(f"piece returned to its place : {get_piece(self.board, y, x)}")
                self.board[row][col] = temp
                #print(f"piece returned to its place : {get_piece(self.board, row, col)}")

        elif piece.color == BLACK:
            if self.black_check():
                
                #print("black in check")

                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col
            
                if temp != 0 and temp.type == 'King' and temp.color == WHITE:
                    pass
                else:
                    self.board[row][col] = piece
                    #print(f"piece moved : {get_piece(self.board, row, col)}")
                    #print(f"piece removed : {temp}")
                    self.board[y][x] = 0
                    
                    if not self.black_check():
                        #print(f"valid move : {row} , {col}")
                        valid = True
                    
                    self.board[y][x] = piece
                    #print(f"piece returned to its place : {get_piece(self.board, y, x)}")
                    self.board[row][col] = temp
                    #print(f"piece returned to its place : {get_piece(self.board, row, col)}")

            else:
                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                self.board[row][col] = piece
                #print(f"piece moved : {get_piece(self.board, row, col)}")
                #print(f"piece removed : {temp}")
                self.board[y][x] = 0
                
                if not self.black_check():
                    #print(f"valid move : {row} , {col}")
                    valid = True
                
                self.board[y][x] = piece
                #print(f"piece returned to its place : {get_piece(self.board, y, x)}")
                self.board[row][col] = temp
                #print(f"piece returned to its place : {get_piece(self.board, row, col)}")

        return valid

    def get_valid_moves(self, piece : Piece):
        moves = []
        #print("get_valid_moves : ...")
        for row in range(ROWS):
            for col in range(COLS):
                #if in a valid position
                if piece.check_pos(row, col, self.board):
                    if self.try_move_valid(piece, row, col):
                        moves.append((row, col))

        #print("end get_valid_moves")
        return moves

    def __getitem__(self, row, col):
        return self.board[row][col]

    def get_matrix(self):
        return self.board

    def print_board(self):
        for item in self.board:
            print(item)

    def white_check(self):
        king_row = 0
        king_col = 0

        #find king position
        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == WHITE:

                    if get_piece(self.board, row, col).type == 'King':

                        king_row = row
                        king_col = col

        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color != WHITE:

                    piece : Piece = get_piece(self.board, row, col)

                    if piece.check_pos(king_row, king_col, self.board):
                        return True
        
        return False
    
    def black_check(self):
        king_row = 0
        king_col = 0

        #find king position
        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == BLACK:

                    if get_piece(self.board, row, col).type == 'King':

                        king_row = row
                        king_col = col

        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color != BLACK:

                    piece : Piece = get_piece(self.board, row, col)

                    if piece.check_pos(king_row, king_col, self.board):
                        return True

        return False


    def white_checkmate(self):

        if self.white_check() and not self.white_has_valid_moves():
            return True

        return False

    def black_checkmate(self):
        
        if self.black_check() and not self.black_has_valid_moves():
            return True

        return False

    def white_has_valid_moves(self):

        valid = False
        for row in range(8):
            for col in range(8):

                #for each white piece
                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == WHITE:

                    piece = get_piece(self.board, row, col)
                    moves = self.get_valid_moves(piece)

                    if len(moves) != 0:
                        valid = True
                
        return valid

    def black_has_valid_moves(self):

        valid = False
        for row in range(8):
            for col in range(8):

                #for each black piece
                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == BLACK:

                    piece = get_piece(self.board, row, col)
                    moves = self.get_valid_moves(piece)

                    if len(moves) != 0:
                        valid = True
                
        return valid

    def promotion(self):

        for col in range(COLS):

            piece = get_piece(self.board, 0, col)

            if piece != 0 and piece.type == 'Pawn':
                return piece, 0, col
            
            piece = get_piece(self.board, 7, col)

            if piece != 0 and piece.type == 'Pawn':
                return piece, 7, col
            
        return False

    def short_castling(self, king : Piece):   #to the right
        
        if king == None or king.type != 'King':
            return False

        if king.color == BLACK:
            
            if king.row != 0 or king.col != 4:
                return False

            rook = self.board[0][7]

            if rook == 0 or rook.type != 'Rook':
                return False

            if king.moved or rook.moved:
                return False

            if not empty_square(self.board, 0, 5) or not empty_square(self.board, 0, 6):
                return False

            if not self.try_move_valid(king, 0, 6):
                return False

            return True

        else:

            if king.row != 7 or king.col != 4:
                return False

            rook = self.board[7][7]

            if rook == 0 or rook.type != 'Rook':
                return False

            if king.moved or rook.moved:
                return False

            if not empty_square(self.board, 7, 5) or not empty_square(self.board, 7, 6):
                return False

            if not self.try_move_valid(king, 7, 6):
                return False

            return True


    def long_castling(self, king : Piece):    #to the left
        
        if king == None or king.type != 'King':
            return False

        if king.color == BLACK:
            
            if king.row != 0 or king.col != 4:
                return False

            rook = self.board[0][0]

            if rook == 0 or rook.type != 'Rook':
                return False

            if king.moved or rook.moved:
                return False

            if not empty_square(self.board, 0, 1) or not empty_square(self.board, 0, 2) or not empty_square(self.board, 0, 3):
                return False

            if not self.try_move_valid(king, 0, 2):
                return False

            return True

        else:

            if king.row != 7 or king.col != 4:
                return False

            rook = self.board[7][0]

            if rook == 0 or rook.type != 'Rook':
                return False

            if king.moved or rook.moved:
                return False

            if not empty_square(self.board, 7, 1) or not empty_square(self.board, 7, 2) or not empty_square(self.board, 7, 3):
                return False

            if not self.try_move_valid(king, 7, 2):
                return False

            return True


    def castling_swap(self, king : Piece, king_row, king_col, rook : Piece, rook_row, rook_col):
        
        king.update_pos(king_row, king_col)
        self.board[king_row][king_col] = king

        #print(f"king : {king_row}, {king_col}")

        rook.update_pos(rook_row, rook_col)
        self.board[rook_row][rook_col] = rook

        #print(f"rook : {rook_row}, {rook_col}")


    def check_en_passant(self, pawn : Piece):

        #print("entering method en passant in file board")
        if pawn == None or pawn.type != 'Pawn':
            return False

        if pawn.move_count == 1 and pawn.two_squares_move:

            piece_right = self.board[pawn.row][pawn.col + 1]

            if piece_right != None and piece_right != 0 and piece_right.type == 'Pawn' and piece_right.color != pawn.color:
                piece1 = piece_right
            else:
                piece1 = 0

            piece_left = self.board[pawn.row][pawn.col - 1]

            if piece_left != None and piece_left != 0 and piece_left.type == 'Pawn' and piece_left.color != pawn.color:
                piece2 = piece_left
            else:
                piece2 = 0

            #print(pawn)
            #print(f"{piece1} , {piece2}")
            return piece1, piece2
        
        return False

        
