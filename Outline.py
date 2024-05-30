from ultralytics import YOLO
import face_recognition
import cv2
import numpy as np

# Tải mô hình YOLOv8 đã huấn luyện sẵn
model = YOLO('yolov8s.pt')  # Sử dụng mô hình YOLOv8 nhỏ đã huấn luyện sẵn

# Hàm nhận diện khuôn mặt
def recognize_face(face_image):
    face_locations = face_recognition.face_locations(face_image)
    face_encodings = face_recognition.face_encodings(face_image, face_locations)
    
    if face_encodings:
        return "Identified Person"
    return "Unknown"

# Giả sử bạn có một trình theo dõi và bộ nhớ đệm khuôn mặt
class SomeTracker:
    def __init__(self):
        self.trackers = {}
        self.next_id = 0

    def update(self, detections):
        # Giả sử phương thức update sẽ cập nhật trackers và trả về danh sách ID
        pass

    def get_id(self, index):
        # Giả sử phương thức này trả về ID của đối tượng được theo dõi
        pass

    def needs_update(self, track_id):
        # Giả sử phương thức này kiểm tra nếu cần cập nhật nhận diện khuôn mặt
        pass

def draw_name_on_frame(frame, name, box):
    x1, y1, x2, y2 = box
    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return frame

def display_or_save_frame(frame):
    # Hiển thị hoặc lưu khung hình
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)

# Khởi tạo trình theo dõi và bộ nhớ đệm khuôn mặt
tracker = SomeTracker()
face_cache = {}

# Giả sử bạn có một danh sách các khung hình video
video_frames = ["tư liệu quý.mp4"]  # Load your video frames herebr

# Xử lý các khung hình video
for frame in video_frames:
    # Phát hiện đối tượng với YOLOv8
    results = model(frame)
    
    for result in results:
        # Lấy các bounding boxes
        boxes = result.boxes.xyxy.numpy()
        for i, (x1, y1, x2, y2, conf, cls) in enumerate(boxes):
            if cls == person_class_id:  # Kiểm tra nếu lớp là người
                track_id = tracker.get_id(i)  # Lấy ID theo dõi cho phát hiện
                
                # Kiểm tra nếu cần chạy nhận diện khuôn mặt
                if track_id not in face_cache or tracker.needs_update(track_id):
                    # Cắt vùng khuôn mặt và chạy nhận diện khuôn mặt
                    face = frame[int(y1):int(y2), int(x1):int(x2)]
                    name = recognize_face(face)
                    
                    # Cập nhật bộ nhớ đệm khuôn mặt
                    face_cache[track_id] = name
                
                # Lấy tên từ bộ nhớ đệm và vẽ nó lên khung hình
                name = face_cache[track_id]
                frame = draw_name_on_frame(frame, name, (int(x1), int(y1), int(x2), int(y2)))

    # Hiển thị hoặc lưu khung hình
    display_or_save_frame(frame)
