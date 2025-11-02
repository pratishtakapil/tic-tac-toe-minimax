from game import Board
from ai import minimax

def play():
    board = Board()
    human = input("Choose your symbol (X or O): ").upper()
    ai = 'O' if human == 'X' else 'X'
    turn = 'X'

    while True:
        board.print_board()
        if board.winner() or board.is_full():
            w = board.winner()
            print("Winner:", w if w else "Draw!")
            break

        if turn == human:
            move = int(input("Enter your move (0-8): "))
            if move in board.legal_moves():
                board.cells[move] = human
                turn = ai
        else:
            _, move = minimax(board, ai, ai)
            board.cells[move] = ai
            print(f"AI plays {move}")
            turn = human

if __name__ == "__main__":
    play()
