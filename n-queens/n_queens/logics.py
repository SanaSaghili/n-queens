# وارد کردن کلاس‌های مربوط به الگوریتم‌های حل مسئله n-Queens
from algorithms.backtracking_algorithm import BacktrackingAlgorithm
from algorithms.genetic_algorithm import GeneticAlgorithm
from algorithms.min_conflicts_algorithm import MinConflictsAlgorithm


# سازنده‌ی کلاس NQueensController
#n: اندازه‌ی صفحه شطرنج و تعداد وزیرها
class NQueensController:

    def __init__(self, n):
        self.n = n

    def set_n(self, n):
        """
        تنظیم مقدار جدید برای n
        """
        self.n = n

    """
    اجرای الگوریتم دقیق Backtracking
    خروجی: لیستی از جواب‌های معتبر (هر جواب یک لیست از موقعیت وزیرها در ردیف‌های مختلف است)
    """
    def run_backtracking_algorithm(self):

        solver = BacktrackingAlgorithm(self.n)
        return solver.all_solutions()

    """
    اجرای الگوریتم ژنتیکی
    خروجی: لیستی از جواب‌های پیدا شده با تکامل ژنتیکی
    """
    def run_genetic_algorithm(self):

        genetic = GeneticAlgorithm(self.n)
        return genetic.run_evolution()

    """
    اجرای الگوریتم Min-Conflicts به عنوان روش CSP
    خروجی: لیستی از جواب‌های پیدا شده با الگوریتم Min-Conflicts
    """
    def run_min_conficts_algorithm(self):
        csp = MinConflictsAlgorithm(self.n)
        return csp.run()


