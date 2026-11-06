import os
from PIL import Image, ImageDraw, ImageFont

DIR = r"C:\Users\aoe\Downloads\BaoCao_PA2_Nhom03_md"
FONT_DIR = r"C:\Windows\Fonts"

font_title = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 26)
font_subtitle = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 20)
font_bold = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 16)
font_regular = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 15)
font_sm = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 13)
font_sm_bold = ImageFont.truetype(os.path.join(FONT_DIR, "segoeuib.ttf"), 13)
font_xs = ImageFont.truetype(os.path.join(FONT_DIR, "segoeui.ttf"), 11)

def draw_rounded_rect(draw, bbox, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=int(width))

def generate_mobile_mockup():
    width = 2000
    height = 960
    im = Image.new("RGB", (width, height), "#f1f5f9")
    draw = ImageDraw.Draw(im)

    # Title header
    draw.text((80, 30), "BẢN MẪU GIAO DIỆN DI ĐỘNG ANDROID (MATERIAL 3)", fill="#1e3a8a", font=font_title)
    draw.text((80, 68), "Hệ thống giám sát cuộc gọi lạ thời gian thực, cảnh báo SOS gia đình và quét VietQR đa năng", fill="#64748b", font=font_sm)

    # Phone 1 (WF-01): Call Screening Overlay
    p1_x = 180
    p1_y = 110
    pw = 420
    ph = 800

    # Phone shadow
    draw_rounded_rect(draw, (p1_x + 8, p1_y + 8, p1_x + pw + 8, p1_y + ph + 8), 36, fill="#cbd5e1")
    # Phone body
    draw_rounded_rect(draw, (p1_x, p1_y, p1_x + pw, p1_y + ph), 36, fill="#0f172a", outline="#334155", width=4)
    # Screen inner
    screen1 = (p1_x + 12, p1_y + 12, p1_x + pw - 12, p1_y + ph - 12)
    draw_rounded_rect(draw, screen1, 26, fill="#1e293b")

    # Camera notch / pill
    draw_rounded_rect(draw, (p1_x + pw//2 - 40, p1_y + 20, p1_x + pw//2 + 40, p1_y + 40), 10, fill="#000000")
    # Status bar
    draw.text((p1_x + 35, p1_y + 24), "09:41", fill="#94a3b8", font=font_xs)
    draw.text((p1_x + pw - 75, p1_y + 24), "5G  100%", fill="#94a3b8", font=font_xs)

    # WF-01: Incoming Call UI
    draw.text((p1_x + 35, p1_y + 65), "CUỘC GỌI ĐẾN (CALL SCREENING)", fill="#cbd5e1", font=font_sm_bold)
    draw.text((p1_x + 35, p1_y + 92), "028.7777.8888", fill="#ffffff", font=font_title)
    draw.text((p1_x + 35, p1_y + 125), "Số lạ ngoài danh bạ • Tổng đài ảo VoIP", fill="#94a3b8", font=font_sm)

    # Risk Warning Card (Overlay Banner)
    draw_rounded_rect(draw, (p1_x + 25, p1_y + 160, p1_x + pw - 25, p1_y + 360), 16, fill="#450a0a", outline="#dc2626", width=2)
    draw.text((p1_x + 40, p1_y + 175), "CẢNH BÁO: SỐ ĐIỆN THOẠI LỪA ĐẢO", fill="#ef4444", font=font_bold)
    draw.text((p1_x + 40, p1_y + 205), "Điểm tín nhiệm: 12 / 100", fill="#f87171", font=font_subtitle)
    draw.text((p1_x + 40, p1_y + 235), "Mức rủi ro: CỰC KỲ NGUY HIỂM", fill="#fca5a5", font=font_sm_bold)
    draw.text((p1_x + 40, p1_y + 265), "Thủ đoạn nhận diện: Mạo danh Cơ quan Cảnh sát", fill="#fecaca", font=font_sm)
    draw.text((p1_x + 40, p1_y + 288), "điều tra yêu cầu kê khai tài khoản ngân hàng.", fill="#fecaca", font=font_sm)
    draw.text((p1_x + 40, p1_y + 320), "Đã có 14 nạn nhân gửi tố cáo trong 48 giờ qua.", fill="#f87171", font=font_xs)

    # Guardian SOS Notification Card
    draw_rounded_rect(draw, (p1_x + 25, p1_y + 380, p1_x + pw - 25, p1_y + 490), 14, fill="#1e1b4b", outline="#6366f1", width=1.5)
    draw.text((p1_x + 40, p1_y + 395), "BẢO VỆ GIA ĐÌNH (SOS KHẨN CẤP)", fill="#818cf8", font=font_bold)
    draw.text((p1_x + 40, p1_y + 425), "Hệ thống đã tự động gửi cảnh báo khẩn cấp", fill="#c7d2fe", font=font_sm)
    draw.text((p1_x + 40, p1_y + 448), "đến tài khoản người bảo hộ:", fill="#c7d2fe", font=font_sm)
    draw.text((p1_x + 40, p1_y + 470), "Con trai (Đặng Quang Tiến - 0988.776.655)", fill="#a5b4fc", font=font_sm_bold)

    # Call Screener Action Buttons
    # Big Emergency Hang Up Button (1-tap action for seniors)
    draw_rounded_rect(draw, (p1_x + 35, p1_y + 530, p1_x + pw - 35, p1_y + 600), 20, fill="#dc2626")
    draw.text((p1_x + 95, p1_y + 550), "NGẮT CUỘC GỌI NGAY", fill="#ffffff", font=font_bold)
    draw.text((p1_x + 125, p1_y + 575), "(Thao tác 1-chạm khẩn cấp)", fill="#fecaca", font=font_xs)

    # Secondary Action Button
    draw_rounded_rect(draw, (p1_x + 35, p1_y + 620, p1_x + pw - 35, p1_y + 675), 16, fill="#334155", outline="#475569", width=1)
    draw.text((p1_x + 75, p1_y + 638), "Xem chi tiết bằng chứng & đồ thị", fill="#e2e8f0", font=font_sm_bold)

    # Footer Caption Phone 1
    draw.text((p1_x + 30, p1_y + ph + 18), "WF-01: Cảnh báo số lạ đè màn hình & SOS gia đình", fill="#1e293b", font=font_bold)
    draw.text((p1_x + 30, p1_y + ph + 42), "Tối ưu cho người lớn tuổi: Phông lớn, rung chuông to, 1 chạm ngắt máy", fill="#64748b", font=font_xs)

    # Phone 2 (WF-02): VietQR & Clipboard Scanner
    p2_x = 1100
    p2_y = 110

    # Phone shadow
    draw_rounded_rect(draw, (p2_x + 8, p2_y + 8, p2_x + pw + 8, p2_y + ph + 8), 36, fill="#cbd5e1")
    # Phone body
    draw_rounded_rect(draw, (p2_x, p2_y, p2_x + pw, p2_y + ph), 36, fill="#0f172a", outline="#334155", width=4)
    # Screen inner
    draw_rounded_rect(draw, (p2_x + 12, p2_y + 12, p2_x + pw - 12, p2_y + ph - 12), 26, fill="#ffffff")

    # Camera notch
    draw_rounded_rect(draw, (p2_x + pw//2 - 40, p2_y + 20, p2_x + pw//2 + 40, p2_y + 40), 10, fill="#000000")
    draw.text((p2_x + 35, p2_y + 24), "09:41", fill="#1e293b", font=font_xs)
    draw.text((p2_x + pw - 75, p2_y + 24), "5G  100%", fill="#1e293b", font=font_xs)

    # App Header
    draw_rounded_rect(draw, (p2_x + 12, p2_y + 50, p2_x + pw - 12, p2_y + 105), 0, fill="#1e3a8a")
    draw.text((p2_x + 30, p2_y + 68), "AntiScam Guard • Quét mã Napas", fill="#ffffff", font=font_bold)

    # Clipboard Prompt Banner
    draw_rounded_rect(draw, (p2_x + 25, p2_y + 120, p2_x + pw - 25, p2_y + 200), 12, fill="#eff6ff", outline="#93c5fd", width=1.5)
    draw.text((p2_x + 38, p2_y + 130), "Phát hiện số tài khoản từ Zalo:", fill="#1e40af", font=font_sm_bold)
    draw.text((p2_x + 38, p2_y + 152), "1029384756 (VietinBank)", fill="#1e293b", font=font_bold)
    draw.text((p2_x + 38, p2_y + 175), "Chạm để kiểm tra ngay mà không cần nhập lại", fill="#64748b", font=font_xs)

    # QR Camera Viewfinder
    draw_rounded_rect(draw, (p2_x + 50, p2_y + 215, p2_x + pw - 50, p2_y + 425), 18, fill="#0f172a", outline="#0284c7", width=2)
    # Camera crosshairs
    draw.line((p2_x + 70, p2_y + 235, p2_x + 110, p2_y + 235), fill="#38bdf8", width=4)
    draw.line((p2_x + 70, p2_y + 235, p2_x + 70, p2_y + 275), fill="#38bdf8", width=4)

    draw.line((p2_x + pw - 70, p2_y + 235, p2_x + pw - 110, p2_y + 235), fill="#38bdf8", width=4)
    draw.line((p2_x + pw - 70, p2_y + 235, p2_x + pw - 70, p2_y + 275), fill="#38bdf8", width=4)

    draw.line((p2_x + 70, p2_y + 405, p2_x + 110, p2_y + 405), fill="#38bdf8", width=4)
    draw.line((p2_x + 70, p2_y + 405, p2_x + 70, p2_y + 365), fill="#38bdf8", width=4)

    draw.line((p2_x + pw - 70, p2_y + 405, p2_x + pw - 110, p2_y + 405), fill="#38bdf8", width=4)
    draw.line((p2_x + pw - 70, p2_y + 405, p2_x + pw - 70, p2_y + 365), fill="#38bdf8", width=4)

    # Scan laser line
    draw.line((p2_x + 75, p2_y + 320, p2_x + pw - 75, p2_y + 320), fill="#ef4444", width=3)
    draw.text((p2_x + 115, p2_y + 335), "Đang đọc mã VietQR...", fill="#94a3b8", font=font_sm)

    # Decoded Beneficiary Result Card
    draw_rounded_rect(draw, (p2_x + 25, p2_y + 440, p2_x + pw - 25, p2_y + 640), 14, fill="#fef2f2", outline="#f87171", width=1.5)
    draw.text((p2_x + 38, p2_y + 452), "KẾT QUẢ KIỂM CHỨNG TỨC THÌ", fill="#991b1b", font=font_bold)
    draw.text((p2_x + 38, p2_y + 480), "Ngân hàng: VietinBank (BIN 970415)", fill="#1e293b", font=font_sm_bold)
    draw.text((p2_x + 38, p2_y + 502), "STK: 1029384756 • NGUYEN VAN LUA DAO", fill="#1e293b", font=font_sm)
    draw.text((p2_x + 38, p2_y + 525), "Số tiền yêu cầu cọc: 1.500.000 VNĐ", fill="#b91c1c", font=font_bold)
    draw.text((p2_x + 38, p2_y + 555), "Điểm tín nhiệm: 18 / 100 (Cực kỳ nguy hiểm)", fill="#dc2626", font=font_bold)
    draw.text((p2_x + 38, p2_y + 582), "Liên kết: Đã bị 3 nạn nhân tố giác lừa cọc phòng", fill="#450a0a", font=font_xs)
    draw.text((p2_x + 38, p2_y + 602), "trọ tại Quận 5. Trùng khớp mạng lưới lừa đảo.", fill="#450a0a", font=font_xs)

    # Action buttons for phone 2
    draw_rounded_rect(draw, (p2_x + 30, p2_y + 660, p2_x + pw - 30, p2_y + 710), 12, fill="#dc2626")
    draw.text((p2_x + 95, p2_y + 675), "KHÔNG CHUYỂN TIỀN", fill="#ffffff", font=font_bold)

    # Footer Caption Phone 2
    draw.text((p2_x + 30, p2_y + ph + 18), "WF-02: Bóc tách VietQR Napas & Khay nhớ tạm", fill="#1e293b", font=font_bold)
    draw.text((p2_x + 30, p2_y + ph + 42), "Tự động nhận diện chuỗi EMVCo, cảnh báo trước khi xác nhận chuyển khoản", fill="#64748b", font=font_xs)

    out_path = os.path.join(DIR, "wf_mobile.png")
    im.save(out_path, "PNG")
    print(f"Saved {out_path}")

def generate_web_mockup():
    width = 1800
    height = 1120
    im = Image.new("RGB", (width, height), "#f8fafc")
    draw = ImageDraw.Draw(im)

    # Browser Frame Window
    draw_rounded_rect(draw, (40, 30, width - 40, height - 30), 16, fill="#ffffff", outline="#cbd5e1", width=2)

    # Browser Top Title Bar
    draw_rounded_rect(draw, (40, 30, width - 40, 80), 0, fill="#f1f5f9")
    draw.ellipse((60, 48, 74, 62), fill="#ef4444")
    draw.ellipse((82, 48, 96, 62), fill="#f59e0b")
    draw.ellipse((104, 48, 118, 62), fill="#10b981")

    # Address bar
    draw_rounded_rect(draw, (220, 42, 1000, 70), 8, fill="#ffffff", outline="#e2e8f0", width=1)
    draw.text((240, 48), "https://antiscam.vn/dashboard/investigate?report_id=RP-2026-098", fill="#475569", font=font_sm)

    # Navigation bar inside app
    draw_rounded_rect(draw, (40, 80, width - 40, 140), 0, fill="#1e3a8a")
    draw.text((70, 98), "HỆ THỐNG THẨM ĐỊNH & CẢNH BÁO LỪA ĐẢO BẰNG ĐỒ THỊ LIÊN KẾT", fill="#ffffff", font=font_subtitle)
    draw.text((width - 360, 100), "Chuyên viên kiểm duyệt: admin@antiscam.vn", fill="#93c5fd", font=font_sm)

    # Layout: 3 Columns
    # Col 1: Multi-channel input (X: 60 - 480) -> W = 420
    # Col 2: Interactive Cytoscape Canvas (X: 500 - 1240) -> W = 740
    # Col 3: Explainable Credit Breakdown & What-If (X: 1260 - 1740) -> W = 480

    # ==================== COLUMN 1 ====================
    c1_x = 60
    c1_y = 160
    c1_w = 420
    draw_rounded_rect(draw, (c1_x, c1_y, c1_x + c1_w, height - 60), 12, fill="#f8fafc", outline="#e2e8f0", width=1.5)
    draw.text((c1_x + 20, c1_y + 20), "1. TIẾP NHẬN DỮ LIỆU ĐA KÊNH", fill="#1e3a8a", font=font_bold)

    # URL Input Field
    draw.text((c1_x + 20, c1_y + 60), "Đường dẫn bài đăng (URL Facebook/Zalo):", fill="#334155", font=font_sm_bold)
    draw_rounded_rect(draw, (c1_x + 20, c1_y + 85, c1_x + c1_w - 20, c1_y + 125), 6, fill="#ffffff", outline="#cbd5e1", width=1)
    draw.text((c1_x + 30, c1_y + 95), "facebook.com/groups/phongtro_q5/posts/891273", fill="#64748b", font=font_xs)

    # Text Area Field
    draw.text((c1_x + 20, c1_y + 145), "Nội dung bài đăng & Hội thoại chat:", fill="#334155", font=font_sm_bold)
    draw_rounded_rect(draw, (c1_x + 20, c1_y + 170, c1_x + c1_w - 20, c1_y + 360), 6, fill="#ffffff", outline="#cbd5e1", width=1)
    sample_text = [
        "Cho thuê phòng trọ cao cấp full nội thất giá 1.8tr/tháng.",
        "Khu vực Quận 5 gần ĐH KHTN. Đang có 5 bạn hỏi thuê.",
        "Yêu cầu cọc giữ chỗ 1.000.000đ trong 30 phút để nhận",
        "chìa khóa. Chuyển khoản STK: 1029384756 (VietinBank),",
        "chủ tài khoản NGUYEN VAN LUA DAO.",
        "---",
        "Mô hình NLP phát hiện: Đòn áp lực thời gian ('30 phút')",
        "và hối thúc đặt cọc ('chỉ còn 1 phòng duy nhất')."
    ]
    for i, line in enumerate(sample_text):
        draw.text((c1_x + 30, c1_y + 180 + i * 22), line, fill="#1e293b" if i < 5 else "#dc2626", font=font_xs)

    # Image Upload Dropzone & pHash preview
    draw.text((c1_x + 20, c1_y + 380), "Ảnh phòng trọ / Hợp đồng đính kèm:", fill="#334155", font=font_sm_bold)
    draw_rounded_rect(draw, (c1_x + 20, c1_y + 405, c1_x + c1_w - 20, c1_y + 570), 8, fill="#ffffff", outline="#93c5fd", width=1.5)
    # Thumbnail placeholder
    draw_rounded_rect(draw, (c1_x + 35, c1_y + 420, c1_x + 135, c1_y + 510), 6, fill="#e2e8f0", outline="#94a3b8", width=1)
    draw.text((c1_x + 45, c1_y + 455), "[Ảnh phòng]", fill="#64748b", font=font_xs)
    # Hash details
    draw.text((c1_x + 150, c1_y + 425), "Tệp: phongtro_luxury_q5.jpg", fill="#1e293b", font=font_sm_bold)
    draw.text((c1_x + 150, c1_y + 450), "Mã pHash: e4a19b8c7210ff4a", fill="#475569", font=font_xs)
    draw.text((c1_x + 150, c1_y + 475), "Khoảng cách Hamming: 3 (<= 10)", fill="#dc2626", font=font_sm_bold)
    draw.text((c1_x + 150, c1_y + 500), "Kết luận: Trùng lặp 98% ảnh lừa cọc", fill="#dc2626", font=font_xs)
    draw.text((c1_x + 35, c1_y + 535), "Kho ảnh vi phạm đã lưu: 4 vụ tố cáo sử dụng cùng ảnh này", fill="#991b1b", font=font_xs)

    # Action Button
    draw_rounded_rect(draw, (c1_x + 20, c1_y + 600, c1_x + c1_w - 20, c1_y + 655), 8, fill="#2563eb")
    draw.text((c1_x + 105, c1_y + 618), "BẮT ĐẦU THẨM ĐỊNH TOÀN DIỆN", fill="#ffffff", font=font_bold)

    # ==================== COLUMN 2 ====================
    c2_x = 500
    c2_y = 160
    c2_w = 740
    draw_rounded_rect(draw, (c2_x, c2_y, c2_x + c2_w, height - 60), 12, fill="#0f172a", outline="#334155", width=2)
    # Header of canvas
    draw_rounded_rect(draw, (c2_x, c2_y, c2_x + c2_w, c2_y + 50), 0, fill="#1e293b")
    draw.text((c2_x + 20, c2_y + 14), "2. MẠNG LƯỚI ĐỒ THỊ LIÊN KẾT THỰC THỂ (CYTOSCAPE.JS INTERACTIVE GRAPH)", fill="#38bdf8", font=font_bold)
    draw.text((c2_x + c2_w - 200, c2_y + 16), "Phạm vi: 3 BƯỚC LIÊN KẾT", fill="#94a3b8", font=font_xs)

    # Draw Nodes and Edges on Graph Canvas
    # Node 1: Post Input (Center Left)
    n_post = (c2_x + 100, c2_y + 240)
    # Node 2: Bank Account (Center)
    n_bank = (c2_x + 360, c2_y + 160)
    # Node 3: Phone (Center Down)
    n_phone = (c2_x + 360, c2_y + 360)
    # Node 4: Fraud Report 1 (Right Top)
    n_rep1 = (c2_x + 600, c2_y + 120)
    # Node 5: Fraud Report 2 (Right Center)
    n_rep2 = (c2_x + 600, c2_y + 260)
    # Node 6: Image Hash Node (Right Down)
    n_img = (c2_x + 600, c2_y + 420)

    # Edges
    draw.line((n_post[0], n_post[1], n_bank[0], n_bank[1]), fill="#f87171", width=3)
    draw.line((n_post[0], n_post[1], n_phone[0], n_phone[1]), fill="#f87171", width=3)
    draw.line((n_bank[0], n_bank[1], n_rep1[0], n_rep1[1]), fill="#ef4444", width=4)
    draw.line((n_bank[0], n_bank[1], n_rep2[0], n_rep2[1]), fill="#ef4444", width=4)
    draw.line((n_phone[0], n_phone[1], n_bank[0], n_bank[1]), fill="#f59e0b", width=2)
    draw.line((n_post[0], n_post[1], n_img[0], n_img[1]), fill="#a855f7", width=3)
    draw.line((n_img[0], n_img[1], n_rep2[0], n_rep2[1]), fill="#ef4444", width=3)

    # Edge labels
    draw.text((230 + c2_x, c2_y + 180), "YÊU CẦU CHUYỂN", fill="#fca5a5", font=font_xs)
    draw.text((460 + c2_x, c2_y + 125), "BỊ TỐ CÁO (BC-01)", fill="#ef4444", font=font_xs)
    draw.text((460 + c2_x, c2_y + 200), "BỊ TỐ CÁO (BC-02)", fill="#ef4444", font=font_xs)
    draw.text((360 + c2_x, c2_y + 250), "DÙNG NHẬN TIỀN", fill="#fbbf24", font=font_xs)
    draw.text((350 + c2_x, c2_y + 400), "CHỨA ẢNH TRÙNG PHASH", fill="#c084fc", font=font_xs)

    # Nodes
    def draw_graph_node(coord, label, subtext, color, border):
        x, y = coord
        w_node, h_node = 160, 56
        draw_rounded_rect(draw, (x - w_node//2, y - h_node//2, x + w_node//2, y + h_node//2), 10, fill=color, outline=border, width=2)
        draw.text((x - w_node//2 + 10, y - h_node//2 + 8), label, fill="#ffffff", font=font_sm_bold)
        draw.text((x - w_node//2 + 10, y - h_node//2 + 28), subtext, fill="#e2e8f0", font=font_xs)

    draw_graph_node(n_post, "BÀI ĐĂNG KIỂM TRA", "fb.com/posts/891273", "#2563eb", "#60a5fa")
    draw_graph_node(n_bank, "STK VIETINBANK", "1029384756 (Lừa cọc)", "#ea580c", "#fb923c")
    draw_graph_node(n_phone, "SỐ ĐIỆN THOẠI", "0987.654.321 (Spam)", "#d97706", "#fcd34d")
    draw_graph_node(n_rep1, "BÁO CÁO #BC-2026-08", "Mất cọc 1.5tr (Đã duyệt)", "#b91c1c", "#f87171")
    draw_graph_node(n_rep2, "BÁO CÁO #BC-2026-11", "Mất cọc 2.0tr (Đã duyệt)", "#b91c1c", "#f87171")
    draw_graph_node(n_img, "ẢNH PHÒNG TRỌ", "pHash: e4a19b8c...", "#7e22ce", "#c084fc")

    # Legend at bottom of graph
    draw_rounded_rect(draw, (c2_x + 20, height - 140, c2_x + c2_w - 20, height - 75), 8, fill="#1e293b")
    draw.text((c2_x + 35, height - 128), "CHÚ GIẢI THỰC THỂ:", fill="#38bdf8", font=font_xs)
    draw.ellipse((c2_x + 180, height - 124, c2_x + 192, height - 112), fill="#2563eb")
    draw.text((c2_x + 200, height - 128), "Đầu vào kiểm chứng", fill="#ffffff", font=font_xs)

    draw.ellipse((c2_x + 350, height - 124, c2_x + 362, height - 112), fill="#ea580c")
    draw.text((c2_x + 370, height - 128), "Tài khoản ngân hàng", fill="#ffffff", font=font_xs)

    draw.ellipse((c2_x + 520, height - 124, c2_x + 532, height - 112), fill="#b91c1c")
    draw.text((c2_x + 540, height - 128), "Vụ án lừa đảo đã duyệt", fill="#ffffff", font=font_xs)

    draw.text((c2_x + 35, height - 100), "Đường đỏ đậm thể hiện đường đi ngắn nhất (Shortest Path 2-Hop) trỏ tới nút lừa đảo đã xác minh.", fill="#fca5a5", font=font_xs)

    # ==================== COLUMN 3 ====================
    c3_x = 1260
    c3_y = 160
    c3_w = 480
    draw_rounded_rect(draw, (c3_x, c3_y, c3_x + c3_w, height - 60), 12, fill="#f8fafc", outline="#e2e8f0", width=1.5)
    draw.text((c3_x + 20, c3_y + 20), "3. ĐIỂM TÍN NHIỆM & GIẢI TRÌNH WHAT-IF", fill="#1e3a8a", font=font_bold)

    # Credit Score Dial Card
    draw_rounded_rect(draw, (c3_x + 20, c3_y + 55, c3_x + c3_w - 20, c3_y + 175), 10, fill="#fef2f2", outline="#f87171", width=1.5)
    draw.text((c3_x + 35, c3_y + 70), "ĐIỂM TÍN NHIỆM TỔNG HỢP:", fill="#991b1b", font=font_bold)
    draw.text((c3_x + 35, c3_y + 98), "18 / 100", fill="#dc2626", font=font_title)
    draw.text((c3_x + 180, c3_y + 105), "MỨC ĐỘ RỦI RO: CỰC KỲ NGUY HIỂM", fill="#dc2626", font=font_sm_bold)
    draw.text((c3_x + 35, c3_y + 140), "Khuyến nghị: KHÔNG CHUYỂN TIỀN CỌC TRONG MỌI TRƯỜNG HỢP", fill="#b91c1c", font=font_xs)

    # Explainable Penalty Breakdown
    draw.text((c3_x + 20, c3_y + 190), "Phân rã điểm phạt thành phần (Explainable AI):", fill="#1e293b", font=font_sm_bold)
    penalties = [
        ("Điểm phạt đồ thị (S_g = 85.0 x 0.40)", "- 34.0 điểm", "#ef4444"),
        ("Điểm phạt ảnh gian lận (S_i = 98.0 x 0.15)", "- 14.7 điểm", "#ef4444"),
        ("Điểm phạt bất thường STK (S_p = 70.0 x 0.25)", "- 17.5 điểm", "#f97316"),
        ("Điểm phạt thao túng tâm lý (S_s = 60.0 x 0.20)", "- 12.0 điểm", "#f59e0b"),
    ]
    for idx, (p_title, p_val, col) in enumerate(penalties):
        card_y = c3_y + 220 + idx * 48
        draw_rounded_rect(draw, (c3_x + 20, card_y, c3_x + c3_w - 20, card_y + 40), 6, fill="#ffffff", outline="#e2e8f0", width=1)
        draw.text((c3_x + 32, card_y + 10), p_title, fill="#334155", font=font_xs)
        draw.text((c3_x + c3_w - 110, card_y + 10), p_val, fill=col, font=font_sm_bold)

    # What-If Projection Stepper
    draw.text((c3_x + 20, c3_y + 430), "Kịch bản giả định diễn tiến lừa đảo (What-If):", fill="#1e293b", font=font_sm_bold)
    whatifs = [
        ("Bước 1: Hối thúc chuyển cọc giữ phòng 1.000.000đ", "Kẻ gian tạo lý do có người khác đang tới xem phòng.", "#ef4444"),
        ("Bước 2: Báo lỗi cú pháp / Đòi thêm phí hồ sơ 500k", "Kẻ gian viện cớ ngân hàng treo lệnh hoặc chủ nhà đòi cọc thêm.", "#ea580c"),
        ("Bước 3: Chặn Facebook, Zalo & Cắt đứt liên lạc", "Nạn nhân tới địa chỉ phòng trọ thì phát hiện nhà có chủ khác.", "#991b1b"),
    ]
    for idx, (step_t, step_d, step_col) in enumerate(whatifs):
        card_y = c3_y + 460 + idx * 72
        draw_rounded_rect(draw, (c3_x + 20, card_y, c3_x + c3_w - 20, card_y + 64), 8, fill="#ffffff", outline="#e2e8f0", width=1)
        draw_rounded_rect(draw, (c3_x + 20, card_y, c3_x + 26, card_y + 64), 0, fill=step_col)
        draw.text((c3_x + 36, card_y + 10), step_t, fill="#1e293b", font=font_xs)
        draw.text((c3_x + 36, card_y + 34), step_d, fill="#64748b", font=font_xs)

    # Bottom Actions
    draw_rounded_rect(draw, (c3_x + 20, height - 120, c3_x + c3_w - 20, height - 70), 8, fill="#dc2626")
    draw.text((c3_x + 120, height - 100), "XÁC NHẬN ĐƯA VÀO DANH SÁCH ĐEN", fill="#ffffff", font=font_bold)

    out_path = os.path.join(DIR, "wf_web.png")
    im.save(out_path, "PNG")
    print(f"Saved {out_path}")

if __name__ == "__main__":
    generate_mobile_mockup()
    generate_web_mockup()
