from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm

class NQueensController:
    def __init__(self, n):
        self.n = n

    def set_n(self, n):
        self.n = n

    def run_backtracking_algorithm(self):
        solver = BacktrackingAlgorithm(self.n)
        return solver.all_solutions()

    def run_genetic_algorithm(self):
        genetic = GeneticAlgorithm(self.n)
        return genetic.run_evolution()

    def run_csp_algorithm(self):
        pass
        return true
