from ultralytics import YOLO

def train_yolo(model_path="yolo11n.pt", data_path="data/data.yaml", epochs=20, img_size=640):
    model = YOLO(model_path)  # Load YOLO model
    model.train(data=data_path, epochs=epochs, imgsz=img_size)  # Train
    print("Training completed!")

if __name__ == "__main__":
    train_yolo()
