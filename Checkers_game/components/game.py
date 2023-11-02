import pygame
from .const import WHITE, BLACK, BLUE, SQUARE_SIZE
from components.board import Board

class Game:

    def __init__(self, surface):
        self._init()
        self.surface = surface


    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = WHITE
        self.turn_nr = 1
        self.possible_moves = {}


    def select(self, row, column):
        if self.selected_piece:
            result = self._move(row, column, self.turn_nr)
            if not result:
                self.selected_piece.deselect()
                self.selected_piece = None
                self.select(row, column)
    
        piece = self.board.get_piece(row, column)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.possible_moves = self.board.get_possible_moves(piece)
            piece.select()
            return True

        return False
 

    def _move(self, row, column, turn_nr):
        piece = self.board.get_piece(row, column)

        if self.selected_piece and piece == 0 and (row, column) in self.possible_moves:
            jumped_pieces = self.possible_moves[(row, column)]
            self.selected_piece.deselect()
            self.board.move(self.selected_piece, row, column, turn_nr, jumped_pieces)
            print("Captured pieces:", jumped_pieces)
            if jumped_pieces:
                self.board.erase_jumped_pieces(jumped_pieces)
            # self.board.update_last_move(self.turn)
            print("Turn nr:", self.turn_nr)
            print("Remaining black pieces:", self.board.black_pieces_left)
            print("Remaining white pieces:", self.board.white_pieces_left)
            print("Black kings:", self.board.black_kings)
            print("White kings:", self.board.white_kings)
            self.change_player_turn()
        else:
            return False

        return True


    def get_all_possible_moves(self, board, color):
        possible_moves = {}
        for piece in board.get_all_pieces(color):
            possible_moves.update(board.get_possible_moves(piece))
        return possible_moves


    def draw_possible_moves(self, possible_moves):
        if self.selected_piece:
            for move in possible_moves:
                row, column = move
                pygame.draw.circle(self.surface, BLUE, (column * SQUARE_SIZE + SQUARE_SIZE // 2,
                                                        row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)


    def has_won(self):
        return self.board.check_has_won()


    def update(self, surface):
            self.board.draw_board(surface)
            self.draw_possible_moves(self.possible_moves)
            pygame.display.update()


    def change_player_turn(self):
        self.possible_moves = {}
        self.turn_nr += 1
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

 
    def reset(self):
            self._init()



