# PROJECT PROPOSAL

# HỆ THỐNG KIỂM CHỨNG VÀ CẢNH BÁO LỪA ĐẢO TRỰC TUYẾN BẰNG ĐỒ THỊ LIÊN KẾT THỰC THỂ

Đại học Quốc gia Thành phố Hồ Chí Minh  
Trường Đại học Khoa học Tự nhiên  
Khoa Công nghệ Thông tin  
Bộ môn Công nghệ Phần mềm  
Môn học: Nhập môn Công nghệ Phần mềm  
Lớp học phần: 24_31  
Nhóm thực hiện: Nhóm 03  
Giảng viên hướng dẫn: ThS. Ngô Ngọc Đăng Khoa  
Thành phố Hồ Chí Minh, ngày 17 tháng 10 năm 2026  

---

## MỤC LỤC
1. Bảng đánh giá thành viên
2. Phát biểu bài toán sơ lược
3. Giải pháp đề xuất
4. Kế hoạch phát triển
5. Kế hoạch nhân sự và chi phí
6. Phụ lục A: Thuật ngữ

---

## 1. Bảng đánh giá thành viên

| **MSSV** | **Họ Tên** | **Đóng góp** | **Chữ ký** |
| :---: | :--- | :---: | :---: |
| 24120149 | Đặng Quang Tiến | 100% | |
| 24120334 | Hoàng Khang | 100% | |
| 24120397 | Trương Bảo Nguyên | 100% | |
| 24120425 | Sỉn Thăng Quyền | 100% | |

---

## 2. Phát biểu bài toán sơ lược

### 2.1. Bối cảnh và vấn đề

Hiện nay, vấn nạn lừa đảo không gian mạng gia tăng phức tạp, tập trung vào hai nhóm nạn nhân chính: học sinh, sinh viên tìm trọ, tìm việc làm thêm (chiêu trò lừa cọc phòng trọ, tuyển dụng cộng tác viên ảo); và người cao tuổi trong gia đình ít am hiểu công nghệ (kịch bản mạo danh cơ quan chức năng, lừa trúng thưởng, dẫn dụ chuyển tiền khẩn cấp). Đối tượng lừa đảo thường tạo tài khoản mạng xã hội ảo, đăng tải hình ảnh căn hộ cao cấp hoặc thông tin tuyển dụng việc nhẹ lương cao để thu hút nạn nhân. Khi trao đổi qua tin nhắn Facebook hoặc Zalo, đối tượng tạo tâm lý khan hiếm, yêu cầu chuyển khoản đặt cọc từ năm trăm nghìn đến hai triệu đồng rồi lập tức chặn toàn bộ liên lạc. Đối với việc làm thêm, kẻ gian dẫn dụ nạp tiền thực hiện nhiệm vụ hưởng hoa hồng trước khi chiếm đoạt số tiền lớn.

Các công cụ hiện nay chủ yếu dựa vào danh sách đen tĩnh hoặc tra cứu thủ công rời rạc, không theo kịp việc đối tượng liên tục thay đổi tài khoản và số điện thoại. Đặc biệt, người cao tuổi gặp rào cản lớn khi thao tác trên máy tính và khó tự phát hiện các kịch bản lừa đảo tinh vi. Tuy nhiên, các mắt xích cốt lõi gồm số tài khoản ngân hàng thụ hưởng, kịch bản thao túng tâm lý và kho ảnh căn hộ thường có tính tái sử dụng và liên kết ngầm chặt chẽ.

Từ thực trạng trên, nhóm chủ động đề xuất giải pháp xây dựng hệ thống phần mềm kiểm chứng và cảnh báo lừa đảo trực tuyến bằng đồ thị liên kết thực thể, kết hợp giữa ứng dụng web trên máy tính và ứng dụng di động chuyên biệt trên hệ điều hành Android. Giải pháp kết nối người dùng với mạng lưới tri thức kiểm chứng đa chiều, đồng thời thiết lập cơ chế bảo vệ gia đình thông qua tính năng cảnh báo khẩn cấp SOS giữa các thế hệ.

Hệ thống vận hành theo hai cơ chế can thiệp: tra cứu bài đăng đa kênh chuyên sâu trên ứng dụng web; và giám sát tự động thời gian thực trên ứng dụng di động Android thông qua dịch vụ nhận diện cuộc gọi đến từ số lạ CallScreeningService và dịch vụ lắng nghe thông báo NotificationListenerService từ các ứng dụng Zalo, Messenger, SMS, Email, kết hợp cơ chế cảnh báo SOS người thân khi người dùng trao đổi tin nhắn hoặc chuẩn bị giao dịch.

Khi thực hiện kiểm chứng, có hai trường hợp xảy ra:

