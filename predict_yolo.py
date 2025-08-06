from ultralytics import YOLO
from PIL import Image

# Load your trained model
model = YOLO("runs/detect/train2/weights/best.pt")

# Path to the image you want to test
image_path = "datasets/images/val/abc005.jpg"

# Run prediction
results = model.predict(source=image_path, show=True, conf=0.25)

# Optional: save results to file
results[0].save(filename="prediction_output.jpg")

# Keep window open if you're using show=True
input("Press Enter to close...")
