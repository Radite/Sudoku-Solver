from sudoku_ocr import extract_sudoku
from solver import solve_sudoku
import numpy as np

# Main function to interface with the user and solve the Sudoku puzzle.
def Solver():
    try:
        SolveType = input('Would you like to use an (I)mage or (L)ist of lists?: ').lower()
        if SolveType == "l":
            board = input('Enter your list of lists here: ')
            board = eval(board)  # Convert the string input into a list of lists.
            print("Solving Sudoku from list of lists:")
            print(np.array(board))
            solve_sudoku(board)  # Solve the Sudoku puzzle.
        elif SolveType == "i":
            imagePath = input('Enter Image Path: ').strip('"')  # Remove surrounding quotes if present
            print(f"Attempting to solve Sudoku from image path: {imagePath}")
            board = extract_sudoku(imagePath)  # Extract the Sudoku puzzle from the image.
            if board:
                print("Sudoku board extracted from image:")
                print(np.array(board))
                solve_sudoku(board)  # Solve the Sudoku puzzle.
                print("Solved Sudoku board:")
                print(np.array(board))
            else:
                print(f"Failed to extract Sudoku from image path: {imagePath}")
        return board  # Return the solved board or None if not solved.

    except Exception as e:
        print(f"Exception occurred in Solver function: {str(e)}")
        return None

# Print the result of the Solver function.
if __name__ == "__main__":
    print(Solver())