Trường hợp 1, nếu các thực thể định danh chưa từng bị báo cáo, hệ thống kiểm tra độc lập mã băm tri giác hình ảnh để phát hiện ảnh sao chép từ kho ảnh lừa đảo và phân tích ngôn ngữ tự nhiên để nhận diện mô thức kịch bản thao túng tâm lý (tạo áp lực thời gian, yêu cầu cọc gấp, dẫn dụ hoa hồng hoặc mạo danh cơ quan chức năng). Hệ thống tính toán điểm tín nhiệm và đưa ra chuỗi kịch bản giả định diễn tiến các bước tiếp theo có thể xảy ra nhằm giúp người dùng nhận thức trước rủi ro. Nếu an toàn, hệ thống trả về nhãn tin cậy và khuyến nghị kiểm tra thực tế trước khi giao dịch.

Trường hợp 2, nếu số điện thoại, tài khoản ngân hàng hoặc nick mạng xã hội có liên kết với nút vi phạm trong cơ sở dữ liệu đồ thị trong phạm vi ba bước, hệ thống lập tức hiển thị nhãn cảnh báo đỏ, đồng thời trên ứng dụng Android sẽ tự động kích hoạt thông báo đẩy SOS khẩn cấp đến tài khoản người bảo hộ để kịp thời can thiệp ngăn chặn giao dịch.

Sau giao dịch, người dùng có thể gửi báo cáo tố giác kèm ảnh chụp biên lai ngân hàng. Hệ thống áp dụng cơ chế đánh giá độ uy tín nguồn tin và cho phép chủ tài khoản khiếu nại xác minh chính chủ để bảo đảm tính minh bạch.

### 2.2. Mục tiêu dự án

Mục tiêu chính là xây dựng giải pháp phần mềm kiểm chứng và cảnh báo sớm lừa đảo trực tuyến dựa trên đồ thị liên kết thực thể, kết hợp ứng dụng di động Android và ứng dụng web.

Các mục tiêu cụ thể gồm:

1. Xây dựng ứng dụng di động Android hỗ trợ lọc cuộc gọi từ số lạ và giám sát thông báo tin nhắn đa kênh (Zalo, Messenger, SMS, Email), tích hợp cơ chế cảnh báo khẩn cấp SOS đến người bảo hộ khi phát hiện tương tác nguy cơ cao dưới một giây.

2. Xây dựng ứng dụng web quản trị và tra cứu bài đăng đa kênh, hỗ trợ trực quan hóa cây đồ thị liên kết thực thể minh bạch.

3. Cài đặt mô-đun trích xuất thực thể định danh tiếng Việt và giải mã mã thanh toán VietQR với độ chính xác trên chín mươi phần trăm.

4. Thiết kế cơ sở dữ liệu đồ thị Neo4j mô hình hóa quan hệ đa chiều, truy vấn liên kết ba bước dưới năm trăm mili-giây trên tập dữ liệu tối thiểu một nghìn nút.

5. Cài đặt thuật toán phân tích kịch bản thao túng tâm lý, tính điểm tín nhiệm đa tiêu chí từ không đến một trăm điểm kèm mô phỏng chuỗi kịch bản giả định rủi ro và cơ chế phát sóng cảnh báo theo khu vực địa lý.

### 2.3. Đối tượng sử dụng

Hệ thống phục vụ ba nhóm tác nhân:

1. Người kiểm chứng thông tin: Sinh viên, người thuê phòng trọ, người tìm việc làm và người cao tuổi trong gia đình cần tra cứu độ an toàn của thông tin thanh toán trực tiếp trên điện thoại Android hoặc ứng dụng web.

2. Người bảo hộ và đóng góp cộng đồng: Người thân, người giám hộ trong gia đình nhận cảnh báo SOS khẩn cấp khi người được bảo hộ gặp rủi ro; nạn nhân gửi báo cáo tố cáo kèm chứng từ chuyển tiền và lịch sử hội thoại.

3. Quản trị viên: Kiểm duyệt các báo cáo tranh chấp, quản lý danh mục ngân hàng, vận hành cơ sở dữ liệu đồ thị và hiệu chỉnh tham số đánh giá rủi ro.

### 2.4. Nghiệp vụ chính

Hệ thống gồm năm quy trình nghiệp vụ cốt lõi:

1. Giám sát cuộc gọi lạ, thông báo đa kênh và SOS gia đình: Ứng dụng Android tự động nhận diện số cuộc gọi đến ngoài danh bạ qua CallScreeningService và bóc tách thông tin thanh toán từ thông báo Zalo, Messenger, SMS, Email qua NotificationListenerService; khi phát hiện rủi ro cao, ứng dụng phát âm thanh cảnh báo lớn, hiển thị biểu ngữ cảnh báo đè và tự động gửi thông báo đẩy SOS khẩn cấp đến tài khoản người bảo hộ đã liên kết.

