EMPTY = " "

class Board:
    def __init__(self):
        self.cells = [EMPTY] * 9

    def print_board(self):
        for i in range(3):
            print(" | ".join(self.cells[i*3:(i+1)*3]))
            if i < 2:
                print("--+---+--")

    def legal_moves(self):
        return [i for i, v in enumerate(self.cells) if v == EMPTY]

    def is_full(self):
        return all(c != EMPTY for c in self.cells)

    def winner(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in wins:
            if self.cells[a] != EMPTY and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_game_over(self):
        return self.winner() is not None or self.is_full()


# ---------------- AI Logic (Minimax) ---------------- #

def minimax(board, is_maximizing, ai_symbol, human_symbol):
    winner = board.winner()
    if winner == ai_symbol:
        return 1
    elif winner == human_symbol:
        return -1
    elif board.is_full():
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in board.legal_moves():
            board.cells[move] = ai_symbol
            score = minimax(board, False, ai_symbol, human_symbol)
            board.cells[move] = EMPTY
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in board.legal_moves():
            board.cells[move] = human_symbol
            score = minimax(board, True, ai_symbol, human_symbol)
            board.cells[move] = EMPTY
            best_score = min(best_score, score)
        return best_score


def ai_move(board, ai_symbol, human_symbol):
    """Return the best move for AI using the minimax algorithm."""
    best_score = -float('inf')
    move = None
    for m in board.legal_moves():
        board.cells[m] = ai_symbol
        score = minimax(board, False, ai_symbol, human_symbol)
        board.cells[m] = EMPTY
        if score > best_score:
            best_score = score
            move = m
    return move
