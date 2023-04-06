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
        top_keywords = postprocessing(list(dict(sorter).keys()))[:12]
        return top_keywords

if __name__=='__main__':
    config = ConfigParser()
    config.read('config.ini')
    config_default = config['DEFAULT']
    extractor = Extractor(config_default,'vi')
    keywords = extractor.run("""Vài ngày nay, cộng đồng kinh doanh và những người làm nghề truyền thông, thương hiệu dồn sự chú ý tới câu chuyện ồn ào liên quan đến một nhãn hàng hóa mỹ phẩm là Dược phẩm Hoa Linh. 

Cụ thể, trong sự kiện bán hàng livestream vào tối 4/4 trên kênh TikTok của mình, Võ Hà Linh (một Tiktoker có sức ảnh hưởng lớn) tuyên bố triển khai chương trình quảng bá sản phẩm với giá sốc là 11.000 đồng và 18.000 đồng.

Ngay sau đó, cộng đồng các nhà thuốc đồng loạt phản ứng gay gắt do hiện nay họ đang phân phối hai sản phẩm trên với giá 71.000 đồng và 76.000 đồng. Việc livestream này khiến một bộ phận khách hàng của doanh nghiệp cho rằng từ trước đến nay họ bị các nhà thuốc bán giá đắt. Mặc dù sau đó Hà Linh giải thích mức giá trên chỉ áp dụng khi mua combo nhưng không xoa dịu được dư luận. Đã có những nhà thuốc kêu gọi nhau tẩy chay không chỉ nhãn hàng trên, mà còn cả những sản phẩm khác của đơn vị này.

Doanh nghiệp này sau đó đã công khai gửi thư xin lỗi các nhà thuốc và nhà phân phối, vì đã khiến người tiếp cận thông tin bị hiểu lầm về giá của sản phẩm, gây ảnh hưởng tới việc kinh doanh.

Chia sẻ với Dân trí về vấn đề này, ông Vũ Trung Hiệp - đồng sáng lập kiêm CEO công ty LinkStar Event & Communication và là Phó Chủ tịch điều hành Cộng đồng Marketing & Truyền thông Việt Nam (VMCC) - cho rằng nếu chỉ thuần túy xét các chỉ số tiếp cận, tương tác và độ lan truyền thì nhãn hàng và Hoa Linh đã có một kết quả tốt. Nhưng xây dựng và quản trị thương hiệu hay rộng hơn là quản trị kinh doanh không đơn giản như thế.
Con dao hai lưỡi

Từ góc nhìn của một chuyên gia thương hiệu, ông đánh giá sao về tác động của câu chuyện trên đến thương hiệu của doanh nghiệp?

- Theo quan sát của cá nhân tôi với diễn biến vụ việc những ngày qua thì sự việc này cần được nhận ở hai góc độ.

Đầu tiên, xét về mặt mục tiêu của nhãn hàng, nếu doanh nghiệp coi livestream trên kênh của một Tiktoker nổi tiếng như Hà Linh là cơ hội để tăng nhận biết thương hiệu và qua đó kích thích dùng thử sản phẩm thì có thể coi họ đã thành công.

Với lượng xem, tương tác và đặt hàng lớn trên livestream; với những bàn tán, thảo luận về vụ việc sau livestream trên cả mạng xã hội và báo chí những ngày qua, nhãn hàng Nguyên Xuân đã được những người trước đây chưa từng nghe tên biết tới. Thậm chí sẽ có những người tò mò dùng thử sản phẩm.

Một số thông tin từ những người kinh doanh trong ngành dược và hóa mỹ phẩm cho biết, nhãn hàng này chỉ đứng trong khoảng top 3 thị trường ở cùng phân khúc và đang được bán chủ yếu tại kênh nhà thuốc. Kênh phân phối truyền thống (GT) và hiện đại (MT) đều đang khá yếu. Đó có thể là lý do khiến doanh nghiệp muốn thử nghiệm một kênh tiếp cận khách hàng mới như livestream trên mạng xã hội của các tài khoản có nhiều lượng theo dõi và lượt xem cao.

Nếu chỉ thuần túy xét các chỉ số tiếp cận, tương tác và độ lan truyền như trên thì nhãn hàng và Hoa Linh đã có một kết quả tốt. Nhưng xây dựng và quản trị thương hiệu hay rộng hơn là quản trị kinh doanh không đơn giản như thế. Nên chúng ta sẽ cần đến một góc nhìn thứ hai, đó là góc nhìn về cảm nhận thương hiệu.

Bên cạnh các con số định lượng được cho là thành công của livestream, nhãn hàng và công ty này sẽ luôn phải đặt câu hỏi: Khách hàng và công chúng sẽ cảm thấy thế nào, sẽ cảm nhận gì từ những thông tin và cách thức kinh doanh của doanh nghiệp.

Vài ngày qua, trên các diễn đàn, cộng đồng xuất hiện khá nhiều phản hồi, đánh giá tiêu cực từ phía các nhà thuốc và người tiêu dùng. Lúc đầu mới chỉ là các phản ứng của riêng cộng đồng nhà thuốc về việc công ty này đã "giành bát cơm", "chặn đường bán hàng" của họ (bằng cách cho Tiktoker bán hàng "phá giá"). Nhưng về sau đã bắt đầu có những phản hồi tiêu cực từ người tiêu dùng xuất hiện trên mạng xã hội. Họ không chỉ bình luận, suy luận về vụ việc mà còn đưa ra cả những đánh giá không tốt về sản phẩm trên, điều mà có thể trước đây dù họ không hài lòng cũng không mất công đưa lên mạng xã hội như vậy.

Tâm lý đám đông từ ngày có thêm "trợ thủ đắc lực" mang tên mạng xã hội luôn rất khó lường. Một ngày đẹp trời những người xa lạ bỗng đoàn kết lại lập một trang Facebook tẩy chay nhãn hàng, công ty là chuyện đã không còn lạ nữa.

Từ một sự việc tưởng như chả ảnh hưởng gì đến người tiêu dùng nhưng vì những kêu than, lên án, phẫn nộ rất hợp vai "kẻ yếu", "người bị hại" của các nhà thuốc cộng thêm những bài viết kiểu "đổ dầu vào lửa" của một số KOL, thế là nguy cơ khủng hoảng manh nha. Đôi khi doanh nghiệp không làm gì sai trực tiếp với người tiêu dùng nhưng họ vẫn ghét, vẫn tẩy chay vì cách doanh nghiệp đối xử với người khác khiến họ thấy "chướng tai, gai mắt".

Ở góc độ này, theo tôi, về mặt cảm nhận chung là tiêu cực đối với nhãn hàng và công ty.
Từ vụ chiến thần Hà Linh, chuyên gia hé lộ bí kíp dùng KOC hiệu quả - 1

Ông Vũ Trung Hiệp (Ảnh NVCC).

Ngoài ra, việc doanh nghiệp chọn Tiktoker Hà Linh cho livestream bán hàng lần này cũng thể hiện doanh nghiệp chưa thực sự hiểu rõ mình và nhất trong việc định hình tính cách thương hiệu của mình. Bởi trước giờ các nhãn hàng của đơn vị này vẫn được đánh giá là những thương hiệu nhẹ nhàng, hòa nhã, thân thiện, tạo cảm giác dễ chịu cho khách hàng.

Nhưng "chiến thần" Hà Linh thì lại bị người xem livestream nhận xét là có cách nói đề cao cá nhân, coi thường, dạy dỗ nhà thuốc. Có người còn nghiên cứu kỹ kênh của Tiktoker này và chỉ ra sự tiêu cực, "toxic" hay cách review có phần "xéo xắt" của cô gái này là không phù hợp với định vị hình mẫu và tính cách thương hiệu của Hoa Linh.

Cũng ở góc nhìn này, dù đây là chương trình bán hàng khuyến khích khách dùng thử và bán theo combo thế nào đi nữa thì cách truyền đạt thông tin có phần "giật tít câu view" của Hà Linh đã găm vào đầu người tiêu dùng cái giá 11.000 đồng và 18.000 đồng cho nhãn hàng dầu gội, tức là một cái giá rất rẻ của sản phẩm bình dân, trong khi nhãn hàng này thực tế không định vị và bán với giá như thế.

Sự không đồng bộ, nhất quán về định vị này cho thấy đơn vị này đã chưa thực sự chặt chẽ và cẩn trọng trong quản trị thương hiệu của mình.
Những cơn sóng xu hướng mới

Việc xử lý bằng văn bản xin lỗi của doanh nghiệp liệu có hiệu quả?

- Theo tôi, nếu doanh nghiệp đưa ra thư xin lỗi sớm hơn thì sẽ tốt hơn, bớt được những "tổn thương", "hờn dỗi" từ nhà thuốc, đại lý như mấy ngày qua. Nhưng dù sao đã có xin lỗi tức là doanh nghiệp đã nhận ra mức độ nguy hiểm của vấn đề rồi. Tôi tin rằng sau thư này họ sẽ có thêm những động thái tiếp xúc trực tiếp với nhà thuốc để khiến tình hình dịu đi.

Bên cạnh đó, chúng ta cũng cần biết rằng mối quan hệ giữa nhà sản xuất và hệ thống nhà phân phối, đại lý không phải được xây lên chỉ trong một vài ngày. Đó là một mối quan hệ được hình thành qua chặng đường dài. Vì thế, cũng không chỉ một vụ việc chưa chuẩn chỉnh mà mối quan hệ mất đi. Thực tế, doanh nghiệp này cũng là thương hiệu mạnh, các nhãn hàng của họ giúp nhà thuốc bán hàng tốt thì nhà thuốc cũng không để cảm xúc nhất thời điều khiển các quyết định. Câu chuyện về lợi ích trong kinh doanh không dễ để cảm xúc chi phối.

Tôi tin là vụ việc rồi sẽ trôi đi và không có thiệt hại nào quá lớn cho doanh nghiệp về mặt hệ thống phân phối, bán hàng như một số lo ngại hơi quá đà. Nhưng doanh nghiệp này cần nghiêm túc coi đây là một bài học đáng nhớ. Vì nếu lặp lại sai lầm tương tự thứ hai thì các đối tác, bạn hàng sẽ không dễ bỏ qua cho như lần này.

Không thể phủ nhận vai trò của công nghệ livestream bán hàng trong thời đại số hiện nay, vậy làm sao để doanh nghiệp không rơi vào tình huống xung đột giữa kênh bán hàng cũ và mới?

- Theo tôi, làm kinh doanh, bản chất là luôn luôn phải linh hoạt thích ứng với mọi biến chuyển của thị trường cũng như thay đổi về công nghệ, kỹ thuật. Livestream trên các nền tảng mạng xã hội như facebook, youtube, tiktok là một sản phẩm của ngành công nghiệp online. Đây là một kênh truyền thông và bán hàng mới, đầy sức mạnh mà doanh nghiệp nào cũng nên nghiên cứu và học cách làm chủ để khai thác hiệu quả từ nó. Nhưng khai thác như thế nào, khai thác được đến đâu thì phụ thuộc nguồn lực, năng lực và cả văn hóa kinh doanh của các doanh nghiệp.

Đứng trước các làn sóng mới, khi thấy nhà nhà "lên thuyền" mà mình vẫn trên bờ ngó xem thì tâm lý ai cũng sốt ruột. Tuy nhiên, nếu chưa thực sự có được những hiểu biết và kỹ năng cần thiết, chưa xây dựng được cơ sở hạ tầng công nghệ, kỹ thuật cũng như có đầy đủ nhân lực vận hành thì sự chạy theo xu hướng là con dao hai lưỡi. Nó có thể khiến doanh nghiệp tiêu tốn thời gian, công sức, tiền bạc mà hiệu quả thu lại không đáng là bao, trong khi lại có thể vì thế mà bỏ bê chăm sóc, tối ưu các kênh cũ.

Việc học hỏi, thử nghiệm để mở rộng thêm các kênh tiếp cận, quảng bá thương hiệu và bán hàng là rất cần thiết. Nhưng trước đó doanh nghiệp cần hiểu rõ mình đang kinh doanh ngành hàng gì, phân khúc nào, định vị thương hiệu ra sao, hệ thống kênh bán hàng hiện tại theo mô hình nào. Phải biết đâu là kênh chủ lực đâu là kênh bổ trợ. Mở rộng nhưng không được cắn mất thị phần của nhau và tạo ra mâu thuẫn, xung đột lợi ích, gây tổn thương các mối quan hệ hợp tác truyền thống. Mọi sự đổi mới đều cần có quá trình chuẩn bị. Tránh quá nôn nóng vì ham muốn hay áp lực tăng trường mà "cua gắt" như cách Hoa Linh để streamer bán online với giá "động trời".

Xu hướng giống như các con sóng. Hết sóng này sẽ lại có sóng khác. Các nền tảng online có phát triển đến đâu cũng chỉ là những trung gian bên ngoài doanh nghiệp, chúng không thuộc sở hữu chắc chắn và dài lâu của doanh nghiệp. Vì thế, chỉ nên khai thác đúng vai trò và đặc tính của chúng chứ không nên phụ thuộc 100%.

B2B2C, D2C, C2C… là các biến thể mô hình kinh doanh từ hai mô hình truyền thống B2B (Business to Business - hình thức kinh doanh giữa doanh nghiệp với doanh nghiệp) và B2C (Business To Consumer - hình thức giao dịch giữa các doanh nghiệp và người tiêu dùng). Chúng được sinh ra trong kỷ nguyên online với sự bùng nổ của các nền tảng mạng xã hội và các sàn thương mại điện tử. Lựa chọn mô hình kinh doanh truyền thống hay những mô hình hiện đại này là tùy vào đặc thù ngành hàng và chiến lược kinh doanh của mỗi doanh nghiệp. Nhưng, một khi doanh nghiệp muốn phát triển bền vững thì không thể xây nhà trên đất người khác hay xây nhà trên mây.

Cuối cùng, khi các làn sóng xu hướng qua đi, khi các nền tảng mới liên tục thay thế nền tảng cũ thì thứ cốt lõi nhất giúp doanh nghiệp đứng vững và phát triển vẫn là năng lực và tâm huyết tạo ra sản phẩm, dịch vụ chất lượng; mô hình kinh doanh phù hợp và thông minh; thương hiệu mạnh; văn hóa sâu sắc; quan hệ khách hàng, đối tác, bền chặt; có trách nhiệm với cộng đồng xã hội và môi trường.
Từ vụ chiến thần Hà Linh, chuyên gia hé lộ bí kíp dùng KOC hiệu quả - 2

Trong thời đại số, các nền tảng mới liên tục thay thế nền tảng cũ (Ảnh: Forbes).
Kẽ hở về quản lý

Liệu có kẽ hở trong quản lý đối với hoạt động livestream, cạnh tranh không lành mạnh thông qua sử dụng các KOC (Key Opinion Consumers - những người thử nghiệm sản phẩm, đưa ra các ý kiến và đề xuất trung thực về các sản phẩm) có tầm ảnh hưởng?

- Tôi cho rằng thời gian tới các cơ quan quản lý sẽ bổ sung vào trong các luật định về lĩnh vực thông tin, truyền thông trực tuyến mà cụ thể ở đây là các mạng xã hội nhằm quản lý, giám sát được nội dung trên các kênh truyền thông, các tài khoản có sức ảnh hưởng lớn đến số đông công chúng, người tiêu dùng. Cần phải có những quy định mới để đáp ứng được yêu cầu của sự thay đổi do công nghệ tạo ra.

Tuy thế, khó có luật nào chặt chẽ và kín kẽ được tuyệt đối so với sự phong phú, đa dạng của cuộc sống. Vì thế, chúng ta vẫn cần kêu gọi và cả hành động để tạo ra một môi trường kinh doanh cũng như môi trường truyền thông có đạo đức. Điều này đòi hỏi nhận thức đúng đắn và sự chung tay của cả doanh nghiệp, khách hàng và các cá nhân, đơn vị tham gia vào hệ thống truyền thông online. Nếu doanh nghiệp không "chơi xấu" nhau thì sẽ không có các streamer, reviewer làm công việc xấu đó. Nếu công chúng, khách hàng phản đối, tẩy chay các doanh nghiệp, streamer có hành vi thiếu đạo đức thì sẽ không ai dám làm điều xấu nữa.

Theo tôi, đây là thời điểm cần thiết phải đưa ra một mô hình hợp tác lành mạnh, văn minh, chuyên nghiệp và có khung khổ pháp lý cụ thể hơn giữa doanh nghiệp, streamer và người tiêu dùng. Có như vậy thì chúng ta mới có thể phát triển kênh livestream theo hướng chính thống và bền vững được.""",
    12)
    print(keywords)