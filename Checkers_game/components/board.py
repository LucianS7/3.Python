import pygame
from .const import WHITE, BLACK, CREAM, BROWN, SQUARE_SIZE, ROWS, COLUMNS
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.black_pieces_left = 12
        self.white_pieces_left = 12
        self.black_kings = 0
        self.white_kings = 0
        self.create_board_matrix()
        self.moves = []


    def create_board_matrix(self):
        for row in range(ROWS):
            self.board.append([])
            for column in range(COLUMNS):
                if column % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, column, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def draw_board_squares(self, surface):
        surface.fill(CREAM)
        for row in range(ROWS):
            for column in range((row+1) % 2, COLUMNS, 2):
                pygame.draw.rect(surface, BROWN, (row * SQUARE_SIZE, column * SQUARE_SIZE,
                                             SQUARE_SIZE, SQUARE_SIZE))


    def draw_board(self, surface):
        self.draw_board_squares(surface)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw_piece(surface)


    def get_piece(self, row, column):
        return self.board[row][column]
    

    def get_all_pieces(self, color):
        # get a list of all pieces of a player
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
 
        return pieces
    

    def check_if_winner(self):
        # check if there is a winner
        if self.black_pieces_left <= 0:
            return "White Player"
        elif self.white_pieces_left <= 0:
            return "Black Player"

        return None


    def get_possible_moves(self, piece):
        possible_moves = {}
        jump_path = []
        row = piece.row
        column = piece.column
        # get all possible moves for small jumps
        possible_moves.update(self._get_possible_moves(piece, row, column, 1))
        # get all possible moves for big jumps over oponents pieces or jump chains
        possible_moves.update(self._get_possible_moves(piece, row, column, 2, jump_path))

        return possible_moves
    

    def _get_possible_moves(self, piece, row, column, step_size, jump_path=[]):
        # first will get the new possible rows and columns based on the current piece position
        up, down, left, right = [x + y * step_size for x in [row, column] for y in [-1, 1]]
        possible_moves = {}
        # for every possible new location will check if the move is valid
        for new_column in [left, right]:
            for new_row in [up, down]:
                    # check to see if move is valid
                    if not self.valid_move(piece, row, column, new_row, new_column, step_size):
                        continue
                    # add the move to the moves dictionary for small jumps
                    if step_size == 1:
                        possible_moves[(new_row, new_column)] = []
                    elif step_size == 2:
                        jumped_row = (new_row + row) // 2
                        jumped_column = (new_column + column) // 2
                        # check if same piece is jumped more than once
                        if (jumped_row, jumped_column) in jump_path:
                            continue
                        new_jump_path = jump_path.copy()
                        new_jump_path.append((jumped_row, jumped_column))
                        # add the move and the jump path to the moves dictionary
                        possible_moves[(new_row, new_column)] = new_jump_path
                        # recursive call to check again the possible moves using the new location
                        possible_moves.update(self._get_possible_moves(piece, new_row, new_column, step_size, new_jump_path))

        return possible_moves


    def valid_move(self, piece, old_row, old_column, new_row, new_column, step_size):
       # check to see if the piece jump direction is valid
        if (piece.is_king or new_row == old_row + piece.get_move_direction() * step_size):
            # check if jump is on board
            if (0 <= new_row < ROWS and 0 <= new_column < COLUMNS):
                new_location = self.get_piece(new_row, new_column)
                # check if new location in empty        
                if new_location == 0:
                    if step_size == 1:
                        return True
                    # check if the jumped square has an opponents piece
                    elif step_size == 2:
                        jumped_row = (old_row + new_row) // 2
                        jumped_column = (old_column + new_column) // 2
                        jumped_piece = self.get_piece(jumped_row, jumped_column)
                        if jumped_piece != 0 and jumped_piece.color != piece.color:
                            return True
        return False


    def move(self, piece, row, column):
        # print the move in the console
        # if turn_nr % 2 == 1:
        #     move = str(turn_nr) + ". " + "White: " + str((piece.row, piece.column)) + " --> " + str((row, column))
        # else:
        #     move = str(turn_nr) + ". " + "Black: " + str((piece.row, piece.column)) + " --> " + str((row, column))
        # print(move)
        # move the piece in the board matrix to the new location
        self.board[row][column] = piece
        # erase the piece from the previus location 
        self.board[piece.row][piece.column] = 0
        # update the moved piece attributes (row, column, x and y)
        piece.update(row, column)
        if (row == 0 or row == ROWS - 1) and not piece.is_king:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1


    def remove(self, pieces):
        # remove the pieces in the pieces list and update the number of pieces for each player
        for row, column in pieces:
            piece = self.board[row][column]
            self.board[row][column] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_pieces_left -= 1
                    if piece.is_king:
                        self.black_kings -= 1
                else:
                    self.white_pieces_left -= 1
                    if piece.is_king:
                        self.white_kings -= 1


    def evaluate(self):
        return self.black_pieces_left - self.white_pieces_left + (self.black_kings * 0.5 - self.white_kings * 0.5)


