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
   git clone https://github.com/yourusername/ocr-document-search.git
   cd ocr-document-search
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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
[Live Web Application](https://your-gradio-url)

## Deliverables
1. **Code**: The Python scripts for the web application, including OCR processing and search functionality.
2. **README File**: This documentation file explaining setup and usage.
3. **Extracted Text Output**: JSON or plain text output of the extracted text from the uploaded image.
4. **Search Functionality Demonstration**: A demonstration of the search functionality with example keywords.

## Evaluation Criteria
- **Accuracy**: Effectiveness of the OCR model in extracting text from both Hindi and English sections.
- **Functionality**: Correct handling of image uploads, text extraction, and keyword searches.
- **User Interface**: Simplicity and intuitiveness of the web interface.
- **Deployment**: Reliable online accessibility of the application.
- **Clarity**: Well-structured documentation and code.
- **Completeness**: Submission of all deliverables demonstrating required functionality.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) for the OCR implementation.
- [OpenCV](https://opencv.org/) for image processing functionalities.
- [Gradio](https://gradio.app/) for easy web interface creation.
```

### Notes:
- Make sure to replace `https://github.com/yourusername/ocr-document-search.git` with the actual URL of your GitHub repository.
- Update the Gradio deployment URL with the live link of your application.
- Feel free to modify any section to better fit your project specifics.
