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
        self.move_path = []


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
    

    def deselect(self):
        self.selected_piece.deselect()
        self.selected_piece = None
 

    def can_move(self, row, column):
        # check if the selected piece can move to the selected position
        new_position = self.board.get_piece(row, column)
        # check if there is a selected piece, the selected positon is empty and the move is valid
        if self.selected_piece and new_position == 0 and (row, column) in self.possible_moves:
            jump_path = self.possible_moves[(row, column)]
            self.move_path.append((row, column))
            if len(jump_path) > 1:
                for i in range(len(jump_path) - 1, 0, -1):
                    r0, c0 = self.move_path[0]  
                    r1, c1 = jump_path[i]
                    move_direction = (r1 - r0, c1 - c0)
                    step_size = 2
                    new_row = r0 + move_direction[0] * step_size
                    new_column = c0 + move_direction[1] * step_size
                    self.move_path.insert(0, (new_row, new_column))
            # remove the selected piece from the board before the move
            self.board.board[self.selected_piece.row][self.selected_piece.column] = 0
            return True
        return False


    def move(self, row, column):
        # get the captured pieces list from the possible moves
        captured_pieces = self.possible_moves[(row, column)]
        # move the current piece on the board
        self.board.move(self.selected_piece, row, column)
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
        # reset the  move path
        self.move_path = []


    def render_animation(self, x, y, next_x, next_y):
        radius = SQUARE_SIZE // 2 - self.selected_piece.margin
        if next_x > x and next_y > y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x + 1, y + 1            
        elif next_x > x and next_y < y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x + 1, y - 1
        elif next_x < x and next_y > y:
            pygame.draw.circle(
                self.surface, GREY, (x, y), radius + self.selected_piece.border)
            pygame.draw.circle(
                self.surface, self.turn, (x, y), radius)
            if self.selected_piece.is_king:
                self.surface.blit(
                    CROWN, (x - CROWN.get_width() // 2, y - CROWN.get_height() // 2))
            return x - 1, y + 1
        elif next_x < x and next_y < y:
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
        # draw a semiopaque piece where the selected piece can move
        if self.selected_piece and not self.move_path:
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
    

    def show_winner(self, surface, winner):
        font = pygame.font.SysFont("arialblack", 38)
        white_text = font.render(f"Winner: {winner}", True, (0, 0, 0))
        white_text_width = white_text.get_width()
        x_white = (surface.get_width() - white_text_width) // 2
        surface.blit(white_text, ((x_white, surface.get_height()//2 + 320)))
        

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


    def get_board(self):
        return self.board
    

    def ai_move(self, new_board):
        new_row = 0
        new_column = 0
        for row in range(8):
            for column in range(8):
                if new_board.board[row][column] == 0 and self.board.board[row][column] != 0:
                    self.select(row, column)
                if new_board.board[row][column] != 0 and self.board.board[row][column] == 0:
                   new_row = row
                   new_column = column
        self.can_move(new_row, new_column)