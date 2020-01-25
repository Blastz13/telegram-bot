import requests

def course_json(wallet):
	url="https://www.cbr-xml-daily.ru/daily_json.js"
	wallet=wallet.upper()
	
	res=requests.get(url).json()
	valute=res["Valute"]
	
	try:
		row="Валюта:\n{}\nПокупка:\n{}\nПродажа:\n{}".format(valute[wallet]["Name"],valute[wallet]["Previous"],valute[wallet]["Value"])
		return row
	except:
		return "Такой валюты не существует"