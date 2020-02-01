import datetime
import re
from typing import List, NamedTuple, Optional

import pytz

import db

class Homework(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    dayweek: str
    lesson: str
    homework: str
    date: str

def add_homework(raw_message: str):
    parse_message=list(raw_message.split())
    
    inserted_row = db.create_homework("homework", {
        "dayweek": parse_message[0],
        "num": parse_message[1],
        "lesson": parse_message[2],
        "homework": parse_message[3],
        "date": parse_message[4]
    })

def get_today_homework():
    date = _get_today_date()
    answer = db.get_today_homework("homework", date)
    return answer

def get_tomorow_homework():
    date 
    answer = db.get_tomorow_homework("homework", date)

def _get_today_date():
    return datetime.datetime.today().strftime("%d-%m-%Y")

def _get_tomorow_date():
    return 
print(get_today_homework())