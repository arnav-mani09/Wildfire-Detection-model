from ultralytics import YOLO

# Load the YOLOv13 small model (you can try "yolov13m.pt" or "yolov13n.pt" later)
model = YOLO("weights/yolov13s.pt")

# Train the model (make sure you have a data.yaml file in your project folder)
model.train(
    data="data.yaml",
    epochs=50,
    imgsz=640
)
