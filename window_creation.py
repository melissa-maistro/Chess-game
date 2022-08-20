from tkinter import *
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from rook import Rook
from queen import Queen
from constants import *

# class Window(Frame):

#     def __init__(self, parent):
#         global piece_color
#         global piece_type

#         Frame.__init__(self, parent)
    
#         piece_type = StringVar()
#         piece_color = StringVar()

#         photo1 = PhotoImage(file='pawn_white.png')
#         pawn_white = Button(self, height=50, width=50, bg='BLACK', image= photo1, 
#                             command= lambda: self.click('pawn', 'white'))

#         pawn_white.grid(row=0, column=0)

#         photo2 = PhotoImage(file='horse_white.png')
#         horse_white = Button(self, height=50, width=50, bg='BLACK', image= photo2,
#                             command= lambda: self.click('horse', 'white'))

#         horse_white.grid(row=0, column=1)

#         photo3 = PhotoImage(file='bishop_white.png')
#         bishop_white = Button(self, height=50, width=50, bg='BLACK', image= photo3, 
#                             command= lambda: self.click('bishop', 'white'))

#         bishop_white.grid(row=0, column=2)

#         photo4 = PhotoImage(file='rook_white.png')
#         rook_white = Button(self, height=50, width=50, bg='BLACK', image= photo4, 
#                             command= lambda: self.click('rook', 'white'))

#         rook_white.grid(row=0, column=3)

#         photo5 = PhotoImage(file='queen_white.png')
#         queen_white = Button(self, height=50, width=50, bg='BLACK', image= photo5, 
#                             command= lambda: self.click('queen', 'white'))

#         queen_white.grid(row=0, column=4)

#         photo6 = PhotoImage(file='pawn_black.png')
#         pawn_black = Button(self, height=50, width=50, bg='WHITE', image= photo6, 
#                             command= lambda: self.click('pawn', 'black'))

#         pawn_black.grid(row=1, column=0)

#         photo7 = PhotoImage(file='horse_black.png')
#         horse_black = Button(self, height=50, width=50, bg='WHITE', image= photo7, 
#                             command= lambda: self.click('horse', 'black'))

#         horse_black.grid(row=1, column=1)

#         photo8 = PhotoImage(file='bishop_black.png')
#         bishop_black = Button(self, height=50, width=50, bg='WHITE', image= photo8, 
#                             command= lambda: self.click('bishop', 'black'))

#         bishop_black.grid(row=1, column=2)

#         photo9 = PhotoImage(file='rook_black.png')
#         rook_black = Button(self, height=50, width=50, bg='WHITE', image= photo9, 
#                             command= lambda: self.click('rook', 'black'))

#         rook_black.grid(row=1, column=3)

#         photo10 = PhotoImage(file='queen_black.png')
#         queen_black = Button(self, height=50, width=50, bg='WHITE', image= photo10, 
#                             command= lambda: self.click('queen', 'black'))

#         queen_black.grid(row=1, column=4)

#     def click(self, type, color):
#         global piece_color
#         global piece_type

#         piece_type = type
#         piece_color = color
#         print(type)
#         print(color)
#         self.destroy()

#     def promotion_selection(row, col):
#         if piece_color == 'white':

#             if piece_type == 'pawn':
#                 new_piece = Pawn(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'horse':
#                 new_piece = Horse(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'bishop':
#                 new_piece = Bishop(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'queen':
#                 new_piece = Queen(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'rook':
#                 new_piece = Rook(row, col, WHITE)
#                 return new_piece
        
#         elif piece_color == 'black':

#             if piece_type == 'pawn':
#                 new_piece = Pawn(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'horse':
#                 new_piece = Horse(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'bishop':
#                 new_piece = Bishop(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'queen':
#                 new_piece = Queen(row, col, WHITE)
#                 return new_piece

#             elif piece_type == 'rook':
#                 new_piece = Rook(row, col, WHITE)
#                 return new_piece

#         return None




#rimettendo questo codice nel file main funziona la prima volta che si ha una promozione
#adesso non si caricano bene i bottoni, infatti non si riesce a schiacciarli e non hanno la foto...

def create_window():
    global piece_color
    global piece_type

    window = Tk()
    window.title("Promotion : choose new piece")
    window.geometry("540x215")
    window.resizable(False, False)

    piece_type = StringVar()
    piece_color = StringVar()

    frame = Frame(window)
    frame.pack()

    photo1 = PhotoImage(file='pawn_white.png')
    pawn_white = Button(frame, height=100, width=100, bg='BLACK', image= photo1, 
                        command= lambda: click(window, 'pawn', 'white'))

    pawn_white.grid(row=0, column=0)

    photo2 = PhotoImage(file='horse_white.png')
    horse_white = Button(frame, height=100, width=100, bg='BLACK', image= photo2,
                        command= lambda: click(window, 'horse', 'white'))

    horse_white.grid(row=0, column=1)

    photo3 = PhotoImage(file='bishop_white.png')
    bishop_white = Button(frame, height=100, width=100, bg='BLACK', image= photo3, 
                        command= lambda: click(window, 'bishop', 'white'))

    bishop_white.grid(row=0, column=2)

    photo4 = PhotoImage(file='rook_white.png')
    rook_white = Button(frame, height=100, width=100, bg='BLACK', image= photo4, 
                        command= lambda: click(window, 'rook', 'white'))

    rook_white.grid(row=0, column=3)

    photo5 = PhotoImage(file='queen_white.png')
    queen_white = Button(frame, height=100, width=100, bg='BLACK', image= photo5, 
                        command= lambda: click(window, 'queen', 'white'))

    queen_white.grid(row=0, column=4)

    photo6 = PhotoImage(file='pawn_black.png')
    pawn_black = Button(frame, height=100, width=100, bg='WHITE', image= photo6, 
                        command= lambda: click(window, 'pawn', 'black'))

    pawn_black.grid(row=1, column=0)

    photo7 = PhotoImage(file='horse_black.png')
    horse_black = Button(frame, height=100, width=100, bg='WHITE', image= photo7, 
                        command= lambda: click(window, 'horse', 'black'))

    horse_black.grid(row=1, column=1)

    photo8 = PhotoImage(file='bishop_black.png')
    bishop_black = Button(frame, height=100, width=100, bg='WHITE', image= photo8, 
                        command= lambda: click(window, 'bishop', 'black'))

    bishop_black.grid(row=1, column=2)

    photo9 = PhotoImage(file='rook_black.png')
    rook_black = Button(frame, height=100, width=100, bg='WHITE', image= photo9, 
                        command= lambda: click(window, 'rook', 'black'))

    rook_black.grid(row=1, column=3)

    photo10 = PhotoImage(file='queen_black.png')
    queen_black = Button(frame, height=100, width=100, bg='WHITE', image= photo10, 
                        command= lambda: click(window, 'queen', 'black'))

    queen_black.grid(row=1, column=4)

    return window

def click(window, type, color):
    global piece_color
    global piece_type

    piece_type = type
    piece_color = color
    print(type)
    print(color)
    window.destroy()

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