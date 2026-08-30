# Sudoku Solver 🧩

A modular Sudoku solver written in Python that combines **constraint-based solving techniques** with **backtracking search**.

The project was built with a focus on understanding how a Sudoku solver works internally rather than relying on a single brute-force algorithm. The solver first tries to reduce the search space using logical solving techniques and uses backtracking when further deduction is not possible.

---

## ✨ Features

* 🧩 Solves standard **9×9 Sudoku puzzles**
* 🔍 Calculates possible candidates for every empty cell
* 🧠 Uses constraint-based solving techniques before searching
* 🔄 Uses recursive backtracking when logical techniques cannot finish the puzzle
* 🎯 Uses a **Minimum Remaining Values (MRV)** strategy to choose the next cell
* 🧱 Modular project structure
* 🏗️ Object-oriented `Sudoku` solver interface
* 🖨️ Clean formatted Sudoku output
* 🔬 Separate validation, candidate-generation, solving-technique, and search modules

---

## 🧠 How It Works

The solver follows a two-stage approach:

```text
             Sudoku Board
                   │
                   ▼
        Calculate Possible Numbers
                   │
                   ▼
        Apply Solving Techniques
                   │
          ┌────────┴────────┐
          │                 │
       Solved          Not Solved
          │                 │
          ▼                 ▼
       Return       Select Best Cell
                            │
                            ▼
                       Backtracking
                            │
                    ┌───────┴───────┐
                    │               │
                  Valid           Invalid
                    │               │
                    ▼               ▼
              Continue Search    Backtrack
```

### 1. Candidate Generation

For every empty cell, the solver determines which numbers from `1` to `9` are currently possible based on the cell's:

* Row
* Column
* 3×3 subgrid

The candidate information is maintained separately from the actual Sudoku board.

---

### 2. Constraint-Based Techniques

Before performing expensive recursive search, the solver attempts to make progress using logical techniques.

The techniques operate on the candidate grid and modify the Sudoku state when a valid deduction is found.

The project currently includes techniques such as:

* Candidate elimination
* Direct candidate placement
* Number-location analysis
* Pair-based candidate elimination

The techniques are repeatedly applied until no further progress can be made.

This reduces the size of the search space before backtracking begins.

---

### 3. Backtracking Search

If logical techniques cannot completely solve the puzzle, the solver switches to recursive backtracking.

Instead of simply choosing the first empty cell, the solver searches for the cell with the **fewest possible candidates**.

For example:

```text
Cell A → [1, 2, 3, 4]
Cell B → [2, 7]
Cell C → [5]
Cell D → [1, 4, 8]
```

The solver prefers the cell with the smallest candidate set.

This is a form of the **Minimum Remaining Values (MRV)** heuristic.

Choosing the most constrained cell first can significantly reduce unnecessary branches in the search tree.

---

## 📁 Project Structure

```text
sudoku_solver/
│
├── sudoku/
│   ├── __init__.py
│   ├── backtrack.py
│   ├── candidates.py
│   ├── chunks.py
│   ├── display.py
│   ├── samples.py
│   ├── solver.py
│   ├── techniques.py
│   └── validation.py
│
├── tests/
│
├── main.py
├── .gitignore
└── README.md
```

### `solver.py`

Provides the main `Sudoku` class.

The class is responsible for maintaining:

* The Sudoku board
* The candidate grid
* The solving interface
* The formatted representation of the board

The current design exposes methods such as:

```python
Sudoku(board)
```

```python
sudoku.fit()
```

and:

```python
print(sudoku)
```

The class initializes a deep copy of the supplied board and creates the corresponding candidate grid.

---

### `candidates.py`

Responsible for determining the possible numbers for cells in the Sudoku board.

The candidate representation allows the solving techniques and backtracking algorithm to reason about the remaining possibilities.

---

### `techniques.py`

Contains the logical Sudoku-solving techniques.

It also contains the mechanism that repeatedly applies the available techniques until the board stops changing.

The solver uses this phase before entering recursive backtracking.

---

### `backtrack.py`

Contains the recursive search algorithm.

The backtracking implementation:

1. Applies the logical solving techniques.
2. Checks whether the puzzle is solved.
3. Validates the current board.
4. Finds the cell with the fewest candidates.
5. Tries each candidate.
6. Creates a temporary Sudoku state.
7. Recursively searches for a solution.
8. Backtracks when a candidate leads to an invalid state.

The implementation uses `deepcopy` to preserve independent states during recursive exploration.

---

### `validation.py`

Responsible for checking whether the Sudoku state is valid.

Validation is important during backtracking because incorrect assumptions must be detected as early as possible.

---

### `display.py`

Handles Sudoku formatting and presentation.

The display function constructs the complete board representation and returns it as a string rather than printing each line directly. This allows the `Sudoku` class to implement a clean `__str__()` interface.