2. Thẩm định bài đăng, phân tích kịch bản và mô phỏng giả định: Ứng dụng web và di động tiếp nhận văn bản, đường dẫn hoặc hình ảnh bài viết; phân tích mô thức kịch bản thao túng tâm lý, tính toán điểm tín nhiệm, hiển thị cây bằng chứng liên kết và xuất chuỗi kịch bản giả định dự báo diễn tiến các bước lừa đảo tiếp theo nếu người dùng tiếp tục giao dịch.

3. Tiếp nhận báo cáo cộng đồng: Thu thập thông tin tố cáo kèm biên lai ngân hàng, thẩm định và cập nhật thực thể vào đồ thị mạng lưới.

4. Phát sóng cảnh báo cục bộ: Gửi thông báo đẩy đến người dùng trong cùng khu vực hoặc trường đại học khi có báo cáo lừa đảo mới được xác nhận.

5. Xử lý khiếu nại: Tiếp nhận minh chứng đối chất từ người dùng bị báo cáo sai và khôi phục điểm tín nhiệm khi đủ căn cứ.

Quy tắc nghiệp vụ xác định:

Quy tắc tính điểm: Điểm tín nhiệm bằng một trăm trừ đi tổng điểm phạt đồ thị liên kết, điểm phạt bất thường thanh toán, điểm phạt trùng lặp hình ảnh gian lận và điểm phạt nhận diện kịch bản thao túng tâm lý.

Quy tắc xếp loại rủi ro: Từ tám mươi đến một trăm điểm là mức an toàn; từ năm mươi đến bảy mươi chín điểm là cần thận trọng; từ hai mươi lăm đến bốn mươi chín điểm là nguy cơ cao; dưới hai mươi lăm điểm là cực kỳ nguy hiểm.

### 2.5. Phạm vi

Trong phạm vi: Tập trung phòng chống lừa đảo đặt cọc phòng trọ, tuyển dụng cộng tác viên online và kịch bản lừa đảo mạo danh nhắm vào người lớn tuổi; hỗ trợ số điện thoại các nhà mạng Việt Nam và tài khoản các ngân hàng nội địa; phát triển ứng dụng web responsive và ứng dụng di động trên nền tảng Android (phiên bản 8.0 trở lên) tích hợp cơ chế SOS gia đình.

Ngoài phạm vi: Không phát triển trên hệ điều hành iOS trong khuôn khổ đề tài môn học; không can thiệp sâu vào bộ nhớ ứng dụng bên thứ ba ngoài việc sử dụng API thông báo hệ thống; không thực hiện phong tỏa tài khoản ngân hàng; không đưa ra kết luận tư pháp thay cơ quan điều tra và không hỗ trợ các giao dịch ngoại hối hay tiền mã hóa.

### 2.6. Môi trường hoạt động

Phía người dùng: Thiết bị di động chạy hệ điều hành Android phiên bản 8.0 trở lên; hoặc máy tính cá nhân chạy trình duyệt Chrome, Edge, Firefox kết nối Internet ổn định.

Phía máy chủ: Hệ điều hành Ubuntu Linux 22.04 LTS, máy chủ ứng dụng Python 3.11 với FastAPI, cơ sở dữ liệu đồ thị Neo4j Community, cơ sở dữ liệu quan hệ PostgreSQL 16 và hạ tầng thông báo đẩy Firebase Cloud Messaging.

### 2.7. Ràng buộc thiết kế và triển khai

1. Bảo mật quyền riêng tư: Ứng dụng Android chỉ đọc số điện thoại cuộc gọi đến ngoài danh bạ và bóc tách chuỗi ký tự khớp định dạng số tài khoản hoặc số điện thoại từ thông báo hiển thị hệ thống, tuyệt đối không can thiệp vào cơ sở dữ liệu riêng tư của Zalo hay Messenger, tuân thủ nghiêm ngặt chính sách bảo mật Google Play và cơ chế hộp cát Android.

2. Thời gian đáp ứng: Thời gian phản hồi cảnh báo và kích hoạt thông báo SOS không vượt quá một giây.

3. Chuẩn mực kỹ thuật: Toàn bộ dịch vụ giao tiếp qua HTTPS với định dạng JSON, tài liệu thiết kế tuân thủ chuẩn IEEE 830 và UML 2.0, hoàn thành đúng tiến độ theo quy định của môn học.

---

## 3. Giải pháp đề xuất

### 3.1. Phần mềm

#### 3.1.1. Danh sách các chức năng phần mềm

Nhóm sử dụng bảng câu chuyện người dùng nhằm lý giải xuất phát điểm thực tế và sự cần thiết của các chức năng, từ đó quy chiếu sang danh mục yêu cầu chức năng và quy định nghiệp vụ tương ứng của phần mềm.

