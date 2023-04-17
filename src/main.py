from utils.utils import get_stopword,preprocessing_vi,preprocessing_en,postprocessing
import math
import py_vncorenlp
from configparser import ConfigParser
import spacy
import logging

class Extractor():
    def __init__(self,config,lang):
        self.lang=lang
        if self.lang =='vi':
            self.stopwords = get_stopword(config['stopwords_path'])
            self.annotator = py_vncorenlp.VnCoreNLP(annotators=["pos"], save_dir=config['vncore_path'])
        elif self.lang =='en':
            self.annotator = spacy.load("en_core_web_sm")
        else:
            logging.exception("This language don't supporting now!")

    def run(self,document,num_keywords):
        if self.lang=='vi':
            tokens = preprocessing_vi(document,self.stopwords,self.annotator)
        elif self.lang=='en':
            tokens = preprocessing_en(document, self.annotator)    
        # Calculate the position weights of the filtered words using a combination of linear and logarithmic scales
        max_position = len(tokens)
        if max_position <= 1:
            return document
        position_weights = [ i / max_position + (1 - math.log(i + 1) / math.log(max_position)) for i, word in enumerate(tokens)]

        tf = {}
        for i,token in enumerate(tokens):
            if token[0].isupper():
                weight = 1.8  # Assign a weight of 1.8 to uppercase tokens
            else:
                weight = 1  # Assign a weight of 1 to lowercase tokens
            tf[token] = tf.get(token, 0) + weight * position_weights[i]

        # Get top keywords
        sorter = sorted(tf.items(), key=lambda x:x[1], reverse=True)
        # print(sorter)
        top_keywords = postprocessing(list(dict(sorter).keys()))[:12]
        keywords_resortby_index = sorted(top_keywords, key=lambda x: list(tf.keys()).index(x))
        if self.lang =='vi':
            keywords_resortby_index = list(map(lambda keyword:keyword.replace('_',' '),keywords_resortby_index))
        return keywords_resortby_index

if __name__=='__main__':
    config = ConfigParser()
    config.read('config.ini')
    config_default = config['DEFAULT']
    extractor = Extractor(config_default,'vi')
    keywords = extractor.run("""T(Dân trí) - Chiều nay (17/4), dự kiến lãnh đạo của Cục Quản lý, giám sát bảo hiểm sẽ họp với các doanh nghiệp bảo hiểm nhân thọ sau những phản ánh về chất lượng chăm sóc khách hàng của doanh nghiệp.

Theo dự kiến, chiều nay (17/4), Cục Quản lý, giám sát bảo hiểm (Bộ Tài chính) sẽ có cuộc họp với đại diện các doanh nghiệp bảo hiểm nhân thọ.

Nội dung cuộc họp sẽ xoay quanh 2 vấn đề. Thứ nhất là thực trạng công tác tổ chức hoạt động tư vấn, giới thiệu chào bán sản phẩm bảo hiểm và công tác xử lý các phản ánh của khách hàng tại doanh nghiệp bảo hiểm.

Thứ hai là giải pháp đã và sẽ thực hiện để nâng cao công tác đại lý bảo hiểm và chất lượng dịch vụ khách hàng.

Cuộc họp được tổ chức sau khi Cục này nhận được một số thông tin phản ánh về chất lượng tư vấn, hỗ trợ giao kết hợp đồng bảo hiểm của các đại lý bảo hiểm và chất lượng dịch vụ chăm sóc khách hàng của doanh nghiệp bảo hiểm.

Ngày 12/4, Thứ trưởng Bộ Tài chính Cao Anh Tuấn cũng đã có cuộc họp với Cục Quản lý, giám sát bảo hiểm, Hiệp hội Bảo hiểm và một số đơn vị thuộc Bộ Tài chính liên quan đến vấn đề tư vấn hợp đồng bảo hiểm nhân thọ trong thời gian qua. Theo chỉ đạo tại cuộc họp, các doanh nghiệp bảo hiểm nhân thọ cần rà soát lại quy trình bán các sản phẩm, hạn chế tình trạng nhân viên tư vấn thiếu trung thực với khách hàng.

Trước đó, diễn viên Ngọc Lan đã livestream phản ánh trên mạng xã hội về những bức xúc khi mua bảo hiểm. Ngọc Lan cho biết 3 năm trước mua bảo hiểm của Công ty TNHH Bảo hiểm nhân thọ Aviva Việt Nam (nay đã bán cho Tập đoàn tài chính Manulife và đổi tên thành Công ty TNHH Bảo hiểm nhân thọ MVI - MVI Life) cho mình và con trai, tổng mức phí 700 triệu đồng/năm. Do tin tưởng người tư vấn, nên cô đã ký hợp đồng và nghĩ rằng sau 10 năm sẽ nhận cả gốc và lãi là 10 tỷ đồng. Tuy nhiên, gần đây cô mới biết hợp đồng của mình có thời hạn lên đến 74 năm và của con trai là 42 năm. Bên cạnh đó, do hợp đồng còn bao gồm nhiều khoản bảo hiểm khác đi kèm, nên số tiền mà cô có thể nhận về sẽ ít hơn rất nhiều so với dự kiến.

Hay nghệ sĩ Kim Tử Long mới đây cũng cho biết năm 2018 mua bảo hiểm của Công ty Bảo hiểm nhân thọ Prudential cho con trai với mức giá hơn 40 triệu đồng mỗi năm. Sau 3 năm đóng tiền và dừng đóng, đến năm thứ 5 nghệ sĩ mới phát hiện ra hợp đồng đã bị hủy, mất trắng số tiền đã đóng.""",
    12)
    print(keywords)