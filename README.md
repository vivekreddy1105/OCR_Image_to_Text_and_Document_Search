

# OCR and Document Search Web Application

## Overview
This project implements a web-based prototype that performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. Users can upload an image, extract text using OCR, and perform keyword searches within the extracted text. The application is developed using Python and deployed using Gradio.

### Implementation Idea: Text Recognition and Searching
The implementation of Optical Character Recognition (OCR) for documents like newspapers focuses on structured text recognition. The application identifies distinct text blocks using contour detection, which is essential for handling the scattered text typical in newspaper layouts. Once these blocks are detected, the OCR model extracts text sequentially from left to right, preserving the logical flow and ensuring that the content remains coherent. Users can input one or more keywords, separated by `|`. The application will then search for each keyword throughout the extracted text, disregarding case sensitivity for comprehensive matching. When a keyword is found, the application highlights the matching sections in the output image using distinct colors for each keyword.

## Objectives
- Perform OCR on images to extract text.
- Implement a keyword search functionality based on the extracted text.
- Provide a user-friendly interface for image upload and search.

## Technologies Used
- **EasyOCR**: A library for Optical Character Recognition that supports multiple languages, including Hindi and English.
- **OpenCV**: A library for image processing.
- **Gradio**: A library to create user-friendly web interfaces for machine learning applications.

## Installation

### Environment Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/vivekreddy1105/OCR_Image_to_Text_and_Document_Search/tree/88aad01849473ea8db2785a0fcd7cccdb68892e4
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  
   ```

3. **Install Required Libraries**
   ```bash
   pip install opencv-python easyocr numpy gradio
   ```

## Running the Application
1. Ensure you have activated your virtual environment.
2. Run the application using the following command:
   ```bash
   python app.py
   ```

## Usage
- **Upload an Image**: Click on the "Upload Image" button to select an image file containing text.
- **Enter Keywords**: Input keywords separated by the pipe character (`|`) to search within the extracted text.
- **View Results**: The application displays the extracted text and highlights the matching keywords in the uploaded image.

## Code Explanation
The core functionality of the application is implemented in `app.py` as follows:

### Key Functions:
- **sort_contours**: Sorts detected contours based on their coordinates.
- **are_in_same_paragraph**: Determines if two bounding boxes belong to the same paragraph.
- **load_and_preprocess_image**: Loads the image and converts it to a binary format suitable for text extraction.
- **extract_text_with_paragraphs**: Extracts text from image blocks, organizing it into paragraphs.
- **extract_words**: Extracts individual words from the image for keyword searching.
- **search_and_draw_boxes**: Highlights keywords in the output image.
- **check_keywords_status**: Checks and returns the status of keywords in the extracted text.
- **ocr_keyword_search**: Main function that orchestrates the OCR and keyword search process, returning the extracted text and processed image.



## Deployment
This application is deployed on [Gradio](https://gradio.app) and can be accessed via the following link:
[Live Web Application](https://huggingface.co/spaces/vivekreddy1105/OCR_Image_to_Text_and_Document_Search)
