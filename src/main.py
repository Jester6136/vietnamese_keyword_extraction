from utils.preprocessing import get_stopword,preprocessing
import pandas as pd
import math
import py_vncorenlp

class extractor():
    def __init__(self,config):
        self.stopwords = get_stopword(config['stopwords_path'])
        self.annotator = py_vncorenlp.VnCoreNLP(annotators=["pos"], save_dir=config['vncore_path'])

    def run(self,document,num_keywords):
        tokens = preprocessing(document,self.stopwords,self.annotator)
        # Calculate the position weights of the filtered words using a combination of linear and logarithmic scales
        max_position = len(tokens)
        position_weights = [ i / max_position + (1 - math.log(i + 1) / math.log(max_position)) for i, word in enumerate(tokens)]

        tf = {}
        for i,token in enumerate(tokens):
            if token[0].isupper():
                weight = 1.8  # Assign a weight of 1.8 to uppercase tokens
            else:
                weight = 1  # Assign a weight of 1 to lowercase tokens
            tf[token] = tf.get(token, 0) + weight * position_weights[i]

        # Calculate IDF and TF-IDF
        idf = {}
        for token in set(tokens):
            idf[token] = 1  # Set IDF to 1 for simplicity
        tfidf = {}
        for token, freq in tf.items():
            tfidf[token] = freq * idf[token]

        # Get top keywords
        df = pd.DataFrame(tfidf.values(), index=tfidf.keys(), columns=["tfidf_scores"])
        df = df.sort_values(by=['tfidf_scores'], ascending=False)
        top_keywords = list(df.index[:num_keywords])
        return top_keywords

if __name__=='__main__':
    extractor1 = extractor()
    keywords = extractor1.run("""Năm trung tâm đăng kiểm ở Hà Nội được mở cửa trở lại từ sáng 13/3 sau thời gian tạm đóng, nâng tổng số đơn vị hoạt động lên 13.

    Đó là trung tâm 2903V phường Láng Thượng, quận Cầu Giấy; 2907D ở Du Nội, Đông Anh; 2011D ở Đông Sơn, Chương Mỹ; 2917D phường Thạch Bàn, Long Biên; và 2918D ở thị xã Sơn Tây.

    Từ sáng sớm, hàng trăm phương tiện đã đến trước trung tâm 2903V xếp hàng chờ kiểm định. Ông Nguyễn Văn Bình, phố Hàng Vôi cho biết, xe ông đã hết hạn kiểm định gần một tuần phải để lại cơ quan thuộc quận Cầu Giấy, hàng ngày đi làm bằng xe máy. Sáng nay, nghe tin trung tâm 2903V mở lại nên ông vội vàng đưa xe đến xếp hàng.

    "Tôi đã nhận được số thứ tự kiểm định trong ngày. Thật may mắn vì tôi đang đau đầu tìm nơi đăng kiểm, dự định sang các tỉnh lân cận song nghe tin chỗ nào cũng đông", ông Bình cho hay.
    Phương tiện đổ về trung tâm 2903V ngay sau khi mở cửa sáng 13/3. Ảnh: Anh Duy

    Phương tiện đổ về trung tâm 2903V đầu giờ sáng 13/3. Ảnh: Anh Duy

    Bên trong đơn vị này, 5 đăng kiểm viên làm việc trên một dây chuyền. Hai cảnh sát giao thông hỗ trợ kiểm tra giấy tờ, số khung, số máy, kích cỡ xe và phân luồng xe vào trạm. Thời gian kiểm định 30-35 phút mỗi xe ôtô 4 chỗ. Dự kiến hôm nay trung tâm tiếp nhận khoảng 100 xe.

    Để nâng công suất tiếp nhận phương tiện, ông Trần Quốc Hoan, phụ trách trung tâm đang huy động nhân lực, cố gắng mở thêm một dây chuyền kiểm định vào ngày mai. Đơn vị cũng sẽ phát phiếu hẹn theo biển số xe, có khung giờ để chủ phương tiện đến kiểm định, tránh xếp hàng gây ùn tắc ngoài trung tâm.

    Phó cục trưởng Đăng kiểm Việt Nam Nguyễn Vũ Hải cho biết, sự hỗ trợ của lực lượng cảnh sát giao thông giúp hoạt động đăng kiểm dần ổn định. Sắp tới, Bộ Quốc phòng cũng sẽ cử nhân lực giúp các trung tâm đăng kiểm trong thời gian khoảng một tháng.
    Cảnh sát giao thông hỗ trợ đăng kiểm viên kiểm tra xe. Ảnh: Anh Duy

    Cảnh sát giao thông hỗ trợ đăng kiểm viên kiểm tra xe. Ảnh: Anh Duy

    Chuỗi cáo buộc sai phạm của ngành đăng kiểm bắt nguồn từ giữa tháng 12/2022, khi cảnh sát giao thông TP HCM chặn một xe tải, cho rằng sai số trong dữ liệu đăng kiểm và vạch trần thủ đoạn phi pháp của các trung tâm. Khoảng 3 tháng sau đó, công an trên cả nước liên tiếp điều tra sai phạm trong hoạt động đăng kiểm, khởi tố gần 500 người của hơn 70 trung tâm về các tội: Nhận hối lộ, Môi giới hối lộ, Giả mạo trong công tác và Sản xuất, mua bán công cụ, phần mềm để sử dụng vào mục đích trái pháp luật.

    Trong bối cảnh thiếu hụt nhân sự nghiêm trọng, lượng xe dự kiến quá hạn kiểm định tháng 3 tại Hà Nội lớn (78.640), các trung tâm đăng kiểm chỉ đáp ứng được 14% nhu cầu. Tại TP HCM, lượng xe bị quá hạn dự kiến 29.940, khả năng đáp ứng của đơn vị đăng kiểm chỉ 49% nhu cầu.

    Tình trạng ùn tắc tại các đơn vị đăng kiểm những ngày qua diễn ra nghiêm trọng, nhiều chủ xe phải đợi 2-3 ngày mới đến lượt, các đăng kiểm viên đều phải làm việc tăng ca, thêm giờ.""",
    12)
    print(keywords)