| **Nhu cầu** | **Yêu cầu** |
| :--- | :--- |
| Là người lớn tuổi ít am hiểu công nghệ, tôi muốn điện thoại tự động phát chuông cảnh báo lớn và hiện biểu ngữ nguy hiểm khi có cuộc gọi từ số lạ lừa đảo để không bị thao túng tâm lý | Giám sát và cảnh báo cuộc gọi số lạ (CallScreening) |
| Là người lớn tuổi, tôi muốn khi gặp tình huống nguy hiểm hoặc bị kẻ gian thúc ép chuyển tiền, hệ thống tự động phát tín hiệu khẩn cấp đến người bảo hộ gia đình để kịp thời can thiệp | Kích hoạt cảnh báo khẩn cấp SOS gia đình |
| Là người thường xuyên sử dụng mạng xã hội, tôi muốn ứng dụng tự động kiểm tra số tài khoản và liên kết đáng ngờ ngay khi nhận tin nhắn từ người lạ qua Zalo, Messenger, SMS để không bấm nhầm vào bẫy lừa đảo | Lắng nghe thụ động thông báo tin nhắn lạ (NotificationListener) |
| Là sinh viên tìm phòng trọ hoặc tìm việc làm trực tuyến, tôi muốn dán nội dung bài đăng hoặc tải ảnh phòng trọ để kiểm tra xem bài viết có dấu hiệu lừa đảo đặt cọc hay ảnh lấy cắp trên mạng hay không | Thẩm định bài đăng và so khớp mã băm ảnh (pHash) |
| Là người đang trao đổi với đối tượng nghi vấn, tôi muốn hệ thống phân tích kịch bản thao túng tâm lý và dự báo trước các bước kẻ gian sẽ thực hiện tiếp theo để tôi chủ động phòng tránh | Phân tích kịch bản và Mô phỏng chuỗi kịch bản giả định (What-If Threat Projection) |
| Là người chuẩn bị chuyển tiền, tôi muốn quét mã VietQR hoặc nhập số tài khoản ngân hàng để tra cứu lịch sử và điểm uy tín của tài khoản thụ hưởng trước khi giao dịch | Tra cứu thực thể thanh toán và Đồ thị liên kết (Neo4j) |
| Là nạn nhân bị lừa đảo, tôi muốn gửi báo cáo tố cáo kèm ảnh chụp ủy nhiệm chi ngân hàng để đưa thông tin kẻ gian vào mạng lưới cảnh báo bảo vệ cộng đồng | Tiếp nhận báo cáo tố cáo và thẩm định chứng từ |
| Là cư dân hoặc sinh viên trong khu vực, tôi muốn nhận được thông báo khi xung quanh nơi tôi ở hoặc trường học có thủ đoạn lừa đảo mới xuất hiện để đề cao cảnh giác | Phát sóng cảnh báo cục bộ theo vị trí địa lý |
| Là chủ tài khoản bị tố cáo nhầm lẫn, tôi muốn gửi hồ sơ xác minh chính chủ để khiếu nại và gỡ bỏ cảnh báo sai lệch | Xử lý khiếu nại và xác minh chính chủ |
| Là người dùng di động, tôi muốn ứng dụng bảo đảm an toàn quyền riêng tư, không đọc trộm dữ liệu cá nhân hay can thiệp vào cơ sở dữ liệu nội bộ của ứng dụng khác | Bảo mật quyền riêng tư và tuân thủ Android Sandbox |
| Là người dùng, tôi muốn thời gian nhận diện số lạ và phản hồi cảnh báo không quá một giây để kịp thời ngăn chặn hành vi lừa đảo | Phản hồi thời gian thực (< 1 giây) |

Dựa trên các câu chuyện người dùng nêu trên, hệ thống quy hoạch thành năm phân hệ chức năng chính kèm theo các quy định nghiệp vụ ràng buộc:

1. Phân hệ Giám sát cuộc gọi lạ, thông báo đa kênh và SOS gia đình: Hoạt động qua ứng dụng di động Android, tự động đối soát số điện thoại cuộc gọi đến từ số lạ qua CallScreeningService và lắng nghe thông báo tin nhắn từ Zalo, Messenger, SMS, Email qua NotificationListenerService; đồng thời hỗ trợ tra cứu nhanh qua khay nhớ tạm và quét mã VietQR. Khi phát hiện thực thể rủi ro cao, ứng dụng phát âm thanh cảnh báo lớn, hiển thị biểu ngữ cảnh báo đè lên màn hình và tự động kích hoạt thông báo đẩy SOS đến tài khoản người bảo hộ. Quy định liên quan: Ứng dụng chỉ được hoạt động qua API do hệ điều hành Android cung cấp; chỉ đọc số điện thoại ngoài danh bạ và bóc tách chuỗi ký tự khớp định dạng tài khoản ngân hàng hoặc liên kết web từ thanh thông báo hệ thống; tuyệt đối không lưu trữ hay gửi nội dung tin nhắn cá nhân về máy chủ; tín hiệu âm thanh SOS phải phát ra ngay cả khi thiết bị đang để chế độ im lặng nếu phát hiện giao dịch rủi ro nghiêm trọng.

