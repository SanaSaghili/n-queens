# N-Queens

## 🇬🇧 English

### Introduction

This project was developed for the Artificial Intelligence and Expert Systems course at the undergraduate level. Its primary goal is to solve the classical N-Queens problem using multiple algorithms and provide a user-friendly graphical interface.

### What is the N-Queens Problem?

The N-Queens problem is a classic challenge in AI and combinatorics. The goal is to place n queens on an n×n chessboard such that no two queens threaten each other — i.e., no two queens share the same row, column, or diagonal.

### Implemented Algorithms

The following three algorithms are implemented for comparison and educational purposes:

1. Backtracking Algorithm: A complete search method to find all possible solutions.  
2. Genetic Algorithm: A heuristic optimization method inspired by natural selection.  
3. Min-Conflicts Algorithm: A local search method suitable for Constraint Satisfaction Problems (CSP).

### Graphical User Interface

To facilitate interaction, the interface is implemented using the Tkinter library. Users can input the number of queens, select a solving algorithm, and visualize solutions on a chessboard. Multiple solutions can be browsed using the 'Next Solution' button.

### Project Structure

```
n_queens/
├── algorithms/
│   ├── backtracking_algorithm.py
│   ├── genetic_algorithm.py
│   ├── min_conflicts_algorithm.py
├── gui/
│   ├── gui.py
│   ├── queen_shape.py
├── logics.py
└── main.py
```

### How to Run

Make sure Python is installed, then simply run the following command:

```
python main.py
```

This will launch the graphical interface where you can solve the N-Queens problem interactively.

### Notes

- The project is implemented in Python.
- Tkinter is required for GUI support (it comes pre-installed with Python).
- Population size and generations in the Genetic Algorithm are configurable for performance.

# N-Queens Solver | حل‌گر مسئله n وزیر

## 🇮🇷 فارسی

### معرفی

این پروژه مربوط به تمرین درس هوش مصنوعی و سیستم‌های خبره در مقطع کارشناسی می‌باشد. هدف اصلی آن حل مسئله کلاسیک n وزیر با استفاده از الگوریتم‌های مختلف و همچنین طراحی یک رابط گرافیکی کاربرپسند است.

### مسئله n وزیر چیست؟

مسئله n وزیر یکی از مسائل کلاسیک در حوزه هوش مصنوعی و ترکیبیات است. در این مسئله هدف قرار دادن n وزیر روی صفحه‌ی شطرنج n×n است به‌گونه‌ای که هیچ دو وزیر نتوانند همدیگر را تهدید کنند؛ یعنی در یک سطر، ستون یا قطر مشترک قرار نگیرند.

### الگوریتم‌های پیاده‌سازی‌شده

برای حل این مسئله، سه الگوریتم مختلف پیاده‌سازی شده‌اند تا مزایا و معایب هر یک مورد بررسی قرار گیرد:

1. الگوریتم عقب‌گرد (Backtracking): جستجوی کامل برای پیدا کردن همه‌ی پاسخ‌های ممکن.  
2. الگوریتم ژنتیک (Genetic Algorithm): روش مبتنی بر بهینه‌سازی تصادفی با الهام از تکامل طبیعی.  
3. الگوریتم Min-Conflicts: الگوریتم محلی برای حل سریع‌تر مسائل محدودیت‌دار (CSP).

### رابط کاربری گرافیکی

برای تعامل ساده‌تر کاربران با سیستم، از کتابخانه Tkinter در پایتون استفاده شده است. رابط کاربری به کاربر اجازه می‌دهد مقدار n را مشخص کند، الگوریتم حل مسئله را انتخاب کرده و راه‌حل‌ها را به‌صورت گرافیکی مشاهده نماید.

### ساختار پروژه

```
n_queens/
├── algorithms/
│   ├── backtracking_algorithm.py      # الگوریتم عقبگرد
│   ├── genetic_algorithm.py           # الگوریتم ژنتیک
│   ├── min_conflicts_algorithm.py     # الگوریتم Min-Conflicts
├── gui/
│   ├── gui.py                         # پیاده سازی رابط گرافیکی 
│   ├── queen_shape.py                 # بارگذاری تصویر مهره وزیر
├── logics.py                          # کلاس کنترل الگوریتم‌ها
└── main.py                            # نقطه اجرای برنامه
```

### نحوه اجرا

برای اجرای پروژه، کافی است پایتون نصب شده باشد. سپس از طریق ترمینال یا محیط IDE دستور زیر را اجرا نمایید:

```
python main.py
```

با اجرای این دستور، رابط گرافیکی برنامه اجرا شده و امکان تعامل فراهم می‌شود.

### ملاحظات

- این پروژه با زبان Python توسعه داده شده است.
- برای اجرای صحیح رابط گرافیکی، کتابخانه Tkinter باید نصب و فعال باشد.
- برای اطمینان از عملکرد صحیح الگوریتم ژنتیک، پارامترهای جمعیت و نسل‌ها قابل تنظیم هستند.

---