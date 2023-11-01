import pygame
from .const import CREAM, BLACK, WHITE, BROWN, SQARE_SIZE, ROWS, COLUMNS
from .piece import Piece
# import csv
# import os

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
                        self.board[row].append(Piece(row, column, CREAM))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def draw_board_sqaures(self, surface):
        surface.fill(CREAM)
        for row in range(ROWS):
            for column in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(surface, BROWN, (row * SQARE_SIZE, column * SQARE_SIZE,
                                             SQARE_SIZE, SQARE_SIZE))


    def draw_board(self, surface):
        self.draw_board_sqaures(surface)
        for row in range(ROWS):
            for column in range(COLUMNS):
                Piece = self.board[row][column]
                if Piece != 0:
                    Piece.draw_piece(surface)


    def move(self, Piece, row, column, turn_nr, jumped_Pieces):
        if jumped_Pieces:
            jumped_Pieces_moves = ""
            for jumped_Piece in jumped_Pieces:
                jumped_Pieces_moves += str(jumped_Piece)
            move = str(turn_nr) + ". " + str((Piece.row, Piece.column)) + "-" +\
                     str(jumped_Pieces_moves) + "-" + str((row, column))
        else:
            move = str(turn_nr) + ". " + str((Piece.row, Piece.column)) + "-" + str((row, column))

        self.moves.append(move)
        print("Moves:", self.moves)
        self.board[Piece.row][Piece.column], self.board[row][column] = self.board[row][column], \
                                                                           self.board[Piece.row][Piece.column]
        Piece.move(row, column)
        Piece.last_moved()

        if (row == ROWS - 1 or row == 0) and not Piece.is_king:
            Piece.make_king()
            if Piece.color == CREAM:
                self.white_kings += 1
            else:
                self.black_kings += 1


    def update_last_move(self, color):
        for row in range(ROWS):
            for column in range(COLUMNS):
                if self.board[row][column] != 0:
                    if color == CREAM:
                        if self.board[row][column].last_piece_moved and self.board[row][column].color == BLACK:
                            self.board[row][column].last_piece_moved = False
                    elif color == BLACK:
                        if self.board[row][column].last_piece_moved and self.board[row][column].color == CREAM:
                            self.board[row][column].last_piece_moved = False


    def erase_jumped_Pieces(self, jumped_Pieces):
        for jumped_Piece in jumped_Pieces:
            Piece = self.board[jumped_Piece[0]][jumped_Piece[1]]
            self.board[jumped_Piece[0]][jumped_Piece[1]] = 0
            if Piece != 0:
                if Piece.color == BLACK:
                    self.black_pieces_left -= 1
                    if Piece.is_king:
                        self.black_kings -= 1
                elif Piece.color == CREAM:
                    self.white_pieces_left -= 1
                    if Piece.is_king:
                        self.white_kings -= 1


    def check_if_winner(self):
        if self.black_pieces_left <= 0:
            return CREAM
        elif self.white_pieces_left <= 0:
            return BLACK

        return None


    def get_piece(self, row, column):
        return self.board[row][column]


    def get_all_pieces(self, color):
        piese = []
        for row in self.board:
            for Piece in row:
                if Piece != 0 and Piece.color == color:
                    piese.append(Piece)

        return piese


    def get_possible_moves(self, Piece):
        moves = {}
        jump_path = []
        row = Piece.row
        column = Piece.column

        moves.update(self._get_possible_moves(Piece, row, column, jump_path, 1))
        moves.update(self._get_possible_moves(Piece, row, column, jump_path, 2))

        return moves


    def _get_possible_moves(self, Piece, row, column, jump_path, step_size):
        ''' This method takes in a row and col of where the piece is currently during the jump. It also takes a jump_path so a king does not jump back to where it came from and to prevent jumping over the same piece twice.
        Finally a step_size is provided: if it's 1 only short jumps are considered, if 2 then jump chains are considered
        '''
        up, down, left, right = [x + y * step_size for x in [row, column] for y in [-1, 1]]
        moves = {}
        for new_column in [left, right]:
            for new_row in [up, down]:
                    if not self.can_move(Piece, row, column, new_row, new_column, step_size):
                        continue
                    if step_size == 1:
                        moves[new_row, new_column] = []
                    elif step_size == 2:
                        jumped_row = (new_row + row) // 2
                        jumped_column = (new_column + column) // 2
                        if (jumped_row, jumped_column) in jump_path:
                            continue
                        new_jump_path = jump_path.copy()
                        new_jump_path.append((jumped_row, jumped_column))
                        moves[(new_row, new_column)] = new_jump_path
                        # recursive call
                        moves.update(self._get_possible_moves(Piece, new_row, new_column, new_jump_path, step_size))

        return moves


    def can_move(self, Piece, old_row, old_column, new_row, new_column, step_size):
        '''Evaluates to True if boundaries are right and if current piece between start/end location is of different color
        '''
        if not (Piece.is_king or new_row == old_row + Piece.get_move_direction() * step_size):
            # invalid direction
            return False
        if not (0 <= new_row < ROWS and 0 <= new_column < COLUMNS):
            # outside of board
            return False
        new_location = self.get_Piece(new_row, new_column)
        if new_location != 0:
            # jump location not empty
            return False
        # all base obstacles have been overcome
        if step_size == 2:
            jumped_row = (old_row + new_row) // 2
            jumped_column = (old_column + new_column) // 2
            jumped_Piece = self.get_piece(jumped_row, jumped_column)
            if jumped_Piece == 0 or jumped_Piece.color == Piece.color:
                return False

        return True



