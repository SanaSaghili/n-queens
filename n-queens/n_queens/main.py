# کد اصلی اجرای برنامه

import tkinter as tk
from gui.gui import NQueensUI # وارد کردن رابط گرافیکی از فایل gui.py در پوشه gui
from logics import NQueensController # وارد کردن کنترل‌کننده‌ی منطق بازی از فایل logics.py


def main():
    # ایجاد پنجره‌ی اصلی Tkinter
    root = tk.Tk()

    # مقدار اولیه n برای صفحه‌ی شطرنج (تعداد ردیف/ستون و وزیرها)
    n = 8

    # ایجاد شیء کنترل‌کننده با مقدار اولیه n
    logic = NQueensController(n)

    # ایجاد رابط کاربری و اتصال به پنجره و منطق برنامه
    app = NQueensUI(root, n, logic)

    # شروع حلقه اصلی رابط گرافیکی (تا بسته شدن پنجره)
    root.mainloop()

# بررسی اینکه آیا این فایل مستقیماً اجرا شده یا خیر
if __name__ == "__main__":
    main()

