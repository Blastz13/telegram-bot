import requests


def course_currency(wallet):
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    wallet = wallet.upper()
    res = requests.get(url).json()
    wallete = res["Valute"]

    try:
        row = "Валюта:\n{}\nПокупка:\n{}\nПродажа:\n{}".format(wallete[wallet]["Name"],
                                                               wallete[wallet]["Previous"],
                                                               wallete[wallet]["Value"])
    except:
        return "Такой валюты не существует"
    return row
