import pygame
from board import Board
from constants import *
from piece import Piece, get_piece, empty_square

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
            return True

        return False

    def _move(self, row, col):

        print("_move iniziato")

        if self.selected != None and self.selected.check_pos(row, col, self.board.get_matrix()):
            print("_move valido")
            skipped = get_piece(self.board.get_matrix(), row, col)

            if skipped != 0:
                print(f"pedina mangiata: {skipped}")
                self.board.remove(skipped)
                print(f"{skipped} rimosso")

            self.board.move(self.selected, row, col)
            
            print("cambio turno")        
            self.change_turn()
            self.selected = None
            self.board.print_board()

        else:
            print("_move finito")
            return False
        return True

    def change_turn(self):
        self.valid_moves = []
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
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




