class BacktrackingAlgorithm:
    def __init__(self, n):
        self.size = n
        self.find_solution = []

    def check(self, rows, columns, temp):
        for row in range(rows):
            if temp[row] == columns or abs(temp[row] - columns) == abs(row - rows):
                return False
        return True

    def find(self, row, temp):
        if row == self.size:
            self.find_solution.append(temp[:])
            return
        for c in range(self.size):
            if self.check(row, c, temp):
                temp[row] = c
                self.find(row + 1, temp)
                temp[row] = -1

    def all_solutions(self):
        temp = [-1] * self.size
        self.find(0, temp)
        return self.find_solution


