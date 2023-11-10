# Import the OCR function from the sudoku_ocr module.
from sudoku_ocr import extract_sudoku

# Define a function to check if a number already exists in the given row.
def check_row(num, board, row_index):
    return num in board[row_index]

# Define a function to check if a number already exists in the given column.
def check_column(num, board, index):
    return any(row[index] == num for row in board)

# Define a function to check if a number is in the 3x3 subgrid that contains the (row_index, column_index) cell.
def check3x3(num, board, row_index, column_index):
    start_row = row_index - row_index % 3
    start_col = column_index - column_index % 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return True
    return False

# This function checks if a number can be legally placed at the (row, column) position on the board.
def check_validity(number, board, row, column):
    # The number is valid only if it is not found in the same row, column, and 3x3 subgrid.
    if check_row(number, board, row) or check_column(number, board, column) or check3x3(number, board, row, column):
        return False
    return True

# This function finds the first empty cell in the board, which is represented by a 0.
def find_empty(board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == 0:  # 0 is used to represent an empty cell.
                return (i, j)  # Return the coordinates of the empty cell.
    return None

# This function attempts to fill an empty cell with a valid number.
def fill_cell(board, row, column):
    for num in range(1, 10):  # Try all numbers from 1 to 9.
        if check_validity(num, board, row, column):
            board[row][column] = num
            if not find_empty(board) or solve_sudoku(board):
                return True
            board[row][column] = 0  # Reset the cell if no number fits (backtrack).
    return False

# This function solves the Sudoku puzzle using a backtracking algorithm.
def solve_sudoku(board):
    coor = find_empty(board)
    if not coor:
        return True  # If there are no empty cells, the puzzle is solved.
    row, col = coor
    for num in range(1, 10):  # Try to fill the cell with a valid number.
        if check_validity(num, board, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return board  # If the puzzle is solved, return the board.
            board[row][col] = 0  # Otherwise, reset the cell (backtrack).
    return False

# Main function to interface with the user and solve the Sudoku puzzle.
def Solver():
    # Ask the user if they want to solve a puzzle from an image or a list of lists.
    SolveType = input('Would you like to use an (I)mage or (L)ist of lists?: ').lower()
    if SolveType == "l":
        board = input('Enter your list of lists here: ')
        board = eval(board)  # Convert the string input into a list of lists.
        solve_sudoku(board)  # Solve the Sudoku puzzle.
    elif SolveType == "i":
        imagePath = input('Enter Image Path: ')
        board = extract_sudoku(imagePath)  # Extract the Sudoku puzzle from the image.
        solve_sudoku(board)  # Solve the Sudoku puzzle.
    return board  # Return the solved board.

# Print the result of the Solver function.
print(Solver())
