# Decoding Luna City’s SUDOKU Mystery

## Introduction

Welcome to the Luna City Sudoku Solver! This project is a comprehensive Sudoku puzzle solver and generator implemented in Python. It was inspired by the mysterious events in Luna City, where encrypted signals were received in the form of Sudoku grids. Your mission is to decode these puzzles to uncover hidden messages.

This solver incorporates advanced algorithms, including constraint propagation with the AC-3 algorithm, backtracking search with forward checking, and heuristics like Minimum Remaining Value (MRV) and Least Constraining Value (LCV) to efficiently solve Sudoku puzzles.

```python
...1..2.7
....4...5
.8...3...
..5..7..9
.1..5..3.
2..9..5..
...6...4.
1...7....
8.2..9...
```

```
***26*7**
68**7****
19****5**
82*******
***6*29**
*********
**93*****
*4**5**36
7*3*18***
```

- `self.domains = dict()`  # For each cell, its possible values
- `self.variables = []`  # List of variables (cells)
- `self.solutions = []`  # List to store all possible solutions
- `self.initial_solution = None ` # Store the initial solution used to generate the puzzle



## Features

- Solves any valid 9x9 Sudoku puzzle provided by the user.
- Generates solvable Sudoku puzzles with customizable difficulty levels.
- Implements constraint propagation to reduce the search space.
- Uses backtracking search enhanced with forward checking.
- Incorporates heuristics to improve solving efficiency.
- Detects and handles unsolvable puzzles.
- User-friendly console interface with colored output for better readability.

## Installation

1.	Clone the repository or download the sudoku_solver.py file.
2. Install the required Python modules:
```python
pip install colorama
```
4. The colorama module is used for colored console output.
5. ure you have Python 3.x installed on your system.

## Usage
Run the program from the command line:
```python
python sudoku_solver.py
```
You will be greeted with a menu:
```python
Welcome to the Sudoku Solver!
Please select an option:
1. Solve a Sudoku puzzle
2. Generate and solve a Sudoku puzzle
3. Exit
Enter your choice (1-3):
```

### Option 1: Solve a Sudoku Puzzle
1. Select option 1 to solve a puzzle.
2. Input the puzzle line by line. Use `0`, `.`, or `*` for empty cells.

**Example Input:**
```
***26*7*1
68**7**9*
19***45**
82*1***4*
**46*29**
*5***3*28
**93***74
*4**5**36
7*3*18***
```
3. The program will display the initial puzzle and attempt to solve it.
4. If solvable, the solved puzzle will be displayed. If unsolvable, you will be informed.

**Example of Invalid Puzzle Input:**
```
5 5 . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
. . . . . . . . .
```

### Option 2: Generate and Solve a Sudoku Puzzle
1. Select option 2 to generate a puzzle.
2. Enter the difficulty level (number of cells to remove). Higher numbers result in fewer clues and harder puzzles.

Example Input:
```
Enter difficulty level (number of cells to remove, e.g., 40): 40
```
3. The program will generate and display the puzzle, then attempt to solve it.

## Code Workflow
### Initialization
Import Modules:
```
import sys
import copy
import random
from colorama import init, Fore, Style
```
### Initialize Colorama for colored console output:
```
init(autoreset=True)
```
### Class Definitions
#### SudokuSolver Class
The `SudokuSolver` class encapsulates all functionalities related to solving and generating Sudoku puzzles.

#### Attributes:

- `board:` The Sudoku grid, a 9x9 list of lists.
- `size:` Size of the grid (9).
- `box_size: `Size of the smaller 3x3 boxes (3).
- `domains:` A dictionary mapping each cell to its possible values.
- `variables:` A list of unassigned cells.

#### Methods:

