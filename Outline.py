from ultralytics import YOLO
import facenet
import tracker

# Load YOLOv8 model
yolo_model = YOLO('yolov8-custom.pt')

# Load FaceNet model
facenet_model = facenet.load_model('facenet-model.h5')

# Initialize tracker
person_tracker = tracker.initialize()

# Process video frames
for frame in video_stream:
    # Detect objects with YOLOv8
    detections = yolo_model.predict(frame)

    # Track persons
    tracks = person_tracker.update(detections)

    # For each person detected
    for track in tracks:
        if track.is_person and track.face_visible:
            # Crop face ROI
            face_roi = crop_face(frame, track.bbox)

            # Recognize face
            name, confidence = facenet_model.recognize(face_roi)

            # If recognition confidence is high, label the track
            if confidence > threshold:
                track.label = name

    # Draw bounding boxes and labels on the frame
    annotated_frame = draw_annotations(frame, tracks)

    # Display or save the annotated frame
    display(annotated_frame)