import cv2
import numpy as np
import pytesseract
from pytesseract import Output

# Ensure Tesseract OCR is installed on your system and its path is set correctly
# You can download it from: https://github.com/tesseract-ocr/tesseract

def extract_sudoku(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Apply GaussianBlur to the image to remove noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    
    # Apply adaptive thresholding to get a binary image
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)
    
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour which should be the Sudoku board
    largest_contour = max(contours, key=cv2.contourArea)
    
    # Get the bounding box of the largest contour
    rect = cv2.minAreaRect(largest_contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    # Get the perspective transform for the Sudoku board
    width = height = 450
    dst_pts = np.array([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]], dtype='float32')
    src_pts = np.array(box, dtype='float32')
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(image, M, (width, height))
    
    # Apply adaptive thresholding again to the warped image
    warped_blurred = cv2.GaussianBlur(warped, (5, 5), 0)
    warped_thresh = cv2.adaptiveThreshold(warped_blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY_INV, 11, 2)
    
    # Initialize the Sudoku board
    board = np.zeros((9, 9), dtype=int)
    
    # Define the size of each cell
    cell_size = width // 9
    
    # Iterate over each cell to extract the digits
    for i in range(9):
        for j in range(9):
            # Get the cell region
            cell = warped_thresh[i*cell_size:(i+1)*cell_size, j*cell_size:(j+1)*cell_size]
            
            # Invert the cell colors for better OCR recognition
            cell_inverted = cv2.bitwise_not(cell)
            
            # Use Tesseract OCR to recognize the digit
            config = "--psm 10 -c tessedit_char_whitelist=0123456789"
            text = pytesseract.image_to_string(cell_inverted, config=config, output_type=Output.STRING).strip()
            
            # If OCR recognized a digit, place it in the board
            if text.isdigit():
                board[i, j] = int(text)
    
    return board.tolist()
