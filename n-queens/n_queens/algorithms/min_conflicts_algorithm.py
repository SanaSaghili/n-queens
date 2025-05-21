import random

class MinConflictsAlgorithm:

    def __init__(self, n, max_tries=10000):
        self.n = n
        self.max_tries = max_tries
        self.found = []


    def create__board(self):
        board = []
        for _ in range(self.n):
            board.append(random.randint(0, self.n - 1))
        return board


    def count_conflicts(self, board, row, col):
        count = 0
        for i in range(self.n):
            if i != col:
                if board[i] == row or abs(board[i] - row) == abs(i - col):
                    count += 1
        return count


    def conflicted_columns(self, board):
        cols = []
        for col in range(self.n):
            if self.count_conflicts(board, board[col], col) > 0:
                cols.append(col)
        return cols


    def run(self):
        board = self.create__board()

        for _ in range(self.max_tries):
            bad_cols = self.conflicted_columns(board)

            if not bad_cols:
                sol = tuple(board)
                if sol not in self.found:
                    self.found.append(sol)
                if len(self.found) >= 5:
                    break
                board = self.create__board()
                continue

            col = random.choice(bad_cols)
            min_conf = self.n
            best_rows = []

            for row in range(self.n):
                c = self.count_conflicts(board, row, col)
                if c < min_conf:
                    min_conf = c
                    best_rows = [row]
                elif c == min_conf:
                    best_rows.append(row)

            board[col] = random.choice(best_rows)

        return [list(sol) for sol in self.found]
