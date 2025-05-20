#main.py
import tkinter as tk
from gui.gui import NQueensUI
from logics import NQueensController

def main():
    root = tk.Tk()
    n = 8
    logic = NQueensController(n)
    app = NQueensUI(root, n, logic)
    root.mainloop()


if __name__ == "__main__":
    main()

