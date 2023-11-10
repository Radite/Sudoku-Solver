# Import necessary libraries: OpenCV for image processing and Pytesseract for OCR (Optical Character Recognition).
import cv2
import pytesseract
from pytesseract import Output

# Define a function to extract Sudoku puzzle from a given image path.
def extract_sudoku(image_path):
    # Read the image from the provided path.
    image = cv2.imread(image_path)
    # Convert the image to grayscale, which is necessary for thresholding.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply adaptive thresholding to get a binary image which enhances the grid and digits.
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Invert the image colors; this is to ensure digits are white on a black background, which is a common assumption in OCR.
    invert = cv2.bitwise_not(thresh)
    # Set custom configurations for Tesseract, instructing it to focus on digit recognition.
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    # Perform OCR on the inverted image to extract text details.
    details = pytesseract.image_to_data(invert, config=custom_config, output_type=Output.DICT)

    # Initialize a list to hold the Sudoku grid as a 2D array filled with zeros.
    n_boxes = len(details['text'])
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]
    # Determine the height and width of each cell in the grid.
    height, width = invert.shape
    cell_height = height // 9
    cell_width = width // 9

    # Iterate over all recognized text elements.
    for i in range(n_boxes):
        # Check if the OCR confidence is high enough to consider the text valid (greater than 10 in this case).
        if int(details['conf'][i]) > 10:
            # Extract the bounding box coordinates of the current text element.
            (x, y, w, h) = (details['left'][i], details['top'][i], details['width'][i], details['height'][i])
            # Calculate the row and column indices of the cell where the text is located.
            row_idx = y // cell_height
            col_idx = x // cell_width
            # Strip the text of any whitespace and check if it is a digit.
            text = details['text'][i].strip()
            if text.isdigit():
                # If it is a digit, add it to the corresponding position in the Sudoku grid array.
                sudoku_array[row_idx][col_idx] = int(text)

    # Return the filled-in Sudoku grid array.
    return sudoku_array
