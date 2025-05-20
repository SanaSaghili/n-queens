# کد مربوط به الگوریتم ژنتیک
import random


class GeneticAlgorithm:

    #مقداردهی اولیه الگوریتم ژنتیک
    #n:تعداد وزیر، population:تعداد جمعیت اولیه، generations: تعداد نسل‌ها
    def __init__(self, n, population=1000, generations=500):

        self.n = n
        # ایجاد جمعیت اولیه با کروموزوم‌های تصادفی
        self.population = [self.create_chromosome() for _ in range(population)]
        self.generations = generations
        # بهترین حالت ممکن برای n وزیر بدون هیچ تعارض
        self.optimum_fitness = (n * (n - 1)) // 2
        self.solutions = []  # لیست نگهداری جواب‌های پیدا شده

    #ساخت یک کروموزوم جدید:
    # لیستی به طول n که شماره ردیف وزیر در ستون متناظر است.

    def create_chromosome(self):

        return [random.randrange(self.n) for _ in range(self.n)]

    #انتخاب والد به روش انتخاب چرخ رولت 
    def select_parent(self, fitness_scores):

        total = sum(fitness_scores)
        pick = random.uniform(0, total) 
        current = 0
        for i, score in enumerate(fitness_scores):
            current += score
            if current >= pick:
                return self.population[i]
        # اگر به هر دلیلی انتخاب نشد، اولین کروموزوم برگردانده می‌شود
        return self.population[0]

    #محاسبه تابع تناسب کروموزوم
    def fitness_check(self, chromosome):

        # تعداد تعارض‌ها در ردیف (تکرار ردیف برای وزیرها)
        row_conflict = sum(chromosome.count(g) - 1 for g in chromosome) // 2

        diag1 = {}
        diag2 = {}
        # محاسبه تعداد وزیرهایی که روی هر قطر قرار دارند
        for pos, gene in enumerate(chromosome):
            d1 = pos + gene
            d2 = pos - gene
            diag1[d1] = diag1.get(d1, 0) + 1
            diag2[d2] = diag2.get(d2, 0) + 1

        diag_conflict = 0
        # محاسبه تعداد تعارض‌های قطری
        for cnt in diag1.values():
            diag_conflict += max(0, cnt - 1)
        for cnt in diag2.values():
            diag_conflict += max(0, cnt - 1)

        # تناسب نهایی: هر چه تعارض کمتر باشد، تناسب بیشتر است
        return self.optimum_fitness - (row_conflict + diag_conflict)

    #انجام کراس آوور بین دو والد
    def crossover(self, parent_a, parent_b):
        #برای هر ژن، به صورت تصادفی یکی از والدین انتخاب می‌شود
        return [random.choice([a, b]) for a, b in zip(parent_a, parent_b)]

    #عمل جهش  روی یک کروموزوم
    #یک ژن تصادفی انتخاب شده و مقدار آن به صورت تصادفی تغییر می‌کند
    def mutation(self, chromosome):

        new_chromosome = chromosome.copy()
        idx = random.randrange(self.n)
        new_chromosome[idx] = random.randrange(self.n)
        return new_chromosome

    #اجرای فرآیند تکامل ژنتیک برای تعداد مشخصی نسل 
    def run_evolution(self):

        elite_count = 5  # تعداد والدین برتر که مستقیم به نسل بعد منتقل می‌شوند

        for _ in range(self.generations):
            # محاسبه تناسب برای هر کروموزوم
            fitness_scores = [self.fitness_check(c) for c in self.population]

            # ذخیره راه حل‌های کامل (کسانی که امتیاز بهینه دارند)
            for i, score in enumerate(fitness_scores):
                if score == self.optimum_fitness:
                    solution = tuple(self.population[i])
                    if solution not in self.solutions:
                        self.solutions.append(solution)

            # اگر تعداد راه حل‌های کامل به حد کافی رسید، خاتمه بده
            if len(self.solutions) >= 5:
                break

            new_population = []

            # انتخاب والدین برتر و اضافه کردن به جمعیت جدید بدون تغییر
            sorted_pop = sorted(zip(fitness_scores, self.population), reverse=True)
            for i in range(elite_count):
                new_population.append(sorted_pop[i][1])

            # تولید بقیه جمعیت جدید با انتخاب والد، crossover و mutation
            while len(new_population) < len(self.population):
                parent1 = self.select_parent(fitness_scores)
                parent2 = self.select_parent(fitness_scores)
                child = self.crossover(parent1, parent2)
                child = self.mutation(child)
                new_population.append(child)

            # جایگزینی جمعیت فعلی با نسل جدید
            self.population = new_population

        # برگرداندن لیستی از راه حل‌ها به صورت لیست از لیست‌ها
        return [list(s) for s in self.solutions]
