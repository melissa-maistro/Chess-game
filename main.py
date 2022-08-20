import pygame
from tkinter import *
from constants import *
from game import Game
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from rook import Rook
from queen import Queen
from window_creation import create_window, promotion_selection


FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Scacchi')

  
# window2 = Tk()
# window2.title("Promotion : choose new piece")
# window2.geometry("600x200")
# window2.resizable(False, False)

# piece_type = StringVar()
# piece_color = StringVar()

# frame = Frame(window2)
# frame.pack()
# #________________________________________________________________________________
# photo1 = PhotoImage(file='pawn_white.png')
# pawn_white = Button(frame, height=50, width=50, bg='BLACK', image= photo1, 
#                     command= lambda: click('pawn', 'white'))

# pawn_white.grid(row=0, column=0)

# photo2 = PhotoImage(file='horse_white.png')
# horse_white = Button(frame, height=50, width=50, bg='BLACK', image= photo2,
#                     command= lambda: click('horse', 'white'))

# horse_white.grid(row=0, column=1)

# photo3 = PhotoImage(file='bishop_white.png')
# bishop_white = Button(frame, height=50, width=50, bg='BLACK', image= photo3, 
#                     command= lambda: click('bishop', 'white'))

# bishop_white.grid(row=0, column=2)

# photo4 = PhotoImage(file='rook_white.png')
# rook_white = Button(frame, height=50, width=50, bg='BLACK', image= photo4, 
#                     command= lambda: click('rook', 'white'))

# rook_white.grid(row=0, column=3)

# photo5 = PhotoImage(file='queen_white.png')
# queen_white = Button(frame, height=50, width=50, bg='BLACK', image= photo5, 
#                     command= lambda: click('queen', 'white'))

# queen_white.grid(row=0, column=4)

# photo6 = PhotoImage(file='pawn_black.png')
# pawn_black = Button(frame, height=50, width=50, bg='WHITE', image= photo6, 
#                     command= lambda: click('pawn', 'black'))

# pawn_black.grid(row=1, column=0)

# photo7 = PhotoImage(file='horse_black.png')
# horse_black = Button(frame, height=50, width=50, bg='WHITE', image= photo7, 
#                     command= lambda: click('horse', 'black'))

# horse_black.grid(row=1, column=1)

# photo8 = PhotoImage(file='bishop_black.png')
# bishop_black = Button(frame, height=50, width=50, bg='WHITE', image= photo8, 
#                     command= lambda: click('bishop', 'black'))

# bishop_black.grid(row=1, column=2)

# photo9 = PhotoImage(file='rook_black.png')
# rook_black = Button(frame, height=50, width=50, bg='WHITE', image= photo9, 
#                     command= lambda: click('rook', 'black'))

# rook_black.grid(row=1, column=3)

# photo10 = PhotoImage(file='queen_black.png')
# queen_black = Button(frame, height=50, width=50, bg='WHITE', image= photo10, 
#                     command= lambda: click('queen', 'black'))

# queen_black.grid(row=1, column=4)
# #________________________________________________________________________________



# def click(type, color):
#     global piece_color
#     global piece_type

#     piece_type = type
#     piece_color = color
#     print(type)
#     print(color)
#     window2.destroy()

# def promotion_selection(row, col):
#     global piece_color
#     global piece_type

#     if piece_color == 'white':

#         if piece_type == 'pawn':
#             new_piece = Pawn(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'horse':
#             new_piece = Horse(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'bishop':
#             new_piece = Bishop(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'queen':
#             new_piece = Queen(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'rook':
#             new_piece = Rook(row, col, WHITE)
#             return new_piece
    
#     elif piece_color == 'black':

#         if piece_type == 'pawn':
#             new_piece = Pawn(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'horse':
#             new_piece = Horse(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'bishop':
#             new_piece = Bishop(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'queen':
#             new_piece = Queen(row, col, WHITE)
#             return new_piece

#         elif piece_type == 'rook':
#             new_piece = Rook(row, col, WHITE)
#             return new_piece

def get_row_col_from_mouse(pos):    #pos e' un tuple
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()

    game = Game(window)

    while run:
        clock.tick(FPS)

        if game.promotion() != False:
            print("promotion!")
            old_piece, row, col = game.promotion()
            window2 = create_window()
            window2.mainloop()
            new_piece = promotion_selection(row, col)
            game.replace_piece(old_piece, new_piece)

        if game.winner():
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

    pygame.quit()

main()