import requests
import config


def weather_forecast(city):
    rainfall = {
        "clear": "Ясно☀️",
        "partly-cloudy": "Малооблачно🌥",
        "cloudy": "Облачно с прояснениями🌥",
        "overcast": "Пасмурно🌥",
        "partly-cloudy-and-light-rain": "Небольшой дождь🌦",
        "partly-cloudy-and-rain": "Дождь🌧",
        "overcast-and-rain": "Сильный дождь🌧",
        "overcast-thunderstorms-with-rain": "Сильный дождь, гроза⛈",
        "cloudy-and-light-rain": "Небольшой дождь🌦",
        "overcast-and-light-rain": "Небольшой дождь🌦",
        "cloudy-and-rain": "Дождь🌧",
        "overcast-and-wet-snow": "Дождь со снегом🌨",
        "partly-cloudy-and-light-snow": "Небольшой снег🌨",
        "partly-cloudy-and-snow": "Снег❄️",
        "overcast-and-snow": "Снегопад❄️",
        "cloudy-and-light-snow": "Небольшой снег❄️",
        "overcast-and-light-snow": "Небольшой снег❄️",
        "cloudy-and-snow": "Снег❄️"}

    coordinate = geo_coordinate(city)
    url = f"https://api.weather.yandex.ru/v1/forecast?lat={coordinate[0]}&lon={coordinate[1]}&lang=ru_RU&limit=1" \
          f"&extra=false "
    headers = {
        "X-Yandex-API-Key": config.X_YANDEX_API_KEY
    }

    response = requests.get(url, headers=headers).json()
    condition = rainfall[response['forecasts'][0]["parts"]["day"]["condition"]]

    row = f"\nПогода на сегодня:\n{['forecasts'][0]['date']}\nВосход: {response['forecasts'][0]['sunrise']}" \
          f"\nЗакат: {response['forecasts'][0]['sunset']}\nТемпература:" \
          f"\nНочью🌑: {response['forecasts'][0]['parts']['night']['temp_avg']}" \
          f"\nУтром🌞: {response['forecasts'][0]['parts']['morning']['temp_avg']}" \
          f"\nДнем🌤: {response['forecasts'][0]['parts']['day']['temp_avg']}" \
          f"\nВечером🌓: {response['forecasts'][0]['parts']['evening']['temp_avg']}\nОсадки: {condition}\n"

    row += f"\nПогода на сегодня:\n{['forecasts'][1]['date']}\nВосход: {response['forecasts'][1]['sunrise']}" \
           f"\nЗакат: {response['forecasts'][1]['sunset']}\nТемпература:" \
           f"\nНочью🌑: {response['forecasts'][1]['parts']['night']['temp_avg']}" \
           f"\nУтром🌞: {response['forecasts'][1]['parts']['morning']['temp_avg']}" \
           f"\nДнем🌤: {response['forecasts'][1]['parts']['day']['temp_avg']}" \
           f"\nВечером🌓: {response['forecasts'][1]['parts']['evening']['temp_avg']}\nОсадки: {condition}\n"

    row += f"\nПогода на сегодня:\n{['forecasts'][2]['date']}\nВосход: {response['forecasts'][2]['sunrise']}" \
           f"\nЗакат: {response['forecasts'][2]['sunset']}\nТемпература:" \
           f"\nНочью🌑: {response['forecasts'][2]['parts']['night']['temp_avg']}" \
           f"\nУтром🌞: {response['forecasts'][2]['parts']['morning']['temp_avg']}" \
           f"\nДнем🌤: {response['forecasts'][2]['parts']['day']['temp_avg']}" \
           f"\nВечером🌓: {response['forecasts'][2]['parts']['evening']['temp_avg']}\nОсадки: {condition}\n"
    return row


def geo_coordinate(city):
    API_KEY = config.COORDINATE_API_KEY
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city}&format=json"

    response = requests.get(url).json()
    response = list(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    return response[1], response[0]