2. Phân hệ Thẩm định bài đăng, phân tích kịch bản và mô phỏng giả định: Người dùng dán văn bản bài viết, đường dẫn hoặc tải ảnh phòng trọ lên web app hoặc ứng dụng di động. Hệ thống bóc tách thực thể, so khớp ảnh bằng mã băm tri giác, phân tích mô thức thao túng tâm lý và tự động xuất chuỗi kịch bản giả định diễn tiến các bước lừa đảo tiếp theo. Quy định liên quan: Thuật toán pHash áp dụng ngưỡng khoảng cách Hamming nhỏ hơn hoặc bằng mười để kết luận trùng lặp hình ảnh gian lận; mô hình phân tích kịch bản bắt buộc phải định danh loại hình đòn tâm lý và sinh tối thiểu ba bước diễn tiến kịch bản giả định tiếp theo nhằm cảnh báo sớm cho nạn nhân.

3. Phân hệ Lõi đồ thị và Điểm tín nhiệm: Nạp thực thể vào cơ sở dữ liệu đồ thị Neo4j, truy vấn liên kết đa bước đến các nút vi phạm đã được xác thực, tính toán điểm tín nhiệm trên thang điểm từ không đến một trăm và xuất cây giải trình bằng chứng minh bạch. Quy định liên quan: Bán kính truy vấn duyệt đường đi trên đồ thị giới hạn tối đa ba bước liên kết để tối ưu thời gian phản hồi; điểm tín nhiệm được tổng hợp từ bốn thành phần phạt với trọng số cố định; hệ thống bắt buộc cung cấp cây phân rã nguyên nhân cho từng điểm phạt thành phần.

4. Phân hệ Phát sóng cảnh báo cộng đồng và gia đình: Tự động gửi thông báo đẩy đến người dùng trong cùng khu vực hoặc trường đại học khi có báo cáo lừa đảo mới phát sinh trong bán kính ba cây số, đồng thời chuyển tiếp thông điệp SOS khẩn cấp đến người bảo hộ gia đình. Quy định liên quan: Phạm vi phát sóng cảnh báo cục bộ mặc định trong bán kính ba cây số tính từ tọa độ địa lý phát sinh vụ việc; thông báo khẩn cấp SOS đến tài khoản người thân bảo hộ qua Firebase Cloud Messaging phải đạt độ trễ truyền tải dưới một giây.

5. Phân hệ Tiếp nhận báo cáo và Quản trị: Cung cấp biểu mẫu gửi bằng chứng chuyển khoản ngân hàng, quy trình thẩm định báo cáo và cơ chế xác minh chính chủ khi có khiếu nại. Quy định liên quan: Mọi báo cáo tố cáo mới từ cộng đồng bắt buộc phải đính kèm hình ảnh biên lai ủy nhiệm chi ngân hàng hợp lệ để làm căn cứ thẩm định; tài khoản bị báo cáo sai lệch có quyền nộp yêu cầu xác minh chính chủ và hệ thống cam kết xử lý khiếu nại, gỡ bỏ nhãn cảnh báo trong thời hạn tối đa bốn mươi tám giờ làm việc.

| **Mã** | **Tên chức năng** | **Mô tả kỹ thuật** | **Quy định liên quan** | **Độ ưu tiên** |
| :---: | :---: | :---: | :---: | :---: |
| F1 | Giám sát cuộc gọi, tin nhắn và SOS | Lọc cuộc gọi số lạ CallScreening, bắt tin nhắn NotificationListener và kích hoạt SOS | Tuân thủ Android Sandbox, không đọc trộm dữ liệu, phát chuông lớn khi khẩn cấp | Bắt buộc |
| F2 | Thẩm định kịch bản và Mô phỏng giả định | Bóc tách thực thể, so khớp ảnh pHash, nhận diện đòn tâm lý, xuất kịch bản giả định What-If | Khoảng cách Hamming pHash nhỏ hơn hoặc bằng 10, sinh tối thiểu 3 bước giả định | Bắt buộc |
| F3 | Lõi đồ thị và Điểm tín nhiệm | Mô hình hóa thực thể trên Neo4j, truy vấn liên kết ba bước, tính điểm tín nhiệm và xuất cây giải trình | Truy vết tối đa 3 bước liên kết, minh bạch cây bằng chứng cho từng điểm phạt | Bắt buộc |
| F4 | Phát sóng cảnh báo cộng đồng và SOS | Kích hoạt thông báo đẩy theo vị trí địa lý (bán kính 3 km) và Firebase SOS gia đình | Bán kính cảnh báo cục bộ 3 km, độ trễ truyền tin SOS dưới 1 giây | Bắt buộc |
| F5 | Tiếp nhận báo cáo và Xử lý khiếu nại | Biểu mẫu gửi bằng chứng ủy nhiệm chi, quy trình thẩm định báo cáo và xác minh chính chủ | Bắt buộc có biên lai ủy nhiệm chi, giải quyết khiếu nại trong vòng 48 giờ | Bắt buộc |

