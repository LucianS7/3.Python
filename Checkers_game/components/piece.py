import pygame
from .const import CREAM, BLACK, GREY, SQARE_SIZE, CROWN

class Piece:
    MARGIN = 10
    BORDER = 2

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.is_king = False
        self.x = 0
        self.y = 0
        self.get_position()
        self.last_piece_moved = False


    def __repr__(self):
        return str(self.color)


    def get_position(self):
        self.x = SQARE_SIZE * self.column + SQARE_SIZE // 2
        self.y = SQARE_SIZE * self.row + SQARE_SIZE // 2


    def draw_piece(self, surface):
        radius = SQARE_SIZE // 2 - self.MARGIN
        pygame.draw.circle(surface, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(surface, self.color, (self.x, self.y), radius)

        if self.is_king:
            surface.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

        if self.last_piece_moved:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self.x - SQARE_SIZE / 2, self.y - SQARE_SIZE / 2, 
                                                           SQARE_SIZE, SQARE_SIZE), 3)


    def move(self, row, column):
        self.row = row
        self.column = column
        self.get_position()


    def get_move_direction(self):
        if self.color == CREAM:
            return -1
        elif self.color == BLACK:
            return 1


    def last_moved(self):
        self.last_piece_moved = True

        
    def make_king(self):
        self.is_king = True


