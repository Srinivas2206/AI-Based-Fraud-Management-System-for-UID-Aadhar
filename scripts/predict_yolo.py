import os
import cv2
from ultralytics import YOLO

# Paths
MODEL_PATH = "models/yolo/best.pt"
TEST_IMAGES_DIR = "data/images/val"
OUTPUT_DIR = "results/predictions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load YOLO model
model = YOLO(MODEL_PATH)

# Run predictions
def predict_images():
    for img_file in os.listdir(TEST_IMAGES_DIR):
        img_path = os.path.join(TEST_IMAGES_DIR, img_file)
        results = model(img_path)
        
        # Save annotated image
        annotated_img = results[0].plot()  # Annotated image
        output_path = os.path.join(OUTPUT_DIR, f"pred_{img_file}")
        cv2.imwrite(output_path, annotated_img)
        
        # Print detected bounding boxes
        print(f"Predictions for {img_file}:")
        print("Bounding Boxes:", results[0].boxes.xyxy.tolist())
        print("Labels:", results[0].boxes.cls.tolist())
        print("Confidences:", results[0].boxes.conf.tolist())

if __name__ == "__main__":
    predict_images()
