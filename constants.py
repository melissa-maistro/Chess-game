import pygame

WIDTH, HEIGHT = 500, 500

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH//COLS 

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BROWN = (177,123,88)
BEIGE = (231,215,204)

WHITE_PAWN = pygame.transform.scale(pygame.image.load('images/pawn_white.png'), (60, 70))
WHITE_HORSE = pygame.transform.scale(pygame.image.load('images/horse_white.png'), (60, 70))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('images/bishop_white.png'), (60, 70))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('images/rook_white.png'), (60, 70))
WHITE_KING = pygame.transform.scale(pygame.image.load('images/king_white.png'), (60, 70))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('images/queen_white.png'), (60, 70))

BLACK_PAWN = pygame.transform.scale(pygame.image.load('images/pawn_black.png'), (60, 70))
BLACK_HORSE = pygame.transform.scale(pygame.image.load('images/horse_black.png'), (60, 70))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('images/bishop_black.png'), (60, 70))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('images/rook_black.png'), (60, 70))
BLACK_KING = pygame.transform.scale(pygame.image.load('images/king_black.png'), (60, 70))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('images/queen_black.png'), (60, 70))