import math
from game import Board

def minimax(board, player, ai_player):
    winner = board.winner()
    if winner == ai_player:
        return 1, None
    elif winner and winner != ai_player:
        return -1, None
    elif board.is_full():
        return 0, None

    if player == ai_player:
        best_value = -math.inf
        best_move = None
        for move in board.legal_moves():
            new_board = Board()
            new_board.cells = board.cells[:]
            new_board.make_move(move, player)
            value, _ = minimax(new_board, get_opponent(player), ai_player)
            if value > best_value:
                best_value = value
                best_move = move
        return best_value, best_move
    else:
        best_value = math.inf
        best_move = None
        for move in board.legal_moves():
            new_board = Board()
            new_board.cells = board.cells[:]
            new_board.make_move(move, player)
            value, _ = minimax(new_board, get_opponent(player), ai_player)
            if value < best_value:
                best_value = value
                best_move = move
        return best_value, best_move

def get_opponent(player):
    return "O" if player == "X" else "X"

def best_move(board, ai_player):
    _, move = minimax(board, ai_player, ai_player)
    return move
