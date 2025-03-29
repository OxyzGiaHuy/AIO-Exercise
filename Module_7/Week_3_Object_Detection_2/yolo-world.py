from ultralytics import YOLOWorld
from ultralytics.engine.results import Boxes
from utils import save_detection_results

model = YOLOWorld("yolov8s-world.pt")

model.set_classes(
    ["person", "phone", "mask"] 
) # <--------- Change this to the class you want to detect

# Execute prediction on an image
results: Boxes = model.predict(
    "./samples/vietnam-3.jpg", max_det=100, iou=0.01, conf=0.01
)

# Save detection results as images
save_detection_results(results)