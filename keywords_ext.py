from configparser import ConfigParser
from src.main import Extractor
config = ConfigParser()
config.read('config.ini')
config_default = config['DEFAULT']
extractor = Extractor(config_default,'vi')


def  extracting(document:str,num_keywords:int):
    return {"keywords": extractor.run(document,num_keywords)}
keywords = extracting("""


(Dân trí) - Máy bay ném bom chiến lược B-52 của Mỹ phóng thành công một tên lửa siêu vượt âm trong cuộc thử nghiệm quan trọng với Không quân nước này, sau một số lần bắn thử không thành công trước đó.
Pháo đài bay Mỹ lần đầu phóng thành công tên lửa siêu vượt âm hoàn chỉnh - 1
Máy bay ném bom chiến lược B-52H (Ảnh: Không quân Mỹ)

Không quân Mỹ ngày 12/12 thông báo, một máy bay B-52H của nước này đã phóng một tên lửa siêu vượt âm hoàn chỉnh. Đây là lần đầu tiên một máy bay ném bom Mỹ phóng ra nguyên mẫu tên lửa AGM-183A có đủ các tính năng sau một số vụ thử không thành công và trong bối cảnh Washington nhiều lần thừa nhận đang bị chậm chân so với đối thủ Nga - Trung Quốc trong cuộc đua vũ khí siêu vượt âm.

Theo thông báo, B-52H đã phóng Vũ khí phản ứng nhanh phóng từ trên không (ARRW) AGM-183A khi bay ở khu vực duyên hải California hôm 9/12.

Sau khi quả tên lửa rời khỏi B-52, nó đạt tốc độ nhanh gấp 5 lần tốc độ âm thanh - một điều kiện để vũ khí được xem là siêu vượt âm. Tên lửa đã hoàn thành đúng đường bay và phát nổ ở khu vực mục tiêu.

Pháo đài bay Mỹ lần đầu phóng thành công tên lửa siêu vượt âm hoàn chỉnh - 2
Cận cảnh tên lửa AGM-183A (Ảnh: Quân đội Mỹ).

"Đội ngũ phát triển ARRW đã thiết kế và thử nghiệm thành công tên lửa siêu vượt âm phóng từ trên không trong 5 năm. Tôi vô cùng tự hào về sự kiên trì và cống hiến mà nhóm này đã thể hiện để mang lại một năng lực quan trọng cho quân đội chúng ta", Chuẩn tướng Jason Bartolomei, giám đốc điều hành Chương trình Vũ khí, cho biết trong tuyên bố.

Nhà sản xuất vũ khí Lockheed Martin cho biết "thử nghiệm mới nhất này cho thấy thiết kế của ARRW và thể hiện khả năng của nó ở tốc độ siêu vượt âm".

ARRW là vũ khí siêu vượt âm thông thường độc lập có thể được phóng từ máy bay ném bom B-52 và "được thiết kế để tấn công mặt đất có giá trị cao".

ARRW đã trải qua 3 lần thử nghiệm thất bại vào năm 2021 do các sự cố trong quá trình phóng tên lửa, nhưng nó đã có 2 lần thử nghiệm thành công trong năm nay.

Không giống tên lửa đạn đạo di chuyển theo quỹ đạo parabol đã định, vũ khí siêu vượt âm có khả năng cơ động cao hơn và tạo ra những thách thức lớn hơn đối với hệ thống phòng không truyền thống.

Trong vài năm qua, Mỹ nhiều lần thừa nhận bị chậm hơn Nga và Trung Quốc trong cuộc đua chế tạo dòng vũ khí có thể bay nhanh gấp ít nhất 5 lần tốc độ âm thanh (6.174 km/h).

Nga hiện đã đưa vào biên chế dòng tên lửa Kinzhal (nhanh gấp 10 lần tốc độ âm thanh) hay Avangard (nhanh gấp 27 lần tốc độ âm thanh), trong khi Trung Quốc cũng đã triển khai tên lửa siêu vượt âm. Mặt khác, Mỹ vẫn đang trong giai đoạn phát triển vũ khí này.
""",
    12)
print(keywords)