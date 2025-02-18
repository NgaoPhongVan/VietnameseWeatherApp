import requests
from config import NINJAS_API_KEY, NINJAS_BASE_URL

def get_location(city):
    """
    Lấy thông tin tọa độ từ tên thành phố sử dụng API Ninjas
    """
    headers = {'X-Api-Key': NINJAS_API_KEY}
    params = {'city': city}
    
    try:
        response = requests.get(NINJAS_BASE_URL, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        if data and len(data) > 0:
            # Lấy kết quả đầu tiên
            location = {
                'name': data[0]['name'],
                'lat': data[0]['latitude'],
                'lon': data[0]['longitude'],
                'country': data[0]['country']
            }
            return location
        else:
            print(f"Không tìm thấy thông tin cho thành phố: {city}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gọi API geocoding: {e}")
        return None
