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

    def winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.cells[a] != EMPTY and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_full(self):
        return all(c != EMPTY for c in self.cells)
