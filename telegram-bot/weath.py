import requests

def weather(city):
    
    url="https://api.weather.yandex.ru/v1/forecast?lat=54.06387&lon=44.9509&lang=ru_RU&limit=1&extra=false"
    headers={
    "X-Yandex-API-Key":"672ec2bc-3e8a-428a-9b3a-5c01a1405fe6"
    }
    
    response=requests.get(url,headers=headers)
    response=response.json()
    
    if city.lower()== "москва":
    	url="https://api.weather.yandex.ru/v1/forecast?lat=&lon=&lang=ru_RU&limit=1&extra=false"
    	response=requests.get(url,headers=headers).json()
    
    return ("{}\nВосход:{}\nЗакат:{}\nТемпература ночью:{}\nТемпература утром:{}\nТемпература днем:{}\nТемпература вечером:{}\nОсадки: не ожидается".format(response['forecasts'][0]["date"],response['forecasts'][0]["sunrise"],response['forecasts'][0]["sunset"],response['forecasts'][0]["parts"]["night"]["temp_avg"],response['forecasts'][0]["parts"]["morning"]["temp_avg"],response['forecasts'][0]["parts"]["day"]["temp_avg"],response['forecasts'][0]["parts"]["evening"]["temp_avg"]))
