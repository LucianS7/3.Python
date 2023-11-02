import pygame
from .const import CREAM, WHITE, BLACK, BROWN, SQUARE_SIZE, ROWS, COLUMNS
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
                        self.board[row].append(Piece(row, column, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, column, BLACK))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def draw_board_sqaures(self, surface):
        surface.fill(CREAM)
        for row in range(ROWS):
            for column in range((row+1) % 2, COLUMNS, 2):
                pygame.draw.rect(surface, BROWN, (row * SQUARE_SIZE, column * SQUARE_SIZE,
                                             SQUARE_SIZE, SQUARE_SIZE))


    def draw_board(self, surface):
        self.draw_board_sqaures(surface)
        for row in range(ROWS):
            for column in range(COLUMNS):
                piece = self.board[row][column]
                if piece != 0:
                    piece.draw_piece(surface)


    def move(self, piece, row, column, turn_nr, jumped_pieces):
        if jumped_pieces:
            jumped_pieces_moves = ""
            for jumped_piece in jumped_pieces:
                jumped_pieces_moves += str(jumped_piece)
            move = str(turn_nr) + ". " + str((piece.row, piece.column)) + "-" +\
                     str(jumped_pieces_moves) + "-" + str((row, column))
        else:
            move = str(turn_nr) + ". " + str((piece.row, piece.column)) + "-" + str((row, column))

        self.moves.append(move)
        print("Moves:", self.moves)
        self.board[piece.row][piece.column], self.board[row][column] = self.board[row][column], \
                                                                           self.board[piece.row][piece.column]
        piece.move(row, column)
        if (row == ROWS - 1 or row == 0) and not piece.is_king:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1


    def erase_jumped_pieces(self, jumped_pieces):
        for jumped_piece in jumped_pieces:
            piece = self.board[jumped_piece[0]][jumped_piece[1]]
            self.board[jumped_piece[0]][jumped_piece[1]] = 0
            if piece != 0:
                if piece.color == BLACK:
                    self.black_pieces_left -= 1
                    if piece.is_king:
                        self.black_kings -= 1
                elif piece.color == WHITE:
                    self.white_pieces_left -= 1
                    if piece.is_king:
                        self.white_kings -= 1


    def check_has_won(self):
        if self.black_pieces_left <= 0:
            return "White Player"
        elif self.white_pieces_left <= 0:
            return "Black Player"

        return None


    def get_piece(self, row, column):
        return self.board[row][column]


    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
 
        return pieces


    def get_possible_moves(self, piece):
        moves = {}
        jump_path = []
        row = piece.row
        column = piece.column

        moves.update(self._get_possible_moves(piece, row, column, jump_path, 1))
        moves.update(self._get_possible_moves(piece, row, column, jump_path, 2))

        return moves


    def _get_possible_moves(self, piece, row, column, jump_path, step_size):
        ''' This method takes in a row and col of where the piece is currently during the jump. It also takes a jump_path so a king does not jump back to where it came from and to prevent jumping over the same piece twice.
        Finally a step_size is provided: if it's 1 only short jumps are considered, if 2 then jump chains are considered
        '''
        up, down, left, right = [x + y * step_size for x in [row, column] for y in [-1, 1]]
        moves = {}
        for new_column in [left, right]:
            for new_row in [up, down]:
                    if not self.can_move(piece, row, column, new_row, new_column, step_size):
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
                        moves.update(self._get_possible_moves(piece, new_row, new_column, new_jump_path, step_size))

        return moves


    def can_move(self, piece, old_row, old_column, new_row, new_column, step_size):
        '''Evaluates to True if boundaries are right and if current piece between start/end location is of different color
        '''

#       print (old_row, old_column, "->", new_row, new_column)
        if not (piece.is_king or new_row == old_row + piece.get_move_direction() * step_size):
            # invalid direction
            return False
        if not (0 <= new_row < ROWS and 0 <= new_column < COLUMNS):
            # outside of board
            return False
        new_location = self.get_piece(new_row, new_column)
        if new_location != 0:
            # jump location not empty
            return False
        # all base obstacles have been overcome
        if step_size == 2:
            jumped_row = (old_row + new_row) // 2
            jumped_column = (old_column + new_column) // 2
            jumped_piece = self.get_piece(jumped_row, jumped_column)
            if jumped_piece == 0 or jumped_piece.color == piece.color:
                return False
            
        return True



    # def update_last_move(self, color):
    #     for row in range(ROWS):
    #         for column in range(COLUMNS):
    #             if self.board[row][column] != 0:
    #                 if color == WHITE:
    #                     if self.board[row][column].last_piece_moved and self.board[row][column].color == BLACK:
    #                         self.board[row][column].last_piece_moved = False
    #                 elif color == BLACK:
    #                     if self.board[row][column].last_piece_moved and self.board[row][column].color == WHITE:
    #                         self.board[row][column].last_piece_moved = False