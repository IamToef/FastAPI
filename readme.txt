Task của Ming Hieeus:
Thực hiện outline theo pipeline sau:

DETECTION & TRACKING: dùng luôn YOLOv8 để nhận dạng khuôn mặt đồng thời track theo khuôn mặt của họ 
Níu z thì mình chỉ cần thực hiện nhận diện khi có người mới được nhận dạng hoặc là khi cái lúc track nhận diện cái j đó quan trọng
(giả sử như sau 1 số lượng frame nhất định hoặc đối tượng nhận dạng có sự thay đổi lớn)

FACE CROPPING: Một khi có người được nhận diện, cắt vùng mặt trong 1 bounding box của YOLOv8. Hãy chắc chắn rằng cái vùng mặt đủ lớn để chứa cả khuôn mặt
(Make sure the face region is large enough to include the entire face).

FACE RECOGNITION: Chỉ áp dụng FaceNet cho cái vùng mặt đc cắt ra. Nếu bạn có cái tracking ID cho mỗi người, có thể giảm số lần thực hiện nhận diện bằng cách
giữ cái cache của các khuôn mặt đc nhận diện và ID tương ứng (ID ở đây có thể là MSSV hoặc cái gì đó, này tui hong có rõ lém)




Task của Trúc Giang:
Hãy tìm các cách khác nhau để thực hiện các task sau:
LABEL ASSIGNMENT: sau khi nhận diện thì label tên khuôn mặt tương ứng.

Tối ưu  (OPTIMIZATION):
1. Có thể dùng 1 mô hình nhận diện khuôn mặt khác (Trong trường hợp FaceNet chạy ko thỏa mãn ý của tụi mình) (Cái này optional)
2. Implement 1 cái cơ chế skip khung khi khuôn mặt không thay đổi quá nhiều, hoặc gần như không đổi (Required)
3. Dùng 1 cái frame rate nhỏ hơn cho việc nhận diện khuôn mặt trong khi vẫn giữ 1 frame rate lớn khi track cũng như nhận diện đối tượng