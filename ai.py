from game import Board, EMPTY

def minimax(board, player, ai_player):
    winner = board.winner()
    if winner == ai_player:
        return 1, None
    elif winner is not None:
        return -1, None
    elif board.is_full():
        return 0, None

    best_move = None
    if player == ai_player:
        best_score = -10
        for move in board.legal_moves():
            b = Board()
            b.cells = board.cells.copy()
            b.cells[move] = player
            score, _ = minimax(b, 'O' if player == 'X' else 'X', ai_player)
            if score > best_score:
                best_score, best_move = score, move
        return best_score, best_move
    else:
        best_score = 10
        for move in board.legal_moves():
            b = Board()
            b.cells = board.cells.copy()
            b.cells[move] = player
            score, _ = minimax(b, 'O' if player == 'X' else 'X', ai_player)
            if score < best_score:
                best_score, best_move = score, move
        return best_score, best_move
