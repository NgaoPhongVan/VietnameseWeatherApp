from geocoding_api import get_location
from weather_api import get_weather_data, parse_weather_data

def display_weather(weather_info):
    """
    Hiển thị thông tin thời tiết theo định dạng đẹp
    """
    if not weather_info:
        print("Không thể lấy thông tin thời tiết!")
        return
    
    print("\n=== THÔNG TIN THỜI TIẾT ===")
    print(f"Thành phố: {weather_info['city']}, {weather_info['country']}")
    
    # Thời tiết hiện tại
    current = weather_info['current']
    print("\n-- Thời tiết hiện tại --")
    print(f"Nhiệt độ: {current['temperature']}°C (Cảm giác như: {current['feels_like']}°C)")
    print(f"Mô tả: {current['description']}")
    print(f"Độ ẩm: {current['humidity']}%")
    print(f"Tốc độ gió: {current['wind_speed']} m/s")
    
    # Dự báo thời tiết 5 ngày
    print("\n-- Dự báo 5 ngày tới --")
    for day in weather_info['forecast']:
        print(f"{day['date']}: {day['temp']}°C, {day['description']}")
    
    print("=========================\n")

def main():
    while True:
        city = input("Nhập tên thành phố (hoặc 'q' để thoát): ")
        
        if city.lower() == 'q':
            print("Tạm biệt!")
            break
         
        # Lấy thông tin vị trí
        location = get_location(city)
        
        if location:
            # Lấy và hiển thị thông tin thời tiết
            weather_data = get_weather_data(location['lat'], location['lon'])
            weather_info = parse_weather_data(weather_data, location['name'], location['country'])
            display_weather(weather_info)
        else:
            print("Không thể tìm thấy thông tin vị trí cho thành phố này.")

if __name__ == "__main__":
    main()