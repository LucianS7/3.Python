import pygame
from .const import WHITE, BLACK, GREY, SQUARE_SIZE, WIDTH, CROWN
from .board import Board

class Checkers:

    def __init__(self, surface):
        self._init()
        self.surface = surface


    def _init(self):
        # private initialization function so there is no need to create a new Checkers_game object
        self.selected_piece = None
        self.board = Board()
        self.turn = WHITE
        self.turn_nr = 1
        self.possible_moves = {}


    def update(self, surface):
        # update the game by redrawing the board and the possible moves
        self.board.draw_board(surface)
        self.draw_possible_moves(self.possible_moves)
        pygame.display.flip()


    def reset(self):
        # reset the game by calling the private _init function to reset the board
        self._init()


    def get_row_and_column(self, position):
        # get the clicked row and column
        x, y = position
        row = y // SQUARE_SIZE
        column = x // SQUARE_SIZE
        return row, column
    

    def get_center_of_square(self, row, column):
        x = SQUARE_SIZE * column + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + SQUARE_SIZE // 2
        return x, y


    def select(self, row, column):
        # check if the selected square has a current player piece
        piece = self.board.get_piece(row, column)
        if piece != 0 and piece.color == self.turn:
            # select the current piece
            self.selected_piece = piece
            # get the valid moves of the selected piece
            self.possible_moves = self.board.get_possible_moves(piece)
            # draw a light green rectangle around the selected piece
            piece.select()
            return True

        return False
 
    def can_move(self, row, column):
        # check if the selected piece can move to the selected position
        new_position = self.board.get_piece(row, column)
        # check if there is a selected piece, the selected positon is empty and the move is valid
        if self.selected_piece and new_position == 0 and (row, column) in self.possible_moves:
            self.board.board[self.selected_piece.row][self.selected_piece.column] = 0
            return True
        return False


    def move(self, row, column):
        # get the captured pieces list from the possible moves
        captured_pieces = self.possible_moves[(row, column)]
        # move the current piece on the board
        self.board.move(self.selected_piece, row, column, self.turn_nr)
        # deselect the moved piece
        self.selected_piece.deselect()
        self.selected_piece = None
        # check if there are captured pieces and print the their location
        if captured_pieces:
            # print("Captured pieces:", captured_pieces)
            self.board.remove(captured_pieces)
            # print the remaining pieces
            # print("Remaining black pieces:", self.board.black_pieces_left)
            # print("Remaining white pieces:", self.board.white_pieces_left)
            # print("Black kings:", self.board.black_kings)
            # print("White kings:", self.board.white_kings)
        # change the player turn
        self.change_player_turn()


    def render_animation(self, x, y, new_x, new_y):
        radius = SQUARE_SIZE // 2 - self.selected_piece.margin
        if new_x > x and new_y > y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x + 1, y + 1            
        elif new_x > x and new_y < y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x + 1, y - 1
        elif new_x < x and new_y > y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x - 1, y + 1
        elif new_x < x and new_y < y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x - 1, y - 1


    def get_all_possible_moves(self, board, color):
        # get all possible moves from the game for the current player 
        player_possible_moves = {}
        for piece in board.get_all_pieces(color):
            player_possible_moves.update(board.get_possible_moves(piece))
        return player_possible_moves


    def draw_possible_moves(self, possible_moves):
        # draw blue dots where the selected piece can move
        if self.selected_piece:
            for move in possible_moves:
                row, column = move
                color = self.turn + (100,)
                semiopaque_surface = pygame.Surface((1024, 768), pygame.SRCALPHA)
                pygame.draw.circle(
                    semiopaque_surface, color, (
                        column * SQUARE_SIZE + SQUARE_SIZE // 2, 
                        row * SQUARE_SIZE + SQUARE_SIZE // 2), 25)
                self.surface.blit(semiopaque_surface, (0, 0))
                

    def has_winner(self):
        return self.board.check_if_winner()


    def change_player_turn(self):
        self.possible_moves = {}
        self.turn_nr += 1
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE


    def draw_captured_pieces(self, surface):
        x = (surface.get_width() - WIDTH) // 2
        y = surface.get_height() // 2
        pygame.draw.circle(surface, BLACK, (x - 50, y + 35), 28)
        pygame.draw.circle(surface, WHITE, (x - 50, y - 35), 28)
        font = pygame.font.SysFont("arialblack", 38)
        white_cp = font.render(f"{12 - self.board.white_pieces_left}", True, (255, 255, 255))
        black_cp = font.render(f"{12 - self.board.black_pieces_left}", True, (0, 0, 0))
        white_text_width = white_cp.get_width()
        black_text_width = black_cp.get_width()
        x_white = x - 50 - white_text_width // 2
        x_black = x - 50 - black_text_width // 2
        surface.blit(white_cp, ((x_white, y + 7)))
        surface.blit(black_cp, ((x_black, y - 63)))


    def draw_player_turn(self, surface):
        x = (surface.get_width() - WIDTH) // 2
        y = surface.get_height() // 2
        if self.turn == WHITE:
            pygame.draw.rect(surface, (220, 220, 220), pygame.Rect((x - 84, y + 2 , 67, 67)), 4) 
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(x - 84, y - 68, 67, 67), 4)
        else:
            pygame.draw.rect(surface, (220, 220, 220), pygame.Rect(x - 84, y - 68, 67, 67), 4)
            pygame.draw.rect(surface, (0, 0, 0), pygame.Rect((x - 84, y + 2 , 67, 67)), 4) 

    def last_piece(self):
        if self.board.white_pieces_left == 1 or self.board.black_pieces_left == 1:
            return True
        return False
      

    # def get_board(self):
    #     return self.board


    # def ai_move(self, board):
    #     self.board = board
    #     self.change_player_turn()

 