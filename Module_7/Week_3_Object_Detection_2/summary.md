# Key Ideas về Object Detection & Tracking

## 1. Object Tracking (Bài toán 1)
- **track_id**: Dùng để phân biệt các đối tượng khi di chuyển qua nhiều khung hình.
- **Hàm `draw_tracks`**: Vẽ đường nối theo quỹ đạo di chuyển của đối tượng qua các khung hình.
- **Batching (phiên bản optimized)**: Giúp tăng tốc độ và hiệu suất xử lý.
- **Hàm `process_batch`**: Trả về `results`, chứa thông tin về `boxes` và `track_ids`.
- **Tối ưu hiệu suất**: Áp dụng batching để xử lý nhiều khung hình trong một lần suy luận.

## 2. Object Counting (Bài toán 2)
- **Ứng dụng thực tế**: Đếm số lượng các đối tượng trong một vùng hoặc khung hình.
- **Biến `region_points`**: Xác định khu vực hoặc đường kẻ dùng để đếm đối tượng.
- **Thư viện `ultralytics.solutions`**: Dùng `ObjectCounter` để đếm số lượng đối tượng.
- **Thiết lập video đầu vào/ra**: Sử dụng `cv2.VideoCapture` và `cv2.VideoWriter`.

## 3. Open Vocabulary Detection (Bài toán 3)
- **Khả năng phát hiện đối tượng**: Cho phép phát hiện các đối tượng không có trong danh sách nhãn cố định.
