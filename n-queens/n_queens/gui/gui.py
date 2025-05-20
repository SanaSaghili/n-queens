import tkinter as tk
import threading
from .queen_shape import get_queen_image


class NQueensUI:
    def __init__(self, root, n, controller):
        self.root = root
        self.n = n
        self.controller = controller

        self.root.title(f"{n}-Queens Solver")

        self.cell_size = 500 // n
        self.offset = 30
        self.tk_crown_image = None

        self.solutions = []
        self.current_solution_index = 0

        self._setup_ui()
        self._draw_board()

    def _setup_ui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        self.canvas = tk.Canvas(frame, width=600, height=600, bg="white")
        self.canvas.grid(row=0, column=0, padx=10, pady=10)

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=0, column=1, padx=10, pady=10)


        tk.Label(btn_frame, text="Enter number of queens:", font=("Arial", 12)).grid(row=0, column=0, pady=5)
        self.n_entry = tk.Entry(btn_frame, width=5, font=("Arial", 12))
        self.n_entry.insert(0, str(self.n))
        self.n_entry.grid(row=1, column=0, pady=5)

        btn_cfg = {"width": 20, "height": 2, "bg": "#77dd77"}


        tk.Button(btn_frame, text="Backtracking Algorithm", command=self.run_backtracking_algorithm, **btn_cfg).grid(
            row=2, column=0, pady=5)
        tk.Button(btn_frame, text="CSP Algorithm", command=self.run_csp_algorithm, **btn_cfg).grid(row=3, column=0,
                                                                                                   pady=5)
        tk.Button(btn_frame, text="Genetic Algorithm", command=self.run_genetic_algorithm, **btn_cfg).grid(row=4,
                                                                                                           column=0,
                                                                                                           pady=5)
        tk.Button(btn_frame, text="Next Solution", bg="#FFC090", command=self.show_next_solution, width=20,
                  height=2).grid(row=5, column=0, pady=5)
        tk.Button(btn_frame, text="Exit", bg="#ff7f7f", command=self.root.quit, width=20, height=2).grid(row=6,
                                                                                                         column=0,
                                                                                                         pady=5)

        self.solution_label = tk.Label(self.root, text="Select an algorithm to solve the problem",
                                       font=("Times New Roman", 14))
        self.solution_label.pack(pady=10)

    def _draw_board(self):
        self.canvas.delete("all")
        for row in range(self.n):
            for col in range(self.n):
                color = "white" if (row + col) % 2 == 0 else "black"
                x1 = col * self.cell_size + self.offset
                y1 = row * self.cell_size + self.offset
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        for col in range(self.n):
            x = col * self.cell_size + self.cell_size / 2 + self.offset
            self.canvas.create_text(x, self.offset / 2, text=str(col + 1), font=("Arial", 12))
        for row in range(self.n):
            y = row * self.cell_size + self.cell_size / 2 + self.offset
            self.canvas.create_text(self.offset / 2, y, text=str(row + 1), font=("Arial", 12))

    def place_queens(self, positions):
        self._draw_board()
        self.tk_crown_image = get_queen_image(self.cell_size)
        for row, col in enumerate(positions):
            x = col * self.cell_size + self.offset + self.cell_size // 2
            y = row * self.cell_size + self.offset + self.cell_size // 2
            self.canvas.create_image(x, y, image=self.tk_crown_image)

    def show_loading(self, message="Finding a solution..."):
        self.loading_window = tk.Toplevel(self.root)
        self.loading_window.title("Please wait")
        self.loading_window.geometry("250x100")
        self.loading_window.resizable(False, False)
        tk.Label(self.loading_window, text=message, font=("Arial", 12)).pack(expand=True, padx=10, pady=20)
        self.loading_window.update()

    def close_loading(self):
        if hasattr(self, 'loading_window') and self.loading_window:
            self.loading_window.destroy()
            self.loading_window = None



    def run_backtracking_algorithm(self):
        if not self.update_n_and_controller():
            return
        self.solution_label.config(text="Running Backtracking Algorithm...")
        threading.Thread(target=self._run_backtracking_thread).start()

    def _run_backtracking_thread(self):
        solutions = self.controller.run_backtracking_algorithm()
        self.root.after(0, self._on_algorithm_done, solutions)

    def run_genetic_algorithm(self):
        if not self.update_n_and_controller():
            return
        self.solution_label.config(text="Running Genetic Algorithm...")
        threading.Thread(target=self._run_genetic_thread).start()

    def _run_genetic_thread(self):
        solutions = self.controller.run_genetic_algorithm()
        self.root.after(0, self._on_algorithm_done, solutions)

    def run_csp_algorithm(self):
        if not self.update_n_and_controller():
            return
        self.solution_label.config(text="Running CSP Algorithm...")
        solutions = self.controller.run_csp_algorithm()
        self._on_algorithm_done(solutions)

    def show_next_solution(self):
        if not self.solutions:
            self.solution_label.config(text="Please run an algorithm first.")
            return
        if self.current_solution_index < len(self.solutions) - 1:
            self.current_solution_index += 1
            self.place_queens(self.solutions[self.current_solution_index])
            self.solution_label.config(text=f"Solution {self.current_solution_index + 1} of {len(self.solutions)}")
        else:
            self.solution_label.config(text="No more solutions available.")

    def update_n_and_controller(self):
        try:
            n = int(self.n_entry.get())
            if n < 1:
                raise ValueError
        except ValueError:
            self.solution_label.config(text="Please enter a valid positive integer for n.")
            return False
        self.n = n
        self.cell_size = 500 // self.n
        self.controller.set_n(n)
        self.current_solution_index = 0
        self.solutions = []
        self._draw_board()
        return True

    def _on_algorithm_done(self, solutions):
        self.close_loading()
        if not solutions:
            self.solution_label.config(text="No solutions found.")
            return
        self.solutions = solutions
        self.current_solution_index = 0
        self.place_queens(solutions[0])
        self.solution_label.config(text=f"Solution 1 of {len(solutions)}")
