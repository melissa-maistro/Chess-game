from pickle import TRUE
import pygame
from constants import *
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

        #self.create_board()

    def draw_squares(self, window : pygame.Surface):
        window.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(window, BEIGE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                                                #(X, Y, WIDTH, HEIGHT)

    def draw(self, window : pygame.Surface):
        self.draw_squares(window)
        for row in range(ROWS):

            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)

    #def get_piece(self, row, col):
    #    return self.board[row][col]

    #def empty_square(self, row, col):
    #    return self.board[row][col] == 0

    def set_piece(self, piece : Piece):
        if piece != 0 and piece != None:
            self.board[piece.row][piece.col] = piece

    def move(self, piece : Piece, row, col):
        old_row = piece.row
        old_col = piece.col

        piece.update_pos(row, col)
        self.board[row][col] = piece
        self.board[old_row][old_col] = 0

        if piece.type == 'Pedone' and piece.first_move:
            piece.first_move = False

    def remove(self, piece):
        self.board[piece.row][piece.col] = 0

        if piece.color == WHITE:

            if piece.type == 'Pedone':
                self.white_pawn_left -= 1
            
            elif piece.type == 'Cavallo':
                self.white_horse_left -= 1

            elif piece.type == 'Alfiere':
                self.white_bishop_left -= 1

            elif piece.type == 'Torre':
                self.white_rook_left -= 1

            elif piece.type == 'Re':
                self.white_king_left -= 1

            elif piece.type == 'Regina':
                self.white_queen_left -= 1 
        
        else:

            if piece.type == 'Pedone':
                self.black_pawn_left -= 1
            
            elif piece.type == 'Cavallo':
                self.black_horses_left -= 1

            elif piece.type == 'Alfiere':
                self.black_bishop_left -= 1

            elif piece.type == 'Torre':
                self.black_rook_left -= 1

            elif piece.type == 'Re':
                self.black_king_left -= 1

            elif piece.type == 'Regina':
                self.black_queen_left -= 1

    def try_move_valid(self ,piece : Piece, row, col):
        valid = False
        if piece.color == WHITE:
            #se il bianco e' sotto scacco
            if self.scacco_bianco():

                print("bianco sotto scacco")

                temp : Piece = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                #non puo' mangiare il re nero
                if temp != 0 and temp.type == 'Re' and temp.color == BLACK:
                    pass
                else:
                    #modifico board temporaneamente
                    self.board[row][col] = piece
                    print(f"pezzo spostato : {get_piece(self.board, row, col)}")
                    print(f"pezzo eliminato : {temp}")
                    self.board[y][x] = 0
                    
                    
                    #mossa valida solo se esce dallo scacco
                    if not self.scacco_bianco():
                        print(f"mossa valida : {row} , {col}")
                        valid = True
                    
                    #board ritorna come prima
                    self.board[y][x] = piece
                    print(f"pezzo tornato al suo posto : {get_piece(self.board, y, x)}")
                    self.board[row][col] = temp
                    print(f"pezzo tornato al suo posto : {get_piece(self.board, row, col)}")
                    
            
            #se non e' sotto scacco
            else:
                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                self.board[row][col] = piece
                print(f"pezzo spostato : {get_piece(self.board, row, col)}")
                print(f"pezzo eliminato : {temp}")
                self.board[y][x] = 0
                
                #comunque non puo' fare una mossa che lo metta sotto scacco
                if not self.scacco_bianco():
                    print(f"mossa valida : {row} , {col}")
                    valid = True
                
                #board ritorna come prima
                self.board[y][x] = piece
                print(f"pezzo tornato al suo posto : {get_piece(self.board, y, x)}")
                self.board[row][col] = temp
                print(f"pezzo tornato al suo posto : {get_piece(self.board, row, col)}")

        elif piece.color == BLACK:
            if self.scacco_nero():
                
                print("nero sotto scacco")

                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col
            
                if temp != 0 and temp.type == 'Re' and temp.color == WHITE:
                    pass
                else:
                    self.board[row][col] = piece
                    print(f"pezzo spostato : {get_piece(self.board, row, col)}")
                    print(f"pezzo eliminato : {temp}")
                    self.board[y][x] = 0
                    
                    if not self.scacco_nero():
                        print(f"mossa valida : {row} , {col}")
                        valid = True
                    
                    #board ritorna come prima
                    self.board[y][x] = piece
                    print(f"pezzo tornato al suo posto : {get_piece(self.board, y, x)}")
                    self.board[row][col] = temp
                    print(f"pezzo tornato al suo posto : {get_piece(self.board, row, col)}")

            else:
                temp = get_piece(self.board, row, col)
                y = piece.row
                x = piece.col

                self.board[row][col] = piece
                print(f"pezzo spostato : {get_piece(self.board, row, col)}")
                print(f"pezzo eliminato : {temp}")
                self.board[y][x] = 0
                
                if not self.scacco_nero():
                    print(f"mossa valida : {row} , {col}")
                    valid = True
                
                #board ritorna come prima
                self.board[y][x] = piece
                print(f"pezzo tornato al suo posto : {get_piece(self.board, y, x)}")
                self.board[row][col] = temp
                print(f"pezzo tornato al suo posto : {get_piece(self.board, row, col)}")

        return valid

    def get_valid_moves(self, piece : Piece):
        moves = []
        print("get_valid_moves : ...")
        for row in range(ROWS):
            for col in range(COLS):
                #se posizione valida
                if piece.check_pos(row, col, self.board):
                    if self.try_move_valid(piece, row, col):
                        moves.append((row, col))

        print("fine get_valid_moves")
        return moves

    def __getitem__(self, row, col):
        return self.board[row][col]

    def get_matrix(self):
        return self.board

    def print_board(self):
        for item in self.board:
            print(item)

    def scacco_bianco(self):
        king_row = 0
        king_col = 0

        #trovo posizione re
        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == WHITE:

                    if get_piece(self.board, row, col).type == 'Re':

                        king_row = row
                        king_col = col

        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color != WHITE:

                    piece : Piece = get_piece(self.board, row, col)

                    if piece.check_pos(king_row, king_col, self.board):
                        return True
        
        return False
    
    def scacco_nero(self):
        king_row = 0
        king_col = 0

        #trovo posizione re
        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == BLACK:

                    if get_piece(self.board, row, col).type == 'Re':

                        king_row = row
                        king_col = col

        for row in range(8):
            for col in range(8):

                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color != BLACK:

                    piece : Piece = get_piece(self.board, row, col)

                    if piece.check_pos(king_row, king_col, self.board):
                        return True

        return False


    def scaccomatto_bianco(self):

        if self.scacco_bianco() and not self.white_has_valid_moves():
            return True

        return False

    def scaccomatto_nero(self):
        
        if self.scacco_nero() and not self.black_has_valid_moves():
            return True

        return False

    def white_has_valid_moves(self):

        valid = False
        for row in range(8):
            for col in range(8):

                #per ogni pezzo bianco
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

                #per ogni pezzo bianco
                if not empty_square(self.board, row, col) and get_piece(self.board, row, col).color == BLACK:

                    piece = get_piece(self.board, row, col)
                    moves = self.get_valid_moves(piece)

                    if len(moves) != 0:
                        valid = True
                
        return valid

    def promotion(self):

        for col in range(COLS):

            piece = get_piece(self.board, 0, col)

            if piece != 0 and piece.type == 'Pedone':
                return piece, 0, col
            
            piece = get_piece(self.board, 7, col)

            if piece != 0 and piece.type == 'Pedone':
                return piece, 7, col
            
        return False
