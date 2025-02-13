import sys
import copy
import random
from colorama import init, Fore, Style

init(autoreset=True)

class SudokuSolver:
    def __init__(self, board):
        self.board = board  # 9x9 grid
        self.size = 9
        self.box_size = 3
        self.domains = dict()  # For each cell, its possible values
        self.variables = []  # List of variables (cells)
        self.initialize_domains()

    def initialize_domains(self):
        self.domains = dict()
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    self.domains[(row, col)] = set(range(1, 10))
                else:
                    self.domains[(row, col)] = set([self.board[row][col]])
        self.variables = list(self.domains.keys())
        # Perform AC-3 algorithm for constraint propagation
        if not self.ac3():
            print(Fore.RED + "The puzzle is unsolvable.")
            sys.exit(0)

    def print_board(self):
        print(Fore.YELLOW + "Sudoku Board:")
        for row in range(self.size):
            if row % 3 == 0 and row != 0:
                print(Fore.YELLOW + "------+-------+------")
            line = ''
            for col in range(self.size):
                if col % 3 == 0 and col != 0:
                    line += Fore.YELLOW + "| "
                num = self.board[row][col]
                if num == 0:
                    line += Fore.CYAN + '.' + ' '
                else:
                    line += Fore.GREEN + str(num) + ' '
            print(line)
        print()

    def is_valid(self, num, pos):
        row, col = pos
        # Check row
        for c in range(self.size):
            if self.board[row][c] == num and c != col:
                return False
        # Check column
        for r in range(self.size):
            if self.board[r][col] == num and r != row:
                return False
        # Check box
        box_row = row // self.box_size
        box_col = col // self.box_size
        for r in range(box_row * self.box_size, (box_row + 1) * self.box_size):
            for c in range(box_col * self.box_size, (box_col + 1) * self.box_size):
                if self.board[r][c] == num and (r, c) != pos:
                    return False
        return True

    def find_empty(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def backtracking_solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Solved
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(num, (row, col)):
                self.board[row][col] = num
                if self.backtracking_solve():
                    return True
                self.board[row][col] = 0
        return False

    def ac3(self):
        queue = [(xi, xj) for xi in self.variables for xj in self.neighbors(xi)]
        while queue:
            xi, xj = queue.pop(0)
            if self.revise(xi, xj):
                if not self.domains[xi]:
                    return False  # Failure
                for xk in self.neighbors(xi):
                    if xk != xj:
                        queue.append((xk, xi))
        return True

    def revise(self, xi, xj):
        revised = False
        for x in set(self.domains[xi]):
            if not any(self.is_consistent(x, y, xi, xj) for y in self.domains[xj]):
                self.domains[xi].remove(x)
                revised = True
        return revised

    def is_consistent(self, x, y, xi, xj):
        if x != y:
            return True
        else:
            return False

    def neighbors(self, var):
        row, col = var
        neighbors = set()
        for c in range(self.size):
            if c != col:
                neighbors.add((row, c))
        for r in range(self.size):
            if r != row:
                neighbors.add((r, col))
        # Box
        box_row = row // self.box_size
        box_col = col // self.box_size
        for r in range(box_row * self.box_size, (box_row + 1) * self.box_size):
            for c in range(box_col * self.box_size, (box_col + 1) * self.box_size):
                if (r, c) != var:
                    neighbors.add((r, c))
        return neighbors

    def select_unassigned_variable(self):
        # Return the unassigned variable with the smallest domain (MRV)
        unassigned_vars = [var for var in self.variables if self.board[var[0]][var[1]] == 0]
        if not unassigned_vars:
            return None
        # MRV heuristic
        return min(unassigned_vars, key=lambda var: len(self.domains[var]))

    def backtracking_search(self):
        return self.backtrack()

    def backtrack(self):
        if all(self.board[row][col] != 0 for row in range(self.size) for col in range(self.size)):
            return True  # Solved
        var = self.select_unassigned_variable()
        if not var:
            return False  # Failure
        row, col = var
        domain_values = self.order_domain_values(var)
        for value in domain_values:
            if self.is_valid(value, var):
                # Assign value
                self.board[row][col] = value
                # Keep a copy of domains
                saved_domains = copy.deepcopy(self.domains)
                # Forward checking: remove value from domains of neighbors
                self.forward_check(var, value)
                result = self.backtrack()
                if result:
                    return True
                # Failure, undo assignment and restore domains
                self.board[row][col] = 0
                self.domains = saved_domains
        return False

    def forward_check(self, var, value):
        # Remove value from domains of neighbors
        for neighbor in self.neighbors(var):
            if self.board[neighbor[0]][neighbor[1]] == 0:
                if value in self.domains[neighbor]:
                    self.domains[neighbor].remove(value)

    def order_domain_values(self, var):
        # Least Constraining Value heuristic
        domain_values = list(self.domains[var])
        def num_constraining(value):
            count = 0
            for neighbor in self.neighbors(var):
                if value in self.domains[neighbor]:
                    count +=1
            return count
        domain_values.sort(key=lambda val: num_constraining(val))
        return domain_values

    def generate_full_grid(self):
        self.board = [[0]*self.size for _ in range(self.size)]
        self.initialize_domains()
        self.backtracking_search()
        return self.board

    def generate_puzzle(self, difficulty=40):
        self.generate_full_grid()
        # Remove numbers from the grid
        cells = [(row, col) for row in range(self.size) for col in range(self.size)]
        random.shuffle(cells)
        for i in range(difficulty):
            row, col = cells[i]
            self.board[row][col] = 0
        # Re-initialize domains
        self.initialize_domains()
        return self.board

def main():
    print(Fore.CYAN + "Welcome to the Sudoku Solver!")
    print("Please select an option:")
    print("1. Solve a Sudoku puzzle")
    print("2. Generate and solve a Sudoku puzzle")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        print("Please enter the Sudoku puzzle line by line (use 0 or '.' for empty cells):")
        board = []
        for i in range(9):
            line = input()
            row = []
            for char in line:
                if char.isdigit():
                    row.append(int(char))
                elif char in '. *':
                    row.append(0)
            if len(row) != 9:
                print(Fore.RED + "Invalid input. Each line must have 9 digits.")
                return
            board.append(row)
        solver = SudokuSolver(board)
        print("Solving the puzzle...")
        solver.print_board()
        if solver.backtracking_search():
            print(Fore.GREEN + "Puzzle solved successfully!")
            solver.print_board()
        else:
            print(Fore.RED + "This puzzle cannot be solved.")
    elif choice == '2':
        difficulty = input("Enter difficulty level (number of cells to remove, e.g., 40): ")
        try:
            difficulty = int(difficulty)
        except ValueError:
            print(Fore.RED + "Invalid input.")
            return
        solver = SudokuSolver([[0]*9 for _ in range(9)])
        solver.generate_puzzle(difficulty)
        print("Generated puzzle:")
        solver.print_board()
        print("Solving the puzzle...")
        if solver.backtracking_search():
            print(Fore.GREEN + "Puzzle solved successfully!")
            solver.print_board()
        else:
            print(Fore.RED + "This puzzle cannot be solved.")
    elif choice == '3':
        print(Fore.CYAN + "Goodbye!")
    else:
        print(Fore.RED + "Invalid choice.")

if __name__ == "__main__":
    main()