Công thức tính Điểm tín nhiệm:

Điểm tín nhiệm = 100 - min(100, W_g * S_g + W_p * S_p + W_i * S_i + W_s * S_s)

Trong đó, S_g là điểm phạt từ đồ thị liên kết với trọng số W_g = 0.40, S_p là điểm phạt từ thông tin thanh toán với trọng số W_p = 0.25, S_i là điểm phạt do trùng lặp ảnh gian lận với trọng số W_i = 0.15, và S_s là điểm phạt do nhận diện kịch bản thao túng tâm lý với trọng số W_s = 0.20.

#### 3.1.2. Kiến trúc tổng thể phần mềm

Hệ thống được thiết kế theo kiến trúc ba tầng:

1. Tầng giao diện người dùng: Gồm ứng dụng web Next.js hiển thị bảng điều khiển, cây đồ thị quan hệ và bản đồ cảnh báo; và ứng dụng di động Android tối ưu cho thao tác tra cứu nhanh, giao diện thân thiện cho người lớn tuổi và cơ chế kích hoạt SOS gia đình.

2. Tầng xử lý nghiệp vụ máy chủ: Xây dựng bằng Python FastAPI bất đồng bộ, gồm dịch vụ trích xuất thực thể định danh, dịch vụ so khớp mã băm ảnh, dịch vụ điều phối truy vấn Cypher và hạ tầng thông báo đẩy Firebase Cloud Messaging.

3. Tầng lưu trữ dữ liệu: Cơ sở dữ liệu đồ thị Neo4j quản lý mạng lưới các nút Người dùng, Số điện thoại, Tài khoản ngân hàng, Mã băm ảnh và Báo cáo vi phạm; cơ sở dữ liệu quan hệ PostgreSQL quản lý tài khoản, nhật ký phiên và lưu trữ chỉ mục mã băm.

### 3.2. Phần cứng

Thiết bị người dùng: Điện thoại thông minh chạy hệ điều hành Android với RAM tối thiểu hai gigabyte, hoặc máy tính cá nhân kết nối Internet ổn định.

Máy chủ vận hành: Máy chủ ảo đám mây Linux Ubuntu 22.04 LTS, cấu hình tối thiểu hai nhân vCPU, bộ nhớ RAM bốn gigabyte và ổ cứng SSD ba mươi gigabyte.

Máy trạm phát triển: Máy tính cá nhân bộ xử lý bốn nhân trở lên, RAM tối thiểu tám gigabyte, hỗ trợ Android Studio, Docker và môi trường phát triển phần mềm.

---

## 4. Kế hoạch phát triển

Dự án áp dụng quy trình Scrum được phân chia thành các Sprint chính và giai đoạn chuẩn bị, bảo đảm bám sát tiến độ theo kế hoạch chung của môn học.

### 4.1. Phân tích yêu cầu

Tuần 1 đến tuần 2: Khảo sát các ca sử dụng lừa cọc phòng trọ, tuyển dụng ảo và kịch bản lừa đảo người lớn tuổi; xác định yêu cầu cơ chế SOS gia đình; biên soạn tài liệu SRS theo chuẩn IEEE 830 và thiết kế Wireframe giao diện web và Android trên Figma.

### 4.2. Thiết kế phần mềm

Tuần 3 đến tuần 4: Thiết kế lược đồ đồ thị Neo4j và cơ sở dữ liệu quan hệ PostgreSQL; đặc tả kiến trúc ba tầng và các giao diện RESTful API; thiết kế kiến trúc ứng dụng di động Android; xây dựng sơ đồ lớp và tuần tự theo chuẩn UML 2.0; hoàn thiện tài liệu SDD.

### 4.3. Cài đặt (implement) phần mềm

Tuần 5 đến tuần 7: Xây dựng máy chủ FastAPI, kết nối cơ sở dữ liệu; cài đặt mô-đun bóc tách thực thể và phát triển ứng dụng Android với dịch vụ CallScreening lọc cuộc gọi lạ, NotificationListener bắt thông báo tin nhắn và tra cứu nhanh thông tin thanh toán.

Tuần 8 đến tuần 9: Cài đặt thuật toán Cypher truy vấn đồ thị, bộ tính điểm tín nhiệm, tích hợp dịch vụ Firebase Cloud Messaging cho cảnh báo SOS và hoàn thiện giao diện ứng dụng web Next.js với thành phần vẽ cây đồ thị.

### 4.4. Kiểm thử phần mềm

Tuần 10: Viết kiểm thử đơn vị cho thuật toán trích xuất và tính điểm; kiểm thử tính năng lọc cuộc gọi, bắt thông báo tin nhắn và kích hoạt gửi thông báo đẩy SOS trên thiết bị Android; kiểm thử toàn diện với bộ dữ liệu hai trăm bài bóc phốt thực tế; lập báo cáo kiểm thử.