- `initialize_domains()`: Initializes domains for each cell and applies the AC-3 algorithm for constraint propagation.
- `print_board()`: Prints the Sudoku board with colored formatting.
- `is_valid(num, pos)`: Checks if placing num at pos is valid.
- `find_empty()`: Finds an empty cell on the board.
- `backtracking_solve()`: Basic backtracking solver.
- `ac3()`: Implements the AC-3 algorithm for constraint propagation.
- `revise(xi, xj)`: Revises the domain of xi based on xj.
- `neighbors(var)`: Returns all neighboring cells of var.
- `select_unassigned_variable()`: Selects the next variable to assign using the MRV heuristic.
- `backtracking_search()`: Initiates the backtracking search with heuristics and forward checking.
- `backtrack()`: Core recursive function for backtracking search.
- `forward_check(var, value)`: Performs forward checking after assigning a value.
- `order_domain_values(var)`: Orders domain values using the LCV heuristic.
- `generate_full_grid()`: Generates a fully solved Sudoku grid.
- `generate_puzzle(difficulty)`: Removes numbers from a full grid to create a puzzle.

### Constraint Propagation with AC-3 Algorithm
- **Purpose:** Reduce the domains of cells by eliminating values that are inconsistent with their neighbors.

- **Implementation:**

```
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
    
```

### Backtracking Search with Heuristics
- **Purpose:** Systematically explore possible assignments, backtracking upon conflicts, and using heuristics to improve efficiency.

**Heuristics Used:**
- `Minimum Remaining Value (MRV`): Selects the unassigned variable with the smallest domain.

```
def select_unassigned_variable(self):
    unassigned_vars = [var for var in self.variables if self.board[var[0]][var[1]] == 0]
    if not unassigned_vars:
        return None
    return min(unassigned_vars, key=lambda var: len(self.domains[var]))
```

- `Least Constraining Value (LCV)`: Orders values in the domain to try those that constrain neighbors the least.

```
def order_domain_values(self, var):
    domain_values = list(self.domains[var])
    def num_constraining(value):
        count = 0
        for neighbor in self.neighbors(var):
            if value in self.domains[neighbor]:
                count += 1
        return count
    domain_values.sort(key=lambda val: num_constraining(val))
    return domain_values
```
### Forward Checking
- Purpose: After assigning a value to a variable, eliminate that value from the domains of its neighbors.
- **Implementation:**

```
def forward_check(self, var, value):
    for neighbor in self.neighbors(var):
        if self.board[neighbor[0]][neighbor[1]] == 0:
            if value in self.domains[neighbor]:
                self.domains[neighbor].remove(value)
```

### Puzzle Generation
- **Purpose:** Generate valid Sudoku puzzles with a unique solution.
- **Process:**
  - Start with an empty grid and generate a full solution using the solver.
  - Remove a specified number of cells to create a puzzle.
  - Reinitialize domains and apply constraint propagation to ensure solvability.

```
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
```


## Task Implementations
### Task 1: Implement a Sudoku Solver Using Backtracking
Implementation: The backtracking_solve() method performs a basic backtracking search to solve the puzzle.
```
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
```
#### Explanation:
- The function searches for an empty cell.
- Tries all numbers from 1 to 9 in that cell.
- If a valid number is found, it recursively attempts to solve the rest of the puzzle.
- If it reaches a conflict, it backtracks.

### Task 2: Define Domains and Implement Constraint Propagation
- **Domains:** For each empty cell, the domain is initially all numbers from 1 to 9.

```
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
```
- **Constraint Propagation**: Uses the AC-3 algorithm to reduce domains.

### Task 3: Combine Backtracking with Constraint Propagation (Forward Checking)
**Implementation:** The backtracking_search() method combines backtracking with forward checking.

```
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
```
#### Explanation:
- After assigning a value, forward checking eliminates that value from neighbors' domains.
- If a domain becomes empty, it triggers backtracking.

### Task 4: Implement Heuristic Algorithms with Constraint Propagation
- **Heuristics Implemented:**
  - Minimum Remaining Value (MRV): Prioritizes variables with the fewest legal values.
  - Least Constraining Value (LCV): Chooses values that least constrain other variables.
- **Purpose:** Improve the efficiency of the solver by reducing the search space.

### Task 5: Generate Valid Sudoku Grids
- **Implementation:** The generate_full_grid() method creates a fully solved grid.

`The generate_puzzle()` method removes numbers to create a puzzle.
- **Explanation:**
  - By solving an empty grid, we ensure the generated puzzle has a valid solution.
  - Randomly removing cells creates puzzles of varying difficulty.

