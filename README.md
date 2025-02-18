# Vietnamese Weather App

Ứng dụng thời tiết sử dụng Python để tra cứu thông tin thời tiết hiện tại và dự báo 5 ngày cho bất kỳ thành phố nào trên thế giới, với hỗ trợ hiển thị tiếng Việt.

## Tính năng

- Tìm kiếm thời tiết dựa trên tên thành phố
- Tự động chuyển đổi tên thành phố thành tọa độ thông qua API Geocoding
- Hiển thị thông tin thời tiết hiện tại chi tiết
- Hiển thị dự báo thời tiết cho 5 ngày tiếp theo
- Hỗ trợ hiển thị mô tả thời tiết bằng tiếng Việt
- Giao diện dòng lệnh thân thiện với người dùng

## Cấu trúc dự án

```
weather_app/
    ├── config.py                # Cấu hình cho các API
    ├── geocoding.py             # Xử lý tìm kiếm tọa độ từ tên thành phố
    ├── weather_api.py           # Xử lý lấy dữ liệu thời tiết từ tọa độ
    ├── main.py                  # Logic chính và giao diện người dùng
    ├── .env                     # File chứa API keys (không đưa vào git)
    └── requirements.txt         # Các thư viện cần thiết
```

## Yêu cầu hệ thống

- Python 3.7 trở lên
- Các thư viện Python như requests, python-dotenv (xem requirements.txt)
- Kết nối internet để truy cập APIs

## Cài đặt

1. Clone dự án về máy:
```bash
git clone https://github.com/NgaoPhongVan/VietnameseWeatherApp.git
cd VietnameseWeatherApp
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

3. Đăng ký tài khoản và lấy API keys:
   - OpenWeatherMap: https://openweathermap.org/
   - API Ninjas: https://api-ninjas.com/

4. Tạo file `.env` trong thư mục gốc với nội dung:
```
OPENWEATHER_API_KEY=your_openweather_api_key
NINJAS_API_KEY=your_ninjas_api_key
```

## Cách sử dụng

1. Chạy ứng dụng:
```bash
python main.py
```

2. Nhập tên thành phố khi được yêu cầu (ví dụ: "Hanoi", "Ho Chi Minh City", "Da Nang")

3. Xem thông tin thời tiết hiện tại và dự báo 5 ngày

4. Nhập 'q' để thoát ứng dụng

## Ví dụ kết quả

```
=== THÔNG TIN THỜI TIẾT ===
Thành phố: Hanoi, VN

-- Thời tiết hiện tại --
Nhiệt độ: 27.8°C (Cảm giác như: 29.5°C)
Mô tả: mây rải rác
Độ ẩm: 78%
Tốc độ gió: 2.5 m/s

-- Dự báo 5 ngày tới --
2025-02-19: 28.1°C, mây thưa
2025-02-20: 29.5°C, mây cụm
2025-02-21: 27.8°C, trời trong
2025-02-22: 25.2°C, mưa nhẹ
2025-02-23: 24.1°C, mưa vừa
=========================
```

## Phát triển trong tương lai

Một số ý tưởng để phát triển dự án trong tương lai:
- Thêm giao diện đồ họa (GUI) sử dụng Tkinter hoặc giao diện web với Flask
- Lưu trữ lịch sử tìm kiếm của người dùng
- Thêm biểu đồ để hiển thị sự thay đổi nhiệt độ theo thời gian
- Thêm tùy chọn đổi đơn vị đo (°C/°F)
- Hỗ trợ nhiều ngôn ngữ hơn

## Giấy phép

[MIT License](https://opensource.org/licenses/MIT)

## Tác giả

[Lê Văn Thuận] - [thienle1247@gmail.com]

## Lời cảm ơn

- OpenWeatherMap API cho dữ liệu thời tiết
- API Ninjas cho dịch vụ geocoding