### 4.5. Triển khai, bảo trì

Tuần 11 đến tuần 12: Đóng gói tệp cài đặt APK cho Android; triển khai máy chủ bằng Docker Compose lên nền tảng đám mây công cộng; ghi hình video minh họa kịch bản hệ thống và hoàn thiện hồ sơ nghiệm thu.

| **Giai đoạn** | **Thời gian** | **Nội dung công việc chủ yếu** | **Kết quả bàn giao** |
| :---: | :---: | :---: | :---: |
| Sprint 0 | Tuần 1–2 | Khảo sát bài toán, viết Proposal, SRS, thiết kế Figma và lược đồ đồ thị | Proposal, SRS, Figma |
| Sprint 1 | Tuần 3–5 | Dựng hạ tầng cơ sở dữ liệu, lập trình API trích xuất thực thể và ứng dụng Android cơ bản | Tài liệu SDD, MVP 1 (APK) |
| Sprint 2 | Tuần 6–8 | Cài đặt thuật toán đồ thị, tính điểm tín nhiệm và cơ chế cảnh báo SOS người thân | MVP 2 hoàn thiện |
| Sprint 3 | Tuần 9–10 | Tích hợp trực quan hóa cây đồ thị lên web, kiểm thử đơn vị và kiểm thử hệ thống Android | Test Report hoàn chỉnh |
| Sprint 4 | Tuần 11–12 | Đóng gói Docker, phát hành bản cài đặt APK Android, hoàn thiện video demo và báo cáo | Tệp APK, URL Web, Mã nguồn |

---

## 5. Kế hoạch nhân sự và chi phí

### 5.1. Nhân sự

Nhóm thực hiện đề tài gồm bốn nhân sự, được phân bổ vào các vai trò chuyên môn kỹ thuật:

1. Kỹ sư hệ thống phía máy chủ: Một nhân sự phụ trách quản lý tiến độ, thiết kế kiến trúc hệ thống, xây dựng RESTful API và quản trị cơ sở dữ liệu quan hệ.

2. Kỹ sư dữ liệu đồ thị: Một nhân sự phụ trách thiết kế mô hình đồ thị trên Neo4j, viết câu lệnh Cypher duyệt đường đi và xây dựng thuật toán tính điểm tín nhiệm.

3. Kỹ sư giao diện web: Một nhân sự phụ trách thiết kế giao diện Figma, lập trình ứng dụng web Next.js và tích hợp thư viện đồ thị Cytoscape.

4. Kỹ sư ứng dụng di động Android và AI: Một nhân sự phụ trách lập trình ứng dụng di động Android, cài đặt CallScreeningService và NotificationListenerService, cơ chế cảnh báo khẩn cấp SOS gia đình, thuật toán trích xuất thực thể và bóc tách mã VietQR.

### 5.2. Phân chia module

Khối lượng công việc chia thành bốn mô-đun độc lập, mỗi mô-đun do một nhân sự chuyên trách đảm nhiệm:

Module A – Quản trị tài khoản và Cổng báo cáo cộng đồng: Xác thực tài khoản, phân quyền, tiếp nhận tố cáo kèm ủy nhiệm chi và quy trình kiểm duyệt tranh chấp.

Module B – Lõi cơ sở dữ liệu đồ thị và Đánh giá rủi ro: Cơ sở dữ liệu Neo4j, truy vấn Cypher duyệt đường đi đa bước, tính toán điểm tín nhiệm và xuất cây giải trình rủi ro.

Module C – Trực quan hóa đồ thị và Phát sóng cảnh báo: Giao diện web Next.js, hiển thị đồ thị mạng lưới liên kết bằng Cytoscape và dịch vụ phát sóng thông báo đẩy theo vị trí địa lý.

Module D – Ứng dụng di động Android và Cảnh báo SOS gia đình: Lập trình ứng dụng di động chuyên biệt trên nền tảng Android (phiên bản 8.0 trở lên), cài đặt CallScreeningService lọc cuộc gọi lạ, NotificationListenerService bắt thông báo tin nhắn Zalo, Messenger, SMS, Email, bóc tách mã VietQR, phát âm thanh cảnh báo và kích hoạt thông báo đẩy SOS khẩn cấp đến người bảo hộ.

### 5.3. Chi phí dự kiến

Dự án áp dụng chiến lược tối ưu hóa ngân sách tối đa nhằm đạt trạng thái hoàn thiện và vận hành phần mềm cao nhất. Nhóm tận dụng triệt để hệ sinh thái mã nguồn mở và các gói tài nguyên sinh viên miễn phí, chỉ đầu tư kinh phí thiết yếu cho máy chủ đám mây chạy dịch vụ 24/7, tên miền bảo mật và cước viễn thông kiểm thử thực tế. Nguồn kinh phí do bốn thành viên tự túc đóng góp.

