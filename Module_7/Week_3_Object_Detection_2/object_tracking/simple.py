from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO11 model
model = YOLO("yolo11l.pt")

# Open video
video_path = "../samples/vietnam.mp4"
cap = cv2.VideoCapture(video_path)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Create VideoWriter object
video_name = video_path.split("/")[-1]
output_path = f"../run/{video_name.split('.')[0]}_tracked.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v") # Codec: MP4 -> FourCC: m,p,4,v
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# track history
track_history = defaultdict(lambda: [])

# Loop through video frames
while cap.isOpened():
    # Read a frame
    success, frame = cap.read()

    if success:
        # Run YOLO11 tracking on the frame, 
        # persisting tracks between frames
        results = model.track(frame, persist = True, show = False)

        # Get boxes and track IDs (with error handling)
        boxes = results[0].boxes.xywh.cpu()
        try:
            track_ids = results[0].boxes.id
            if track_ids is not None:
                track_ids = track_ids.int().cpu().tolist()
            else:
                track_ids = [] # No tracks found
        except AttributeError:
            track_ids = [] # Handle case where tracking fails
        
        # Visualize result
        annotated_frame = results[0].plot()

        # Plot tracks only if having valid tracking data
        if track_ids:
            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y))) # center point

                if len(track) > 120: # retain 30 tracks for 30 frames
                    track.pop(0)
                
                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(
                    annotated_frame,
                    [points],
                    isClosed = False,
                    color = (230, 230, 230),
                    thickness = 4
                )
        # Write frame to output video
        out.write(annotated_frame)
    else:
        # Break loop at the end of video
        break

# Release everything
cap.release()
out.release()
print(f"Video has been saved to {output_path}")