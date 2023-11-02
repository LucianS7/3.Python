import pygame
from .const import WHITE, BLACK, GREY, SQUARE_SIZE, CROWN

class Piece:
    MARGIN = 10
    BORDER = 2

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.is_king = False
        self.x, self.y = self.get_position()
        self.is_selected = False


    def __repr__(self):
        if self.color == WHITE:
            return str("White")
        elif self.color == BLACK:
            return str("Black")


    def get_position(self):
        x = SQUARE_SIZE * self.column + SQUARE_SIZE // 2
        y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        return x, y


    def draw_piece(self, surface):
        radius = SQUARE_SIZE // 2 - self.MARGIN
        pygame.draw.circle(surface, GREY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(surface, self.color, (self.x, self.y), radius)

        if self.is_king:
            surface.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

        if self.is_selected:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(self.x - SQUARE_SIZE / 2, self.y - SQUARE_SIZE / 2, 
                                                           SQUARE_SIZE, SQUARE_SIZE), 3)


    def move(self, row, column):
        self.row = row
        self.column = column
        self.x, self.y = self.get_position()


    def get_move_direction(self):
        if self.color == WHITE:
            return 1
        elif self.color == BLACK:
            return -1


    def select(self):
        self.is_selected = True

    def deselect(self):
        self.is_selected = False


        
    def make_king(self):
        self.is_king = True


