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

class Week(NamedTuple):
    """Структура добавленного в БД нового расхода"""
    date_start: str
    date_end: str

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
    date = _get_tomorow_date()
    answer = db.get_tomorow_homework("homework", date)
    return answer

def get_week_homework():
    date = _get_week_date()
    answer = db.get_week_homework("homework", date)
    return answer

def get_timetable_dayweek(raw_message):
    answer = db.get_timetable_dayweek("timesheet", raw_message)
    return answer

def get_all_timetable():
    return db.get_all_timetable("timesheet")

def delete_homework(raw_message):
    raw_message=list(raw_message.split())
    answer = db.delete_homework_homework("homework", raw_message[0], raw_message[1], raw_message[2])

def edit_timetable_lesson(raw_message):
    raw_message=list(raw_message.split())
    answer = db.edit_timetable_lesson("timesheet", raw_message[0], raw_message[1], raw_message[2])

def edit_homework(raw_message):
    raw_message=list(raw_message.split())
    answer = db.edit_homework_homework("homework", raw_message[0], raw_message[1], raw_message[2])

def _get_today_date():
    return datetime.datetime.today().strftime('%Y-%m-%d')

def _get_tomorow_date():
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow.strftime('%Y-%m-%d')

def _get_week_date():
    today = datetime.date.today()
    days=datetime.datetime.today().weekday()
    date_start = today - datetime.timedelta(days=days)
    date_end = date_start + datetime.timedelta(days=6)
    week=Week(date_start.strftime('%Y-%m-%d'), date_end.strftime('%Y-%m-%d'))
    return week
