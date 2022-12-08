import customtkinter
from PIL import Image,ImageTk
from constants import WHITE, BLACK
from pawn import Pawn
from horse import Horse
from bishop import Bishop
from rook import Rook
from queen import Queen


class Promozione(customtkinter.CTk):
    def __init__(self,row,col,color):
        super().__init__()
        self.piece_color = None
        self.piece_type = None
        self.row = row
        self.col = col
        self.color = color

        self.title("Promotion : choose a new piece")
        self.geometry("400x100")
        self.resizable(False, False)
        
        self.create_buttons()

    def create_buttons(self):
        frame = customtkinter.CTkFrame(master=self)
        frame.pack()

        if self.color == WHITE:

            #white horse
            photo1 = ImageTk.PhotoImage(Image.open('horse_white.png'))
            horse_white = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image=photo1, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('horse', 'white'))

            horse_white.grid(row=0,column=0)
            
            #white bishop
            photo2 = ImageTk.PhotoImage(Image.open('bishop_white.png'))
            bishop_white = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image= photo2, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('bishop', 'white'))

            bishop_white.grid(row=0, column=1)

            #white rook
            photo3 = ImageTk.PhotoImage(Image.open('rook_white.png'))
            rook_white = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image= photo3, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('rook', 'white'))

            rook_white.grid(row=0, column=2)

            #white queen
            photo4 = ImageTk.PhotoImage(Image.open('queen_white.png'))
            queen_white = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image= photo4, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('queen', 'white'))

            queen_white.grid(row=0, column=3)

        else:

            #black horse
            photo5 = ImageTk.PhotoImage(Image.open('horse_black.png'))
            horse_black = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image=photo5, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('horse', 'black'))

            horse_black.grid(row=0, column=0)

            #black bishop
            photo6 = ImageTk.PhotoImage(Image.open('bishop_black.png'))
            bishop_black = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image=photo6, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('bishop', 'black'))

            bishop_black.grid(row=0, column=1)

            #black rook
            photo7 = ImageTk.PhotoImage(Image.open('rook_black.png'))
            rook_black = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image=photo7, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('rook', 'black'))

            rook_black.grid(row=0, column=2)

            #black queen
            photo8 = ImageTk.PhotoImage(Image.open('queen_black.png'))
            queen_black = customtkinter.CTkButton(master=frame, height=100, width=100, hover_color='white', image=photo8, text="", border_width=2, border_color='black',
                                                command= lambda: self.click('queen', 'black'))

            queen_black.grid(row=0, column=3)

    def click(self, type, color):

        self.piece_type = type
        self.piece_color = color
        print(type)
        print(color)
        self.destroy()

    def promotion_selection(self):

        if self.piece_color == 'white':

            if self.piece_type == 'pawn':
                new_piece = Pawn(self.row, self.col, WHITE)
                return new_piece

            elif self.piece_type == 'horse':
                new_piece = Horse(self.row, self.col, WHITE)
                return new_piece

            elif self.piece_type == 'bishop':
                new_piece = Bishop(self.row, self.col, WHITE)
                return new_piece

            elif self.piece_type == 'queen':
                new_piece = Queen(self.row, self.col, WHITE)
                return new_piece

            elif self.piece_type == 'rook':
                new_piece = Rook(self.row, self.col, WHITE)
                return new_piece

        elif self.piece_color == 'black':

            if self.piece_type == 'pawn':
                new_piece = Pawn(self.row, self.col, BLACK)
                return new_piece

            elif self.piece_type == 'horse':
                new_piece = Horse(self.row, self.col, BLACK)
                return new_piece

            elif self.piece_type == 'bishop':
                new_piece = Bishop(self.row, self.col, BLACK)
                return new_piece

            elif self.piece_type == 'queen':
                new_piece = Queen(self.row, self.col, BLACK)
                return new_piece

            elif self.piece_type == 'rook':
                new_piece = Rook(self.row, self.col, BLACK)
                return new_piece

        return None

# def main():
#     window = Promozione(2,0, WHITE)
#     window.mainloop()

# main()