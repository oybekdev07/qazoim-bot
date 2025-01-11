import requests
from bs4 import BeautifulSoup

def get_prayer_times(city_name):
    # HTTP so‘rov yuborish
    response = requests.get(f"https://namozvaqti.uz/shahar/{city_name}")
    response.raise_for_status()  # Agar xatolik bo‘lsa, exception tashlaydi

    # HTMLni tahlil qilish
    soup = BeautifulSoup(response.text, 'html.parser')

    # Namoz vaqtlarini jadvaldan qidirish
    prayer_table = soup.find_all('p', {'class': 'time'})  # `table` klassi to‘g‘ri ekanligini tekshiring
    prayer_times = []
    if prayer_table:
        for item in prayer_table:
            prayer_times.append(item.text)
    else:
        return False,False,False,False,False,False
    return prayer_times
