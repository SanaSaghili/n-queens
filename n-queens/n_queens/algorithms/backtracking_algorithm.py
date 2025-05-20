# کد مربوط به الگوریتم عقبگرد
class BacktrackingAlgorithm:

    # مقداردهی اولیه الگوریتم عقبگرد
    # n:تعداد وزیر
    def __init__(self, n):

        self.size = n  # اندازه صفحه
        self.find_solution = []  # لیست جواب‌های پیدا شده

    def check(self, rows, columns, temp):
        #بررسی شروط تعارض
        for row in range(rows):
            # بررسی تعارض ستونی یا قطری
            if temp[row] == columns or abs(temp[row] - columns) == abs(row - rows):
                return False  # تعارض وجود دارد
        return True  # بدون تعارض

#تابع بازگشتی برای پیدا کردن تمام راه‌حل‌ها با استفاده از عقبگرد
    def find(self, row, temp):

        if row == self.size:
            # اگر همه ردیف‌ها با موفقیت پر شدند، یک راه‌حل معتبر پیدا شده است
            self.find_solution.append(temp[:])
            return
        
        # برای هر ستون در ردیف فعلی امتحان می‌کنیم
        for c in range(self.size):
            if self.check(row, c, temp):  # اگر قرار دادن وزیر در (row, c) معتبر است
                temp[row] = c  # وزیر را قرار بده
                self.find(row + 1, temp)  # برو به ردیف بعد
                temp[row] = -1  # backtrack (برگرداندن به حالت قبلی)

    #اجرای الگوریتم و برگشت دادن تمام جواب‌های معتبر
    def all_solutions(self):

        temp = [-1] * self.size
        self.find(0, temp)
        return self.find_solution