### Task 6: Handle Invalid Sudoku Puzzles
Implementation: During initialization and constraint propagation, the solver checks for unsolvable puzzles.

```
if not self.ac3():
    print(Fore.RED + "The puzzle is unsolvable.")
    sys.exit(0)
```
- **Explanation:**
  - If any domain becomes empty during AC-3, the puzzle is unsolvable.
  - The solver informs the user and exits gracefully.

### Task 7: Implement Advanced Constraint Propagation Algorithms
- Implementation: Uses the AC-3 algorithm for constraint propagation.
- **Explanation:**
  - AC-3 effectively reduces domains by eliminating inconsistent values.
  - This pre-processing step simplifies the puzzle before search begins.

## Definitions and Explanations
### Constraint Satisfaction Problems (CSP)
- **Definition:** A problem where variables must be assigned values that satisfy specific constraints.
- In Sudoku:
  - **Variables:** Each cell in the grid.
  - **Domains:** Possible numbers (1-9) for each cell.
  - **Constraints:** No duplicate numbers in any row, column, or 3x3 box.

### AC-3 Algorithm
- **Arc Consistency Algorithm #3.**
- **Purpose:** Enforces consistency between pairs of variables.
- **Process:**
  - Iteratively removes values from domains that are inconsistent with neighboring variables.
  - Maintains a queue of arcs (variable pairs) to check.
- **Benefits:**
  - Simplifies the problem before search.
  - Can detect unsolvable puzzles early.

### Backtracking Search
- **Definition:** A recursive algorithm that attempts to build a solution incrementally.
- **Process:**
  - Assigns a value to a variable and moves to the next variable.
  - If a conflict arises, it backtracks to the previous variable and tries a different value.

### Forward Checking
- **Definition:** After assigning a value, it eliminates that value from the domains of neighboring unassigned variables.
- **Purpose:** Prevents future conflicts and reduces the need for backtracking.

### Heuristics: MRV and LCV
- **Minimum Remaining Value (MRV):**
  - Selects the variable with the fewest legal values.
  - Focuses on the most constrained variables first.
- **Least Constraining Value (LCV):**
  - Chooses the value that rules out the fewest options for neighboring variables.
  - Tries to leave as many choices as possible for other variables.

## Additional Explanations and Anticipated Questions
### Why Use AC-3 in Sudoku Solving?
- **Early Detection:** AC-3 can detect unsolvable puzzles before starting the search.
- **Domain Reduction:** Simplifies the problem by reducing possible values.
- **Efficiency:** Reduces the search space, making the solver faster.

### How Does Forward Checking Improve Efficiency?
- **Prevents Conflicts:** Eliminates values that would cause conflicts in the future.
- **Reduces Backtracking:** By catching failures early, it reduces the need to backtrack.
- **Dynamic Constraint Propagation:** Updates domains during the search process.

### What Are MRV and LCV Heuristics?
- MRV (Minimum Remaining Value):
  - Focuses on variables that are most likely to cause a dead end.
  - Solving these first increases the chances of early detection of conflicts.
- LCV (Least Constraining Value):
  - Prefers values that have the least impact on other variables.
  - Helps to keep options open for future assignments.

### Handling Multiple Solutions
- Current Implementation: The solver stops after finding the first valid solution.
- Extending to Find All Solutions:
  - Modify the `backtrack()` method to continue searching after a solution is found.
  - Collect all valid solutions in a list.

### Extending to Larger Grids
- Sudoku Variants:
  - The solver is designed for standard z grids.
  - To support larger grids (e.g., `16x16`), adjust `size` and `box_size` accordingly.

### Considerations:
- Larger grids increase computational complexity.
- Advanced techniques or optimizations may be required for efficiency.

## Conclusion
The Luna City Sudoku Solver is a robust and efficient tool for solving and generating Sudoku puzzles. By integrating advanced algorithms like AC-3, backtracking with forward checking, and heuristics, it provides a comprehensive solution to constraint satisfaction problems inherent in Sudoku.

Whether you're deciphering mysterious signals from the dark side of the moon or just enjoying a challenging puzzle, this solver offers a deep dive into the world of AI and algorithmic problem-solving.

