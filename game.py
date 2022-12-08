import pygame
from board import Board
from constants import WHITE, BLACK, BLUE, SQUARE_SIZE, RED
from piece import Piece, get_piece

class Game:
    def __init__(self, window):
        self._init()
        self.window = window
        print("gioco creato")

    def _init(self):
        self.selected : Piece = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = []
        self.valid_en_passant  = False          # indica se en passant e' valido per questo turno
        self.en_passant_pieces = (0,0,0)        # 1) pedone da mangiare, 2) pedone a destra che potrebbe mangiarlo, 3) pedone a sinistra che potrebbe mangiarlo

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
            self.short_castling(piece)                              #aggiungo eventuali altre mosse speciali
            self.long_castling(piece)
            self.add_en_passant_move()
            return True

        return False

    def _move(self, row, col):

        print("_move iniziato")
        if self.move_castling(row, col):                            #arrocco
            print("arrocco effettuato")
            self.change_turn()
            self.selected = None
            return True
        
        elif self.move_en_passant(row, col):                        #en passant
            self.board.remove(self.en_passant_pieces[0])
            self.change_turn()
            self.selected = None
            return True
        
        elif self.selected != None and self.selected.check_pos(row, col, self.board.get_matrix()) and self.board.try_move_valid(self.selected, row, col):       #move normale
            print("_move valido")
            skipped = get_piece(self.board.get_matrix(), row, col)

            if skipped != 0:
                print(f"pedina mangiata: {skipped}")
                self.board.remove(skipped)
                print(f"{skipped} rimosso")

            self.board.move(self.selected, row, col)
            
            print("cambio turno")
            self.check_en_passant()     
            self.change_turn()
            self.selected = None
            self.board.print_board()

        else:
            print("_move finito")
            return False
        return True

    def move_castling(self, row, col):
        if self.selected != None:
            
            if self.short_castling(self.selected):

                print("arrocco corto")
                
                if self.turn == BLACK and (row,col) == (0,6):

                    print("nero")

                    rook = get_piece(self.board.get_matrix(), 0, 7)

                    self.board.castling_swap(self.selected, 0, 6, rook, 0, 5)

                    return True
                
                elif self.turn == WHITE and (row, col) == (7,6):

                    print("bianco")

                    rook = get_piece(self.board.get_matrix(), 7, 7)

                    self.board.castling_swap(self.selected, 7, 6, rook, 7, 5)

                    return True

            
            if self.long_castling(self.selected):

                print("arrocco lungo")
                
                if self.turn == BLACK and (row,col) == (0,2):

                    print("nero")

                    rook = get_piece(self.board.get_matrix(), 0, 0)

                    self.board.castling_swap(self.selected, 0, 2, rook, 0, 3)

                    return True
                
                elif self.turn == WHITE and (row, col) == (7,2):

                    print("bianco")

                    rook = get_piece(self.board.get_matrix(), 7, 0)

                    self.board.castling_swap(self.selected, 7, 2, rook, 7, 3)

                    return True
        
        print("no arrocco")
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
        if self.board.scaccomatto_bianco() or self.board.scaccomatto_nero():
            return True
        return False

    def promotion(self):
        
        return self.board.promotion()

    def replace_piece(self, old_piece, new_piece):

        self.board.remove(old_piece)
        self.board.set_piece(new_piece) 

    def short_castling(self, king):

        if self.board.short_castling(king):

            print("arrocco corto possibile")
            
            if king.color == BLACK:

                self.valid_moves.append((0,6))
                print("aggiunto arrocco corto a mosse valide")
            
            else:

                self.valid_moves.append((7,6))
                print("aggiunto arrocco corto a mosse valide")

            return True

        return False


    def long_castling(self, king):

        if self.board.long_castling(king):

            print("arrocco lungo possibile")
            
            if king.color == BLACK:

                self.valid_moves.append((0,2))
                print("aggiunto arrocco lungo a mosse valide")
            
            else:

                self.valid_moves.append((7,2))
                print("aggiunto arrocco lungo a mosse valide")

            return True

        return False

    def check_en_passant(self):

        if self.board.check_en_passant(self.selected) != False:
            print("en passant possibile")

            self.valid_en_passant = True

            piece_right, piece_left = self.board.check_en_passant(self.selected)

            self.en_passant_pieces = (self.selected, piece_right, piece_left)

            print(f"{self.selected}, {piece_right}, {piece_left}")

        else:
            print("no en passant")
            self.valid_en_passant = False
            self.en_passant_pieces = (0,0,0)

    def add_en_passant_move(self):

        if self.valid_en_passant:

            if self.turn == WHITE:

                piece_right = self.en_passant_pieces[1]
                if piece_right != 0:
                    
                    if self.selected == piece_right:
                        self.valid_moves.append((self.selected.row -1, self.selected.col -1))
                        print("aggiunta mossa en passant")
                
                piece_left = self.en_passant_pieces[2]
                if piece_left != 0:
                    
                    if self.selected == piece_left:
                        self.valid_moves.append((self.selected.row -1, self.selected.col +1))
                        print("aggiunta mossa en passant")

            else:

                piece_right = self.en_passant_pieces[1]
                if piece_right != 0:
                    
                    if self.selected == piece_right:
                        self.valid_moves.append((self.selected.row +1, self.selected.col -1))
                        print("aggiunta mossa en passant")
                
                piece_left = self.en_passant_pieces[2]
                if piece_left != 0:
                    
                    if self.selected == piece_left:
                        self.valid_moves.append((self.selected.row +1, self.selected.col +1))
                        print("aggiunta mossa en passant")
        
    
    def move_en_passant(self, row, col):

        if self.turn == WHITE:

            piece_right = self.en_passant_pieces[1]
            if piece_right != 0:
                
                if self.selected == piece_right and (row,col) == (self.selected.row -1, self.selected.col -1):
                    self.board.move(self.selected, row, col)
                    print("en passant effettuato")
                    return True
            
            piece_left = self.en_passant_pieces[2]
            if piece_left != 0:
                
                if self.selected == piece_left and (row,col) == (self.selected.row -1, self.selected.col +1):
                    self.board.move(self.selected, row, col)
                    print("en passant effettuato")
                    return True
            
        else:

            piece_right = self.en_passant_pieces[1]
            if piece_right != 0:
                
                if self.selected == piece_right and (row, col) == (self.selected.row +1, self.selected.col -1):
                    self.board.move(self.selected, row, col)
                    print("en passant effettuato")
                    return True
            
            piece_left = self.en_passant_pieces[2]
            if piece_left != 0:
                
                if self.selected == piece_left and (row, col) == (self.selected.row +1, self.selected.col +1):
                    self.board.move(self.selected, row, col)
                    print("en passant effettuato")
                    return True
        
        return False


