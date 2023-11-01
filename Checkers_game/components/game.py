import pygame
from .const import CREAM, BLACK, BLUE, SQARE_SIZE
from components.board import Board

class Game:

    def __init__(self, surface):
        self._init()
        self.surface = surface


    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = CREAM
        self.turn_nr = 1
        self.posible_moves = {}


    def select(self, row, column):
        if self.selected_piece:
            result = self._muta(row, column, self.turn_nr)
            if not result:
                self.selected_piece = None
                self.select(row, column)

        Piece = self.board.get_piece(row, column)
        if Piece != 0 and Piece.color == self.turn:
            self.selected_piece = Piece
            self.posible_moves = self.board.get_posible_moves(Piece)
            return True

        return False
 

    def _move(self, row, column, turn_nr):
        Piece = self.board.get_piece(row, column)
        if self.selected_piece and Piece == 0 and (row, column) in self.posible_moves:
            jumped_pieces = self.posible_moves[(row, column)]
            self.board.move(self.selected_piece, row, column, turn_nr, jumped_pieces)
            print("Captured pieces:", jumped_pieces)
            if jumped_pieces:
                self.board.erase_jumped_Pieces(jumped_pieces)
            self.board.update_last_move(self.turn)
            print("Turn nr:", self.turn_nr)
            print("Remaining black pieces:", self.board.black_pieces_left)
            print("Remaining white pieces:", self.board.white_pieces_left)
            print("Black kings:", self.board.black_kings)
            print("White kings:", self.board.white_kings)
            self.change_player_turn()
        else:
            return False

        return True


    def get_all_posible_moves(self, board, color):
        possible_moves = {}
        for Piece in board.get_all_pieces(color):
            possible_moves.update(board.get_possible_moves(Piece))

        return possible_moves


    def draw_posible_moves(self, posible_moves):
        for move in posible_moves:
            row, column = move
            pygame.draw.circle(self.surface, BLUE, (column * SQARE_SIZE + SQARE_SIZE // 2,
                                                    row * SQARE_SIZE + SQARE_SIZE // 2), 10)


    def is_winner(self):
        return self.board.check_if_winner()



    def update(self, surface):
            self.board.draw(surface)
            self.draw_posible_moves(self.posible_moves)
            pygame.display.update()


    def change_player_turn(self):
        self.possible_moves = {}
        self.turn_nr += 1
        if self.turn == CREAM:
            self.turn = BLACK
        else:
            self.turn = CREAM

 
    def reset(self):
            self._init()



