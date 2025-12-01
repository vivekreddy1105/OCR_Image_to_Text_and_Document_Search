Hugging Face's logo

Spaces:
vivekreddy1105
/
OCR_Image_to_Text_and_Document_Search 

like
0

App
Files
Community
Settings
OCR_Image_to_Text_and_Document_Search
/
app.py

vivekreddy1105's picture
vivekreddy1105
Update app.py
2361647
verified
raw

Copy download link
history
blame
edit
delete

5.09 kB
import cv2
import easyocr
import numpy as np
import gradio as gr

def sort_contours(contours):
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    # Sort by y, then by x coordinate
    sorted_contours = sorted(zip(contours, bounding_boxes), key=lambda b: (b[1][1], b[1][0]))
    return [contour[0] for contour in sorted_contours]

def are_in_same_paragraph(box1, box2, threshold=20):
    _, y1, _, h1 = box1
    _, y2, _, _ = box2
    return (y2 - (y1 + h1)) < threshold
def load_and_preprocess_image(image_data):
    gray = cv2.cvtColor(image_data, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return image_data, binary_image

def extract_text_with_paragraphs(image):
    reader = easyocr.Reader(['en','hi'])  
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    contours, _ = cv2.findContours(dilated_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sort_contours(contours)

    paragraphs = []
    current_paragraph = ""
    prev_box = None
    for contour in sorted_contours:
        x, y, w, h = cv2.boundingRect(contour)
        block = image[y:y+h, x:x+w]
        result = reader.readtext(block)
        block_text = " ".join([res[1] for res in result])

        if prev_box is None or are_in_same_paragraph(prev_box, (x, y, w, h)):
            current_paragraph += " " + block_text.strip()
        else:
            paragraphs.append(current_paragraph.strip())
            current_paragraph = block_text.strip()

        prev_box = (x, y, w, h)
    if current_paragraph:
        paragraphs.append(current_paragraph.strip())
    extracted_text = "\n\n".join(paragraphs)  
    return extracted_text

def extract_words(image):
    reader = easyocr.Reader(['en','hi']) 
    results = reader.readtext(image, detail=1)
    filtered_results = [(bbox, text, conf) for bbox, text, conf in results if conf > 0.70]
    return filtered_results


def search_and_draw_boxes(image, results, search_texts):
    output_image = image.copy()
    search_keywords = [s.strip() for s in search_texts.split('|')]
    if not search_keywords or search_keywords == ['']:
        return output_image

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
                    color = keyword_color_mapping[search_text]
                    cv2.rectangle(output_image, (word_x, word_y),
                                  (word_x + width_per_word, bottom_right[1]),
                                  color, 4)  
                    break

    return output_image

def check_keywords_status(word_results, search_keywords):
    found_keywords = []
    detected_text = " ".join([text for (_, text, _) in word_results])

    for keyword in search_keywords:
        if any(keyword.lower() in word.lower() for (_, word, _) in word_results):
            found_keywords.append(f"{keyword}: found")
        else:
            found_keywords.append(f"{keyword}: not found")

    return found_keywords

def ocr_keyword_search(image, search_texts):
    image_array = np.array(image)
    image_cv = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    _, binary_image = load_and_preprocess_image(image_cv)


    extracted_text = extract_text_with_paragraphs(binary_image)
    if not search_texts.strip():
        return extracted_text, [], None
    word_results = extract_words(image_cv)
    search_keywords = [s.strip() for s in search_texts.split('|')]
    keyword_status = check_keywords_status(word_results, search_keywords)

    output_image = search_and_draw_boxes(image_cv, word_results, search_texts)
    output_image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)


    from PIL import Image
    output_image_pil = Image.fromarray(output_image_rgb)

    return extracted_text, keyword_status, output_image_pil

gr_interface = gr.Interface(
    fn=ocr_keyword_search,
    inputs=[
        gr.Image(type="pil", label=" "),
        gr.Textbox(label="Enter Keywords (separate by '|')")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Keyword Status (Found/Not Found)"),
        gr.Image(label="Output Image with Highlighted Text") 
    ],
    title="OCR",
)

if __name__ == "__main__":
    gr_interface.launch()
