import pygame
from constants import WIDTH, HEIGHT, SQUARE_SIZE
from game import Game
from promotion import Promotion

FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

def get_row_col_from_mouse(pos):    
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
            #print("promotion!")
            old_piece, row, col = game.promotion()
            window2 = Promotion(row, col, old_piece.color)
            window2.mainloop()
            new_piece = window2.promotion_selection() 
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