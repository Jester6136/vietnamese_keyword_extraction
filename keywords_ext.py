from configparser import ConfigParser
from src.main import Extractor
config = ConfigParser()
config.read('config.ini')
config_default = config['DEFAULT']
extractor = Extractor(config_default,'vi')


def  extracting(document:str,num_keywords:int):
    return {"keywords": extractor.run(document,num_keywords)}
keywords = extracting("""
So với U23 Malaysia, U23 Việt Nam được đánh giá cao hơn, nhưng đội bóng của HLV Hoàng Anh Tuấn không thể xem thường đối thủ có lối đá đầy khó chịu.
*Trận đấu giữa U23 Việt Nam và U23 Malaysia sẽ diễn ra lúc 16h00 ngày 24/8, trên sân vận động tỉnh Rayong (Thái Lan), Dân trí sẽ tường thuật trực tuyến trận đấu này.

Thật ra việc U23 Việt Nam được đánh giá cao hơn so với U23 Malaysia cũng chỉ là về lý thuyết, xuất phát từ chỗ đội hình của chúng ta khá ổn định, với nòng cốt gồm các cầu thủ từng có mặt tại SEA Games 32.

Còn trên thực tế, đội nào mạnh hơn đội nào ở giải đấu năm nay còn phải chờ trận quyết đấu sắp diễn ra. U23 Malaysia hiện có lợi thế rất lớn về mặt tinh thần, ở chỗ đội bóng của HLV Elavarasan đã đánh bại đại kình địch U23 Indonesia ở vòng bảng.

U23 Việt Nam - U23 Malaysia (16h ngày 24/8): Thẳng tiến vào chung kết? - 1
U23 Việt Nam sẽ vào chung kết? (Ảnh: Minh Quân).


Mỗi khi các đại diện của bóng đá Malaysia đánh bại các đại diện của bóng đá Indonesia, họ luôn có thêm sự tự tin.

Đấy là chưa kể U23 Malaysia có một vài sự bổ sung quan trọng ở giải U23 Đông Nam Á so với SEA Games 32. Nổi bật nhất trong số này là tiền vệ sinh ra tại Scotland Fergus Tierney, người ghi cả hai bàn thắng cho U23 Malaysia vào lưới Indonesia ở vòng bảng.

Ngoài ra, HLV Elavarasan của U23 Malaysia là người tinh quái, ông có nhiều chiêu bài khác nhau để đối thủ lộ ra các nhược điểm, trước khi U23 Malaysia khai thác vào các nhược điểm đấy.

Không phải ngẫu nhiên mà HLV Elavarasan đánh giá rất cao người đồng nghiệp Hoàng Anh Tuấn bên phía U23 Việt Nam.

U23 Việt Nam - U23 Malaysia (16h ngày 24/8): Thẳng tiến vào chung kết? - 2
U23 Malaysia không hề yếu (Ảnh: FAM).

HLV Hoàng Anh Tuấn là người giỏi đọc trận đấu, có nhiều kinh nghiệm cầm quân kể cả ở các giải đấu trẻ lẫn sân chơi đỉnh cao (ông Tuấn từng dẫn dắt các đội Khánh Hòa và Hải Phòng tại V-League). HLV Hoàng Anh Tuấn sẽ biết cách kiềm chế các cầu thủ của mình, tránh cho họ không sa vào những đòn khiêu khích của Malaysia.

Đấy cũng là lý do mà ông Tuấn phản ứng khá mạnh trước những pha gây hấn liên tục của Nguyễn Văn Trường với cầu thủ Philippines hôm 22/8. Nếu những tình huống gây hấn này rơi vào trận bán kết với U23 Malaysia, cầu thủ Việt Nam có thể bị đối thủ khiêu khích rồi rơi vào thế bất lợi.

Nhược điểm khác của U23 Việt Nam chính là vị trí của thủ môn Quan Văn Chuẩn. Dù là cựu binh, đeo băng đội trưởng của U23 Việt Nam, dù có kinh nghiệm ở giải U23 Đông Nam Á năm ngoái và SEA Games 32 năm nay, nhưng Quan Văn Chuẩn thi đấu không hề an toàn.

Thủ thành này bắt bóng bổng rất kém. Những pha phán đoán điểm rơi không chính xác của Quan Văn Chuẩn thường xuyên lặp đi lặp lại, chứng tỏ có thể đây không phải là vấn đề kinh nghiệm hay tâm lý, mà xuất phát từ chính khâu chuyên môn của thủ thành Quan Văn Chuẩn: Năng lực khống chế bóng bổng hạn chế.

Không loại trừ khả năng HLV Hoàng Anh Tuấn sẽ sử dụng thủ môn khác cho trận bán kết với Malaysia, để đảm bảo an toàn cho hàng thủ.

Trận đấu với U23 Malaysia là trận đấu có tính chất khác so với 2 trận vòng bảng. Nhưng như HLV Hoàng Anh Tuấn cho biết, điều quan trọng trong trận đấu này là U23 Việt Nam phát huy tối đa phong độ và năng lực của mình, chúng ta sẽ có chiến thắng.

Dự đoán: U23 Việt Nam thắng 2-1

""",
    10)
print(keywords)