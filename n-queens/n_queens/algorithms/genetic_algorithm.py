# population_solver.py

import random


class GeneticAlgorithm:
    def __init__(self, n, population=1000, generations=500):
        self.n = n
        self.population = [self.create_chromosome() for _ in range(population)]
        self.generations = generations
        self.optimum_fitness = (n * (n - 1)) // 2
        self.solutions = []

    def create_chromosome(self):
        return [random.randrange(self.n) for _ in range(self.n)]

    def select_parent(self, fitness_scores):
        total = sum(fitness_scores)
        pick = random.uniform(0, total)
        current = 0
        for i, score in enumerate(fitness_scores):
            current += score
            if current >= pick:
                return self.population[i]
        return self.population[0]

    def fitness_check(self, chromosome):
        row_conflict = sum(chromosome.count(g) - 1 for g in chromosome) // 2

        diag1 = {}
        diag2 = {}
        for pos, gene in enumerate(chromosome):
            d1 = pos + gene
            d2 = pos - gene
            diag1[d1] = diag1.get(d1, 0) + 1
            diag2[d2] = diag2.get(d2, 0) + 1

        diag_conflict = 0
        for cnt in diag1.values():
            diag_conflict += max(0, cnt - 1)
        for cnt in diag2.values():
            diag_conflict += max(0, cnt - 1)

        return self.optimum_fitness - (row_conflict + diag_conflict)

    def crossover(self, parent_a, parent_b):
        return [random.choice([a, b]) for a, b in zip(parent_a, parent_b)]

    def mutation(self, chromosome):
        new_chromosome = chromosome.copy()
        idx = random.randrange(self.n)
        new_chromosome[idx] = random.randrange(self.n)
        return new_chromosome

    def run_evolution(self):
        elite_count = 5  # تعداد نخبگان

        for _ in range(self.generations):
            fitness_scores = [self.fitness_check(c) for c in self.population]

            # ذخیره راه حل‌های کامل
            for i, score in enumerate(fitness_scores):
                if score == self.optimum_fitness:
                    solution = tuple(self.population[i])
                    if solution not in self.solutions:
                        self.solutions.append(solution)

            if len(self.solutions) >= 5:
                break

            # تولید نسل جدید
            new_population = []

            # انتخاب نخبگان و کپی مستقیم به نسل بعد
            sorted_pop = sorted(zip(fitness_scores, self.population), reverse=True)
            for i in range(elite_count):
                new_population.append(sorted_pop[i][1])

            # تولید فرزندان تا پر شدن جمعیت
            while len(new_population) < len(self.population):
                parent1 = self.select_parent(fitness_scores)
                parent2 = self.select_parent(fitness_scores)
                child = self.crossover(parent1, parent2)
                child = self.mutation(child)
                new_population.append(child)

            self.population = new_population

        return [list(s) for s in self.solutions]

'''
solver = GeneticAlgorithm(n=8)
solutions = solver.run_evolution()
for sol in solutions:
    print(sol)'''