| **STT** | **Hạng mục chi phí** | **Phương án kỹ thuật triển khai** | **Chi phí dự kiến** |
| :---: | :---: | :---: | :---: |
| 1 | Nhân lực thực hiện | Bốn thành viên sinh viên tự thực hiện trong suốt quá trình triển khai đề tài | 0 VNĐ |
| 2 | Máy chủ đám mây riêng (VPS) | Thuê máy chủ ảo hai vCPU, bốn gigabyte RAM trong ba tháng để chạy Neo4j và FastAPI 24/7 | 450.000 VNĐ |
| 3 | Tên miền và Chứng chỉ SSL | Tên miền định tuyến API bảo mật HTTPS qua chứng chỉ Let's Encrypt miễn phí phục vụ app Android | 100.000 VNĐ |
| 4 | SIM và cước viễn thông kiểm thử | Hai SIM phụ thử nghiệm các nhà mạng phục vụ kiểm thử cuộc gọi lạ CallScreening và tin nhắn | 150.000 VNĐ |
| 5 | Phân phối và kiểm thử ứng dụng Android | Xuất file APK ký số, phân phối thử nghiệm nội bộ qua GitHub Releases và Firebase App Distribution | 0 VNĐ |
| 6 | Cơ sở dữ liệu và Công cụ lập trình | Neo4j Community, PostgreSQL, Android Studio, VS Code, Git, GitHub và Figma gói giáo dục | 0 VNĐ |
| 7 | Quỹ dự phòng rủi ro kỹ thuật | Dự phòng phát sinh băng thông mạng đám mây và kiểm thử tích hợp dịch vụ phụ trợ | 100.000 VNĐ |
| | **Tổng kinh phí dự kiến** | **Kinh phí tự túc do bốn thành viên nhóm đóng góp (200.000 VNĐ / người)** | **800.000 VNĐ** |

---

## 6. Phụ lục A: Thuật ngữ

| **Thuật ngữ** | **Định nghĩa và ý nghĩa kỹ thuật trong đề tài** |
| :---: | :---: |
| Graph Database | Cơ sở dữ liệu đồ thị, phương thức lưu trữ dưới dạng nút và cạnh, tối ưu cho việc truy vấn đường đi liên kết nhiều bước giữa các đối tượng. |
| Neo4j và Cypher | Hệ quản trị cơ sở dữ liệu đồ thị nguồn mở và ngôn ngữ truy vấn khai báo hỗ trợ tìm kiếm mô hình đường đi phức tạp trong mạng lưới thực thể. |
| Named Entity Recognition | Kỹ thuật xử lý ngôn ngữ tự nhiên tự động trích xuất các thực thể định danh như số điện thoại, tên người và số tài khoản từ văn bản. |
| Perceptual Hashing | Kỹ thuật tạo mã băm dựa trên đặc trưng thị giác hình ảnh, phát hiện ảnh tương đồng hoặc đã qua chỉnh sửa kích thước và màu sắc. |
| Hamming Distance | Thước đo số lượng vị trí bit khác nhau giữa hai chuỗi nhị phân có cùng độ dài, dùng để đánh giá mức độ tương đồng của mã băm ảnh. |
| Android OS | Hệ điều hành di động mã nguồn mở phổ biến, nền tảng duy nhất được lựa chọn để phát triển ứng dụng di động trong đề tài, hỗ trợ cơ chế dịch vụ nền và phân quyền tối ưu. |
| CallScreeningService | Dịch vụ hệ thống Android cho phép ứng dụng can thiệp kiểm tra số điện thoại cuộc gọi đến từ số lạ trước khi đổ chuông để cảnh báo dấu hiệu lừa đảo. |
| NotificationListenerService | Dịch vụ hệ thống Android cho phép ứng dụng lắng nghe và bóc tách thông tin thanh toán từ thông báo của Zalo, Messenger, SMS và Email mà không vi phạm quyền riêng tư. |
| Family Guardian SOS | Cơ chế tự động gửi cảnh báo khẩn cấp qua thông báo đẩy đến tài khoản người bảo hộ khi phát hiện người dùng tiếp xúc với thông tin thanh toán có nguy cơ cao. |
| Firebase Cloud Messaging | Hạ tầng truyền thông điệp và thông báo đẩy đa nền tảng từ máy chủ đến ứng dụng di động Android theo thời gian thực dưới một giây. |
| What-If Threat Projection | Cơ chế mô phỏng chuỗi kịch bản giả định diễn tiến các bước lừa đảo tiếp theo mà kẻ gian thường áp dụng, giúp người dùng nhận thức trước rủi ro và ngăn chặn kịp thời. |
| Explainable AI | Khả năng giải trình minh bạch các căn cứ dữ liệu và mắt xích liên kết dẫn đến kết quả cảnh báo rủi ro của hệ thống. |
