import pygame

WIDTH, HEIGHT = 800, 800

ROWS, COLS = 8, 8

SQUARE_SIZE = WIDTH//COLS #100

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
IVORY = (231, 232, 227)
BLACKISH_BLUE = (30, 29, 35)
BROWN = (177,123,88)
BEIGE = (231,215,204)

WHITE_PAWN = pygame.transform.scale(pygame.image.load('pawn_white.png'), (60, 70))
WHITE_HORSE = pygame.transform.scale(pygame.image.load('horse_white.png'), (60, 70))
WHITE_BISHOP = pygame.transform.scale(pygame.image.load('bishop_white.png'), (60, 70))
WHITE_ROOK = pygame.transform.scale(pygame.image.load('rook_white.png'), (60, 70))
WHITE_KING = pygame.transform.scale(pygame.image.load('king_white.png'), (60, 70))
WHITE_QUEEN = pygame.transform.scale(pygame.image.load('queen_white.png'), (60, 70))

BLACK_PAWN = pygame.transform.scale(pygame.image.load('pawn_black.png'), (60, 70))
BLACK_HORSE = pygame.transform.scale(pygame.image.load('horse_black.png'), (60, 70))
BLACK_BISHOP = pygame.transform.scale(pygame.image.load('bishop_black.png'), (60, 70))
BLACK_ROOK = pygame.transform.scale(pygame.image.load('rook_black.png'), (60, 70))
BLACK_KING = pygame.transform.scale(pygame.image.load('king_black.png'), (60, 70))
BLACK_QUEEN = pygame.transform.scale(pygame.image.load('queen_black.png'), (60, 70))