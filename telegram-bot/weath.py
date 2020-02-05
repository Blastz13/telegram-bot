import requests

def weather(city):
    rainfall = {
    "clear" : "Ясно☀️",
    "partly-cloudy" : "Малооблачно🌥",
    "cloudy" : "Облачно с прояснениями🌥",
    "overcast" : "Пасмурно🌥",
    "partly-cloudy-and-light-rain" : "Небольшой дождь🌦",
    "partly-cloudy-and-rain" : "Дождь🌧",
    "overcast-and-rain" : "Сильный дождь🌧",
    "overcast-thunderstorms-with-rain" : "Сильный дождь, гроза⛈",
    "cloudy-and-light-rain" : "Небольшой дождь🌦",
    "overcast-and-light-rain" : "Небольшой дождь🌦",
    "cloudy-and-rain" : "Дождь🌧",
    "overcast-and-wet-snow" : "Дождь со снегом🌨",
    "partly-cloudy-and-light-snow" : "Небольшой снег🌨",
    "partly-cloudy-and-snow" : "Снег❄️",
    "overcast-and-snow" : "Снегопад❄️",
    "cloudy-and-light-snow" : "Небольшой снег❄️",
    "overcast-and-light-snow" : "Небольшой снег❄️",
    "cloudy-and-snow" : "Снег❄️"}

    coordinate = geo_coordinate(city)
    url=f"https://api.weather.yandex.ru/v1/forecast?lat={coordinate[0]}&lon={coordinate[1]}&lang=ru_RU&limit=1&extra=false"
    headers={
    "X-Yandex-API-Key":"eece54d3-00b0-4527-9493-75b19c943ac0"
    }
    
    response=requests.get(url,headers=headers)
    response=response.json()
    condition=rainfall[response['forecasts'][0]["parts"]["day"]["condition"]]
    row = "\nПогода на сегодня:\n{}\nВосход: {}\nЗакат: {}\nТемпература:\nНочью🌑: {}\nУтром🌞: {}\nДнем🌤: {}\nВечером🌓: {}\nОсадки: {}\n".format(response['forecasts'][0]["date"],response['forecasts'][0]["sunrise"],response['forecasts'][0]["sunset"],response['forecasts'][0]["parts"]["night"]["temp_avg"],response['forecasts'][0]["parts"]["morning"]["temp_avg"],response['forecasts'][0]["parts"]["day"]["temp_avg"],response['forecasts'][0]["parts"]["evening"]["temp_avg"], condition)
    row += "\nПогода на завтра:\n{}\nВосход: {}\nЗакат: {}\nТемпература:\nНочью🌑: {}\nУтром🌞: {}\nДнем🌤: {}\nВечером🌓: {}\nОсадки: {}\n".format(response['forecasts'][1]["date"],response['forecasts'][1]["sunrise"],response['forecasts'][1]["sunset"],response['forecasts'][1]["parts"]["night"]["temp_avg"],response['forecasts'][1]["parts"]["morning"]["temp_avg"],response['forecasts'][1]["parts"]["day"]["temp_avg"],response['forecasts'][1]["parts"]["evening"]["temp_avg"], condition)
    row += "\nПогода на послезавтра:\n{}\nВосход: {}\nЗакат: {}\nТемпература:\nНочью🌑: {}\nУтром🌞: {}\nДнем🌤: {}\nВечером🌓: {}\nОсадки: {}\n".format(response['forecasts'][2]["date"],response['forecasts'][2]["sunrise"],response['forecasts'][2]["sunset"],response['forecasts'][2]["parts"]["night"]["temp_avg"],response['forecasts'][2]["parts"]["morning"]["temp_avg"],response['forecasts'][2]["parts"]["day"]["temp_avg"],response['forecasts'][2]["parts"]["evening"]["temp_avg"], condition)
    return (row)


def geo_coordinate(city):
    API_KEY="3b4143c7-9efc-46df-aaa3-c49b2d23b540"
    url=f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={city}&format=json"

    response=requests.get(url).json()
    response = list(response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"].split())
    
    return response[1], response[0]