import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
FPS = 120
WIDTH, HEIGHT = 600, 600
ROWS, COLUMNS = 8, 8
SQUARE_SIZE = WIDTH // COLUMNS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CREAM = (250, 233, 218)
GREY = (128, 128, 128)
BROWN = (124, 81, 43)

CROWN = pygame.transform.scale(pygame.image.load("images/crown.png"), (44, 25))
