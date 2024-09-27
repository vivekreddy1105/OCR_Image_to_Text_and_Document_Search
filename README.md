# OCR and Document Search Web Application

## Overview
This project implements a web-based prototype that performs Optical Character Recognition (OCR) on uploaded images containing text in both Hindi and English. Users can upload an image, extract text using OCR, and perform keyword searches within the extracted text. The application is developed using Python and deployed using Gradio.

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

3. Access the application at `http://localhost:7860` in your web browser.

## Usage
- **Upload an Image**: Click on the "Upload Image" button to select an image file containing text.
- **Enter Keywords**: Input keywords separated by the pipe character (`|`) to search within the extracted text.
- **View Results**: The application displays the extracted text and highlights the matching keywords in the uploaded image.

## Deployment
This application is deployed on [Gradio](https://gradio.app) and can be accessed via the following link:
[Live Web Application](https://huggingface.co/spaces/vivekreddy1105/OCR_Image_to_Text_and_Document_Search)
