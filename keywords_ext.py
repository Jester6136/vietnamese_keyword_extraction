from configparser import ConfigParser
from src.main import Extractor
config = ConfigParser()
config.read('config.ini')
config_default = config['DEFAULT']
extractor1 = Extractor(config_default,'vi')
extractor2 = Extractor(config_default,'en')
def  extracting(document:str,num_keywords:int,lang:str):
    if lang =='vi':
        return {"keywords": extractor1.run(document,num_keywords)}
    if lang =='en':
        return {"keywords": extractor2.run(document,num_keywords)}

keywords = extracting("""

Đây là bản thiết kế hàng tỉ đô-la của Bộ Quốc phòng mới nhất New Mexico với giá 23 tỉ đô-la của Hợp chủng quốc Hoa Kỳ. Thông báo chính phủ Ấn Độ cho biết Ủy ban quốc phòng đã phê chuẩn 24 thiết bị dự trữ của Bộ Quốc phòng, 21 nước Mỹ đã có một khoản thu nhập cao hơn 7 triệu đô. Theo tuyên bố, số tiền này sẽ được dùng để mua cho quân đội Ấn Độ, xe tăng, vũ khí hạng nhẹ, và máy bay vũ khí hạng nặng để chế tạo bom hạt nhân mới cho không quân Ấn Độ. Hơn nữa, những thiết bị quân sự còn lại trong danh sách quân sự bao gồm các tên lửa của Hải quân, vận chuyển hàng, vận chuyển tàu và máy bay tự động theo thời gian. Nhiều năm qua, các thiết bị của Ấn Độ đã gây ra một căn bệnh lây lan trên đất Ấn Độ, và cả nước Ấn Độ cũng nghi ngờ việc cung cấp vũ khí phòng thủ quốc gia. Những nhà phê bình địa phương cho biết vũ khí sản xuất quốc gia không đủ mạnh, và có rất nhiều cơ hội để tham nhũng. Ít nhất Ấn Độ đã xảy ra bảy vụ mua chuộc hạng nặng từ khi xuất ngũ.





""",
    10,'vi')
print(keywords)