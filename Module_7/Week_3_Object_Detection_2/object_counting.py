import cv2
from ultralytics import solutions

video_path = "./samples/highway.mp4"
cap = cv2.VideoCapture(video_path)
assert cap.isOpened(), "Error reading video file"
w, h, fps = (
    int(cap.get(x))
    for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2. CAP_PROP_FPS)
)

# region points for counting
# region_points = [
#     (430, 700),
#     (1600, 700),
#     (1600, 1080),
#     (430, 1080)
# ]
region_points = [(960, 850), (1920, 850)]

video_name = video_path.split("/")[-1]
output_path = f"./run/{video_name.split('.')[0]}_counted.mp4"
video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init counter
counter = solutions.ObjectCounter(
    show = False,
    region = region_points,
    model = "yolo11x.pt" # model="yolo11n-obb.pt" for object counting using YOLO11 OBB model.
)

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed")
        break
    img = counter.count(img)
    video_writer.write(img)

cap.release()
video_writer.release()
cv2.destroyAllWindows()