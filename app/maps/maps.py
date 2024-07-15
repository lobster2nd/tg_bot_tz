from geopy.geocoders import Nominatim


def generate_location_link(place):
    """Создаёт ссылку на Яндекс карты по указзанным координатам"""
    nominatim = Nominatim(user_agent='user')

    location = nominatim.geocode(place).raw

    if location:
        latitude = location['lat']
        longitude = location['lon']

        yandex_maps_url = f"https://yandex.ru/maps/?ll={longitude},{latitude}&z=17&pt={longitude},{latitude},pm2~{latitude},{longitude},pm2"

        return f"Ссылка на локацию в Яндекс.Картах: {yandex_maps_url}"
    else:
        return "Место не найдено"