---

### `chunks.py`

Contains utilities used to work with Sudoku sections and groups.

---

### `samples.py`

Contains example Sudoku boards that can be used for testing and experimentation.

---

### `tests/`

Contains tests for the solver and its individual components.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/nimafarahani1919/sudoku_solver.git
```

Move into the project directory:

```bash
cd sudoku_solver
```

No external Python packages are currently required for the core solver.

Make sure you have Python installed:

```bash
python --version
```

Python 3.9+ is recommended.

---

## ▶️ Usage

Create a Sudoku board using `0` for empty cells:

```python
from sudoku.solver import Sudoku

board = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

sudoku = Sudoku(board)

sudoku.fit()

print(sudoku)
```

The solver will modify its internal Sudoku state and the object can then be printed using:

```python
print(sudoku)
```

---

## 🔎 Candidate Grid

The solver maintains two related representations:

### Sudoku grid

```text
[
    [5, 3, 0, ...],
    [6, 0, 0, ...],
    ...
]
```

### Possible-number grid

An empty cell can contain a list of possible values:

```text
[
    [5, 3, [1, 2, 4], ...],
    [6, [1, 7], [2, 8], ...],
    ...
]
```

This separation allows the solver to distinguish between:

* Values already placed on the board
* Values that are still possible

That candidate information is then used by the logical techniques and backtracking algorithm.

---

## 🎯 Backtracking Strategy

A naive backtracking solver might always select the first empty cell:

```text
Find empty cell
      ↓
Try 1
      ↓
Try 2
      ↓
Try 3
      ↓
...
```

This can create a very large search tree.

This project instead looks for the cell with the **smallest number of candidates**.

For example:

```text
A → [1, 2, 3, 4, 5]
B → [2, 7]
C → [1, 4, 8]
D → [6]
```

The solver chooses `D` first because it has the smallest candidate set.

This reduces branching and makes the recursive search considerably more focused.

---

## 🏗️ Object-Oriented Design

The current version uses a `Sudoku` class as the main interface.

```python
class Sudoku:
    def __init__(self, sudoku):
        ...

    def fit(self):
        ...

    def __str__(self):
        ...
```

This design separates the public Sudoku-solving interface from the internal implementation details.

The solving process itself remains modular:

```text
Sudoku
  │
  ├── Candidate Generation
  │
  ├── Techniques
  │
  ├── Validation
  │
  └── Backtracking
```

The class-based refactor was introduced to make the solver easier to use and to separate responsibilities between modules.

---

## 🧪 Testing

Tests are located in:

```text
tests/
```

Run the test suite with:

```bash
python -m pytest
```

If `pytest` is not installed:

```bash
pip install pytest
```

---

## 🛠️ Design Goals

The main goals of this project are:

* Learn how Sudoku solving algorithms work internally.
* Separate different solving responsibilities into independent modules.
* Combine human-like deduction with algorithmic search.
* Reduce unnecessary backtracking through candidate analysis.
* Keep the codebase easy to extend with new solving techniques.
* Practice object-oriented Python design.

This project is therefore intended not only as a Sudoku solver, but also as an exploration of **constraint solving, recursion, search heuristics, and software architecture**.

---

## 🔮 Future Improvements

Possible future improvements include:

* [ ] Add more advanced Sudoku techniques.
* [ ] Improve candidate propagation.
* [ ] Add detailed solving-step output.
* [ ] Add performance benchmarks.
* [ ] Improve input validation and error messages.
* [ ] Add Sudoku puzzle generation.
* [ ] Add difficulty estimation.
* [ ] Add a graphical user interface.
* [ ] Improve test coverage.
* [ ] Add type hints throughout the project.
* [ ] Optimize deep-copy operations during backtracking.

---

## 📚 Concepts Demonstrated

This project provides practical experience with several important programming and computer-science concepts:

| Concept                     | Usage                                     |
| --------------------------- | ----------------------------------------- |
| Recursion                   | Backtracking search                       |
| Backtracking                | Exploring possible Sudoku states          |
| Constraint Satisfaction     | Maintaining valid candidates              |
| Heuristics                  | Selecting the most constrained cell       |
| MRV                         | Choosing the cell with minimum candidates |
| Object-Oriented Programming | `Sudoku` class                            |
| Modular Design              | Separate solver components                |
| Deep Copying                | Maintaining independent search states     |
| Validation                  | Detecting invalid Sudoku states           |
| Data Structures             | Lists and candidate sets                  |

---

## 👤 Author

**Nima Farahani**

GitHub: [@nimafarahani1919](https://github.com/nimafarahani1919)

---

## 📄 License

This project is currently intended primarily as a learning and personal software project.

If you plan to distribute the project publicly, consider adding an explicit open-source license such as the MIT License.
