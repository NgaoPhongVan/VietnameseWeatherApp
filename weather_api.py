import requests
from config import OPENWEATHER_API_KEY, WEATHER_BASE_URL

def get_weather_data(lat, lon):
    """
    Lấy dữ liệu thời tiết từ OpenWeatherMap API sử dụng tọa độ
    """
    params = {
        'lat': lat,
        'lon': lon,
        'appid': OPENWEATHER_API_KEY,
        'units': 'metric',  # Sử dụng độ C thay vì độ F
        'lang': 'vi'  # Lấy mô tả thời tiết bằng tiếng Việt
    }
    
    try:
        response = requests.get(WEATHER_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gọi API thời tiết: {e}")
        return None

def parse_weather_data(data, city_name, country):
    """
    Xử lý dữ liệu thời tiết thô từ API thành định dạng dễ đọc
    """
    if not data:
        return None
    
    # Lấy thông tin thời tiết hiện tại (forecast đầu tiên)
    current = data['list'][0]
    
    # Dự báo thời tiết cho 5 ngày (mỗi ngày lấy 1 mẫu)
    forecasts = []
    days_processed = set()
    
    for item in data['list']:
        # Lấy ngày từ timestamp
        day = item['dt_txt'].split(' ')[0]
        
        # Chỉ lấy 1 mẫu cho mỗi ngày
        if day not in days_processed and len(forecasts) < 5:
            forecasts.append({
                'date': day,
                'temp': round(item['main']['temp'], 1),
                'description': item['weather'][0]['description'],
                'humidity': item['main']['humidity'],
                'wind_speed': item['wind']['speed']
            })
            days_processed.add(day)
    
    return {
        'city': city_name,
        'country': country,
        'current': {
            'temperature': round(current['main']['temp'], 1),
            'feels_like': round(current['main']['feels_like'], 1),
            'humidity': current['main']['humidity'],
            'description': current['weather'][0]['description'],
            'wind_speed': current['wind']['speed']
        },
        'forecast': forecasts
    }
