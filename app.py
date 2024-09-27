import cv2
import easyocr
import numpy as np
import gradio as gr

def load_and_preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return image, binary_image

def extract_words(image):
    reader = easyocr.Reader(['en'])
    results = reader.readtext(image, detail=1)
    filtered_results = [(bbox, text, conf) for bbox, text, conf in results if conf > 0.75]
    return filtered_results

def search_and_draw_boxes(image, results, search_texts):
    output_image = image.copy()
    search_keywords = [s.strip() for s in search_texts.split('|')]

    # Define different colors for different search keywords
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (0, 255, 255)]
    keyword_color_mapping = {keyword: colors[i % len(colors)] for i, keyword in enumerate(search_keywords)}

    for (bbox, detected_text, _) in results:
        words = detected_text.split()
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        word_width = bottom_right[0] - top_left[0]

        for word in words:
            for search_text in search_keywords:
                if search_text.lower() in word.lower():
                    word_start_index = detected_text.index(word)
                    num_words = len(words)
                    width_per_word = word_width // num_words
                    word_x = top_left[0] + (word_start_index * width_per_word)
                    word_y = top_left[1]

                    # Use different colors for each keyword
                    color = keyword_color_mapping[search_text]
                    cv2.rectangle(output_image, (word_x, word_y), 
                                  (word_x + width_per_word, bottom_right[1]), 
                                  color, 2)  # Box with assigned color
                    break

    return output_image

def ocr_keyword_search(image, search_texts):
    image_array = np.array(image)
    image_cv = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    word_results = extract_words(image_cv)
    detected_text = " ".join([text for (_, text, _) in word_results])
    output_image = search_and_draw_boxes(image_cv, word_results, search_texts)
    output_image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
    return detected_text, output_image_rgb

gr_interface = gr.Interface(
    fn=ocr_keyword_search,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Enter Keywords (separate by '|')")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Image(label="Output Image with Highlighted Text")
    ],
    title="OCR and Multi-Keyword Search",
    description="Upload an image with text, search for multiple keywords (separate by '|'). Each keyword will be highlighted with a different color."
)

if __name__ == "__main__":
    gr_interface.launch()

