# ỨNG DỤNG DI ĐỘNG BẢO VỆ GIA ĐÌNH (ANDROID APP)

Ứng dụng di động chuyên biệt trên hệ điều hành Android (do **Module D - Sỉn Thăng Quyền** phụ trách).

---

## 1. Thông số kỹ thuật
* **Hệ điều hành:** Android Native (Kotlin)
* **Minimum SDK:** Android 8.0 (API Level 26) – *Yêu cầu tối thiểu để hỗ trợ CallScreeningService và NotificationListenerService*
* **Target SDK:** Android 14 (API Level 34)
* **Kiến trúc ứng dụng:** MVVM (Model - View - ViewModel) với Jetpack Compose hoặc XML Views
* **Thư viện chính:**
  * Retrofit 2 + OkHttp 3: Giao tiếp RESTful API với Backend FastAPI.
  * Firebase Cloud Messaging (FCM): Nhận thông báo đẩy khẩn cấp SOS và cảnh báo khu vực.
  * ZXing / Google ML Kit Barcode Scanning: Giải mã mã thanh toán VietQR từ camera hoặc ảnh chụp.

---

## 2. Các dịch vụ hệ thống Android cốt lõi (Core Services)

### ① `CallScreeningService` (Lọc cuộc gọi số lạ)
* **Mục đích:** Đón đầu các cuộc gọi đến ngoài danh bạ, tự động kiểm tra số điện thoại với API Backend và hiển thị biểu ngữ cảnh báo đè lên màn hình trước khi người dùng nghe máy.
* **Khai báo Manifest bắt buộc:**
  ```xml
  <service
      android:name=".services.AntiScamCallScreeningService"
      android:permission="android.permission.BIND_SCREENING_SERVICE">
      <intent-filter>
          <action android:name="android.telecom.CallScreeningService" />
      </intent-filter>
  </service>
  ```

### ② `NotificationListenerService` (Lắng nghe thụ động thông báo đa kênh)
* **Mục đích:** Bắt chuỗi thông báo từ Zalo, Messenger, SMS, Email; dùng biểu thức chính quy (Regex) bóc tách số tài khoản ngân hàng và đường dẫn khả nghi.
* **Cam kết bảo mật:** Chỉ bóc tách chuỗi khớp mẫu chuyển tiền, **tuyệt đối không can thiệp nội bộ hay lưu trữ tin nhắn cá nhân**, tuân thủ nghiêm ngặt Android Sandbox.
* **Khai báo Manifest bắt buộc:**
  ```xml
  <service
      android:name=".services.AntiScamNotificationListener"
      android:permission="android.permission.BIND_NOTIFICATION_LISTENER_SERVICE">
      <intent-filter>
          <action android:name="android.service.notification.NotificationListenerService" />
      </intent-filter>
  </service>
  ```

### ③ `FamilySOSManager` (Cơ chế SOS bảo vệ 2 thế hệ)
* Khi phát hiện giao dịch nguy hiểm cao hoặc người lớn tuổi bị thúc ép chuyển tiền:
  1. Phát âm thanh chuông lớn cảnh báo ngay cả khi máy để im lặng.
  2. Bắn yêu cầu `POST /api/v1/sos/trigger` gửi cảnh báo khẩn cấp đến tài khoản người bảo hộ qua Firebase trong thời gian < 1 giây.

---

## 3. Hướng dẫn mở dự án bằng Android Studio

1. Khởi động **Android Studio** (phiên bản Giraffe / Hedgehog hoặc mới hơn).
2. Chọn **Open** và trỏ đến thư mục `mobile/`.
3. Chờ Gradle đồng bộ (Sync Project with Gradle Files).
4. Thêm tệp cấu hình `google-services.json` vào thư mục `mobile/app/` để kích hoạt thông báo Firebase.
5. Chạy thử trên máy ảo hoặc thiết bị Android thật (bật USB Debugging).

