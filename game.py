import pygame
from board import Board
from constants import WHITE, BLACK, BLUE, SQUARE_SIZE, RED
from piece import Piece, get_piece

class Game:
    def __init__(self, window):
        self._init()
        self.window = window
        #print("game created")

    def _init(self):
        self.selected : Piece = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.valid_en_passant  = False          # indicates if en passant is valid for this turn
        self.en_passant_pieces = (0,0,0)        # (pawn to eat, pawn to the right who could eat it, pawn to the left who could eat it)

    def update(self):
        self.board.draw(self.window)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:   
            result = self._move(row, col)   

            if not result:  
                self.selected = None
                self.select(row, col)
        
        piece = get_piece(self.board.get_matrix(), row, col)   

        if piece != 0 and piece.color == self.turn: 
            self.selected = piece                   
            self.valid_moves = self.board.get_valid_moves(piece)
            #adding special moves
            self.short_castling(piece)                              
            self.long_castling(piece)
            self.add_en_passant_move()
            return True

        return False

    def _move(self, row, col):

        #print("_move started")
        #castling
        if self.move_castling(row, col):                            
            #print("castling carried out")
            self.change_turn()
            self.selected = None
            return True
        
        #en passant
        elif self.move_en_passant(row, col):                        
            self.board.remove(self.en_passant_pieces[0])
            self.change_turn()
            self.selected = None
            return True
        
        #regular move
        elif self.selected != None and self.selected.check_pos(row, col, self.board.get_matrix()) and self.board.try_move_valid(self.selected, row, col):       
            #print("valid _move")
            skipped = get_piece(self.board.get_matrix(), row, col)

            if skipped != 0:
                #print(f"piece removed: {skipped}")
                self.board.remove(skipped)
                #print(f"{skipped} removed")

            self.board.move(self.selected, row, col)
            
            #print("change turn")
            self.check_en_passant()     
            self.change_turn()
            self.selected = None
            self.board.print_board()

        else:
            #print("_move finished")
            return False
        return True

    def move_castling(self, row, col):
        if self.selected != None:
            
            if self.short_castling(self.selected):

                #print("short castling")
                
                if self.turn == BLACK and (row,col) == (0,6):

                    #print("black")

                    rook = get_piece(self.board.get_matrix(), 0, 7)

                    self.board.castling_swap(self.selected, 0, 6, rook, 0, 5)

                    return True
                
                elif self.turn == WHITE and (row, col) == (7,6):

                    #print("white")

                    rook = get_piece(self.board.get_matrix(), 7, 7)

                    self.board.castling_swap(self.selected, 7, 6, rook, 7, 5)

                    return True

            
            if self.long_castling(self.selected):

                #print("long castling")
                
                if self.turn == BLACK and (row,col) == (0,2):

                    #print("black")

                    rook = get_piece(self.board.get_matrix(), 0, 0)

                    self.board.castling_swap(self.selected, 0, 2, rook, 0, 3)

                    return True
                
                elif self.turn == WHITE and (row, col) == (7,2):

                    #print("white")

                    rook = get_piece(self.board.get_matrix(), 7, 0)

                    self.board.castling_swap(self.selected, 7, 2, rook, 7, 3)

                    return True
        
        #print("no castling")
        return False

    def change_turn(self):
        self.valid_moves = []
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move

            if self.board.short_castling(self.selected) and ((row, col) == (0,6) or (row, col) == (7,6)):

                pygame.draw.circle(self.window, RED, (col * SQUARE_SIZE + SQUARE_SIZE//2, 
                                row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
            
            elif self.board.long_castling(self.selected) and ((row, col) == (0,2) or (row, col) == (7,2)):

                pygame.draw.circle(self.window, RED, (col * SQUARE_SIZE + SQUARE_SIZE//2, 
                                row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

            else:
                
                pygame.draw.circle(self.window, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, 
                                row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def winner(self):
        if self.board.white_checkmate() or self.board.black_checkmate():
            return True
        return False

    def promotion(self):
        
        return self.board.promotion()

    def replace_piece(self, old_piece, new_piece):

        self.board.remove(old_piece)
        self.board.set_piece(new_piece) 

    def short_castling(self, king):

        if self.board.short_castling(king):

            #print("short castling is possible")
            
            if king.color == BLACK:

                self.valid_moves.append((0,6))
                #print("short castling added to valid moves")
            
            else:

                self.valid_moves.append((7,6))
                #print("short castling added to valid moves")

            return True

        return False


    def long_castling(self, king):

        if self.board.long_castling(king):

            #print("long castling is possible")
            
            if king.color == BLACK:

                self.valid_moves.append((0,2))
                #print("long castling added to valid moves")
            
            else:

                self.valid_moves.append((7,2))
                #print("long castling added to valid moves")

            return True

        return False

    def check_en_passant(self):

        if self.board.check_en_passant(self.selected) != False:
            #print("en passant is possible")

            self.valid_en_passant = True

            piece_right, piece_left = self.board.check_en_passant(self.selected)

            self.en_passant_pieces = (self.selected, piece_right, piece_left)

            #print(f"{self.selected}, {piece_right}, {piece_left}")

        else:
            #print("no en passant")
            self.valid_en_passant = False
            self.en_passant_pieces = (0,0,0)

    def add_en_passant_move(self):

        if self.valid_en_passant:

            if self.turn == WHITE:

                piece_right = self.en_passant_pieces[1]
                if piece_right != 0:
                    
                    if self.selected == piece_right:
                        self.valid_moves.append((self.selected.row -1, self.selected.col -1))
                        #print("en passant added to moves")
                
                piece_left = self.en_passant_pieces[2]
                if piece_left != 0:
                    
                    if self.selected == piece_left:
                        self.valid_moves.append((self.selected.row -1, self.selected.col +1))
                        #print("en passant added to moves")

            else:

                piece_right = self.en_passant_pieces[1]
                if piece_right != 0:
                    
                    if self.selected == piece_right:
                        self.valid_moves.append((self.selected.row +1, self.selected.col -1))
                        #print("en passant added to moves")
                
                piece_left = self.en_passant_pieces[2]
                if piece_left != 0:
                    
                    if self.selected == piece_left:
                        self.valid_moves.append((self.selected.row +1, self.selected.col +1))
                        #print("en passant added to moves")
        
    
    def move_en_passant(self, row, col):

        if self.turn == WHITE:

            piece_right = self.en_passant_pieces[1]
            if piece_right != 0:
                
                if self.selected == piece_right and (row,col) == (self.selected.row -1, self.selected.col -1):
                    self.board.move(self.selected, row, col)
                    #print("en passant carried out")
                    return True
            
            piece_left = self.en_passant_pieces[2]
            if piece_left != 0:
                
                if self.selected == piece_left and (row,col) == (self.selected.row -1, self.selected.col +1):
                    self.board.move(self.selected, row, col)
                    #print("en passant carried out")
                    return True
            
        else:

            piece_right = self.en_passant_pieces[1]
            if piece_right != 0:
                
                if self.selected == piece_right and (row, col) == (self.selected.row +1, self.selected.col -1):
                    self.board.move(self.selected, row, col)
                    #print("en passant carried out")
                    return True
            
            piece_left = self.en_passant_pieces[2]
            if piece_left != 0:
                
                if self.selected == piece_left and (row, col) == (self.selected.row +1, self.selected.col +1):
                    self.board.move(self.selected, row, col)
                    #print("en passant carried out")
                    return True
        
        return False


