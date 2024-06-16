Sure, here's the complete README file for the Sudoku solver project:

---

# Sudoku Solver

This project extracts and solves Sudoku puzzles from images or a list of lists using OpenCV and Tesseract OCR.

## Installation

### Prerequisites

- Python 3.x
- Tesseract OCR (Ensure Tesseract is installed and added to your system PATH)

You can download Tesseract from [here](https://github.com/tesseract-ocr/tesseract).

### Install Python Packages

Install the required Python packages using pip:

```bash
pip install opencv-python pytesseract numpy
```

## Usage

1. **Clone the repository:**

```bash
git clone <repository-url>
cd sudoku_solver
```

2. **Run the solver:**

```bash
python main.py
```

3. **Choose the input method:**

- (I)mage: Provide the path to the Sudoku image.
- (L)ist of lists: Provide the Sudoku board as a list of lists.

## Example

### Using an Image

1. Save your Sudoku puzzle image (e.g., `sudoku.jpg`).
2. Run the solver:

```bash
python main.py
```

3. Enter `i` for image and provide the image path when prompted:

```
Would you like to use an (I)mage or (L)ist of lists?: i
Enter Image Path: "sudoku.jpg"
```

### Using a List of Lists

1. Run the solver:

```bash
python main.py
```

2. Enter `l` for list of lists and provide the board when prompted:

```
Would you like to use an (I)mage or (L)ist of lists?: l
Enter your list of lists here: [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], ...]
```

## Note

- Ensure Tesseract OCR is properly installed and configured on your system.
- Adjust the preprocessing steps in `extract_sudoku.py` if OCR accuracy needs improvement based on your images.

---

# File Descriptions

## `extract_sudoku.py`

This file contains the `extract_sudoku` function that performs the following steps:

1. Loads the input image in grayscale.
2. Applies Gaussian blur to reduce noise.
3. Uses adaptive thresholding to convert the image to a binary format.
4. Finds the largest contour, which should be the Sudoku board.
5. Performs a perspective transform to get a top-down view of the Sudoku board.
6. Divides the board into 9x9 cells and uses Tesseract OCR to recognize digits.
7. Returns the recognized Sudoku board as a list of lists.

## `solver.py`

This file contains the Sudoku solver functions:

- `check_row`: Checks if a number already exists in a given row.
- `check_column`: Checks if a number already exists in a given column.
- `check3x3`: Checks if a number exists in the 3x3 subgrid.
- `check_validity`: Validates if a number can be placed in a specific cell.
- `find_empty`: Finds the first empty cell in the board.
- `fill_cell`: Attempts to fill an empty cell with a valid number.
- `solve_sudoku`: Solves the Sudoku puzzle using a backtracking algorithm.

## `main.py`

This is the main entry point for the Sudoku solver. It interacts with the user to get the input type (image or list of lists) and calls the appropriate functions to extract and solve the Sudoku puzzle.

