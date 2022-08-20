from abc import abstractmethod
import pygame
from constants import *

class Piece:

    PADDING = 15    #spazio tra pedina e bordo
    OUTLINE = 2     #bordo cella

    def __init__(self, row, col, color, type):
        self.row = row
        self.col = col
        self.color = color
        self.type = type

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2

    def draw(self, window : pygame.Surface):
        
        if self.type == 'Pedone':
            
            if self.color == WHITE:   
                window.blit(WHITE_PAWN, (self.x - WHITE_PAWN.get_width()//2,    #x,y sono al centro della pedina ma non possiamo mettere l'immagine li 
                        self.y - WHITE_PAWN.get_height()//2))                   #perche' x,y saranno l'angolo in alto a sinistra dell'immagine
            else:
                window.blit(BLACK_PAWN, (self.x - BLACK_PAWN.get_width()//2,     
                        self.y - BLACK_PAWN.get_height()//2))

        elif self.type == 'Cavallo':
            
            if self.color == WHITE:   
                window.blit(WHITE_HORSE, (self.x - WHITE_HORSE.get_width()//2,     
                        self.y - WHITE_HORSE.get_height()//2))                   
            else:
                window.blit(BLACK_HORSE, (self.x - BLACK_HORSE.get_width()//2,     
                        self.y - BLACK_HORSE.get_height()//2))           


        elif self.type == 'Alfiere':
           
            if self.color == WHITE:   
                window.blit(WHITE_BISHOP, (self.x - WHITE_BISHOP.get_width()//2,     
                        self.y - WHITE_BISHOP.get_height()//2))                   
            else:
                window.blit(BLACK_BISHOP, (self.x - BLACK_BISHOP.get_width()//2,     
                        self.y - BLACK_BISHOP.get_height()//2))             


        elif self.type == 'Torre':
            
            if self.color == WHITE:   
                window.blit(WHITE_ROOK, (self.x - WHITE_ROOK.get_width()//2,     
                        self.y - WHITE_ROOK.get_height()//2))                   
            else:
                window.blit(BLACK_ROOK, (self.x - BLACK_ROOK.get_width()//2,     
                        self.y - BLACK_ROOK.get_height()//2))           


        elif self.type == 'Re':
            
            if self.color == WHITE:   
                window.blit(WHITE_KING, (self.x - WHITE_KING.get_width()//2,     
                        self.y - WHITE_KING.get_height()//2))                   
            else:
                window.blit(BLACK_KING, (self.x - BLACK_KING.get_width()//2,     
                        self.y - BLACK_KING.get_height()//2))             


        elif self.type == 'Regina':
            
            if self.color == WHITE:   
                window.blit(WHITE_QUEEN, (self.x - WHITE_QUEEN.get_width()//2,     
                        self.y - WHITE_QUEEN.get_height()//2))                   
            else:
                window.blit(BLACK_QUEEN, (self.x - BLACK_QUEEN.get_width()//2,     
                        self.y - BLACK_QUEEN.get_height()//2))             


    def __repr__(self):
        return str(self.type)

    def update_pos(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    @abstractmethod
    def check_pos(self, row, col, board : list[list]):
        pass

#--------------------------------------------------------------------------------------------------------------------------------

@staticmethod
def empty_square(board, row, col):
    return board[row][col] == 0

@staticmethod
def get_piece(board, row, col):
    return board[row][col]

@staticmethod
def check_boundaries(row, col):
    return row >= 0 and row <= 7 and col >= 0 and col <= 7