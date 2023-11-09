from copy import deepcopy
import pygame
from components.const import BLACK, WHITE


def ai_algorithm(board, depth, max_player, game):
    if depth == 0 or board.check_if_winner() != None:
        return board.evaluate(), board
    
    if max_player:
        max_evaluation = float('-inf')
        best_move = None
        for move in get_all_moves(board, BLACK, game):
            evaluation = ai_algorithm(move, depth-1, False, game)[0]
            max_evaluation = max(max_evaluation, evaluation)
            if max_evaluation == evaluation:
                best_move = move
    
        return max_evaluation, best_move
    else:
        min_evaluation = float('inf')
        best_move = None
        for move in get_all_moves(board, WHITE, game):
            evaluation = ai_algorithm(move, depth-1, True, game)[0]
            min_evaluation = min(min_evaluation, evaluation)
            if min_evaluation == evaluation:
                best_move = move
        
        return min_evaluation, best_move


def simulate_move(piece, move, board, captured_pieces):
    board.move(piece, move[0], move[1])
    if captured_pieces:
        board.remove(captured_pieces)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_possible_moves(piece)
        for move, captured_pieces in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.column)
            new_board = simulate_move(temp_piece, move, temp_board, captured_pieces)
            moves.append(new_board)
    
    return moves


