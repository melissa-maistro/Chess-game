from  tkinter import *
from constants import *
from game import Game
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from rook import Rook
from queen import Queen

class Promozione(Tk):
    def __init__(self):
        self.create_buttons()
    def create_buttons(self):
        
        photo2 = PhotoImage(file='horse_white.png')
        horse_white = Button(self, height=50, width=50, bg='BLACK', image= photo2,
                            command= lambda: self.click('horse', 'white'))

        horse_white.grid(row=0, column=1)
    def click(self, type, color):
        global piece_color
        global piece_type

        piece_type = type
        piece_color = color
        print(type)
        print(color)
        self.destroy()

def promotion_selection(row, col):
    if piece_color == 'white':

        if piece_type == 'pawn':
            new_piece = Pawn(row, col, WHITE)
            return new_piece

        elif piece_type == 'horse':
            new_piece = Horse(row, col, WHITE)
            return new_piece

        elif piece_type == 'bishop':
            new_piece = Bishop(row, col, WHITE)
            return new_piece

        elif piece_type == 'queen':
            new_piece = Queen(row, col, WHITE)
            return new_piece

        elif piece_type == 'rook':
            new_piece = Rook(row, col, WHITE)
            return new_piece

    elif piece_color == 'black':

        if piece_type == 'pawn':
            new_piece = Pawn(row, col, WHITE)
            return new_piece

        elif piece_type == 'horse':
            new_piece = Horse(row, col, WHITE)
            return new_piece

        elif piece_type == 'bishop':
            new_piece = Bishop(row, col, WHITE)
            return new_piece

        elif piece_type == 'queen':
            new_piece = Queen(row, col, WHITE)
            return new_piece

        elif piece_type == 'rook':
            new_piece = Rook(row, col, WHITE)
            return new_piece

    return None