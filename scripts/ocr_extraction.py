import os
import numpy as np
import easyocr
from PIL import Image
import json

# Paths
PREDICTIONS_DIR = "results/predictions"
TEST_IMAGES_DIR = "data/images/val"
OCR_RESULTS_DIR = "results/extracted_text"
os.makedirs(OCR_RESULTS_DIR, exist_ok=True)

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Extract text from bounding boxes
def extract_text(img_path, bbox):
    img = Image.open(img_path)
    cropped_img = img.crop((bbox[0], bbox[1], bbox[2], bbox[3]))  # Crop using bbox
    text = reader.readtext(np.array(cropped_img))
    return text[0][1] if text else ""

# Process predictions
def process_predictions():
    for pred_file in os.listdir(PREDICTIONS_DIR):
        if not pred_file.endswith(".jpg"):
            continue
        
        img_path = os.path.join(TEST_IMAGES_DIR, pred_file.replace("pred_", ""))
        with open(os.path.join(PREDICTIONS_DIR, pred_file.replace(".jpg", ".json")), "r") as f:
            predictions = json.load(f)
        
        ocr_results = []
        for bbox in predictions["bboxes"]:
            extracted_text = extract_text(img_path, bbox)
            ocr_results.append(extracted_text)
        
        # Save OCR results
        ocr_output_path = os.path.join(OCR_RESULTS_DIR, pred_file.replace(".jpg", ".json"))
        with open(ocr_output_path, "w") as f:
            json.dump(ocr_results, f)

if __name__ == "__main__":
    process_predictions()
