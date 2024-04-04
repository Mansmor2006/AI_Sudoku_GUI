# CSP Sudoku Solver 🎲

A Constraint Satisfaction Problem (CSP) Sudoku Solver implemented in Python using the Pygame library. The solver utilizes both Backtracking and Forward Checking algorithms to efficiently solve Sudoku puzzles.

## Features 🌟

- Solve Sudoku puzzles of various difficulty levels from easy, medium & hard.
- Utilizes Backtracking algorithm for efficient solving.
- Implements Forward Checking to reduce the search space by eliminating possible dead ends and improve performance.
- Interactive GUI built with Pygame for a visually appealing gameplay experience.

## Installation 🚀

1. Clone the repository:

    ```bash
    git clone https://github.com/Mansmor2006/AI_Sudoku_GUI
    ```

2. Navigate to the project directory:

    ```bash
    cd AI-Sudoku-GUI
    ```
3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```
4. Activate virtual environment:

    ```bash
    .venv\Scripts\activate # Windows
    
    source venv/bin/activate # Mac/Linux
    ```
5. Install the required dependencies in venv only:

    ```bash
    pip install -r requirements.txt
    ```
6. If environment not needed anymore deactivate:

    ```bash
    deactivate
    ```
    

## Usage 🎮

1. Run the `main.py` script:

    ```bash
    python main.py
    ```
2. Choose a difficulty in the splash screen, then press **Start** button
3. Press with your mouse on any sudoku square and type in a number.<br> ***Note:** If number goes against sudoku rules it will not appear*
4. **Solve** button displays sudoku solution if stuck
5. **Reset** will clear sudoku puzzle to its starting state
6. **New Game** will create a new sudoku puzzle
7. Enjoy solving Sudoku puzzles interactively using the Pygame GUI!

## How it Works 🧠

The solver uses the concept of Constraint Satisfaction Problem (CSP) to solve Sudoku puzzles. Here's a brief overview:

- **Backtracking Algorithm**: Backtracking is used to systematically search for a solution to the Sudoku puzzle. It tries out various combinations of numbers for each empty cell while respecting the constraints imposed by the puzzle's rules.

- **Forward Checking**: Forward Checking is applied during the search process to reduce the domain of variables (possible values for each cell) by eliminating values that conflict with the constraints before they are explicitly violated.

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to this project, feel free to open a pull request with your changes.
Thanks Mansoor.

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
