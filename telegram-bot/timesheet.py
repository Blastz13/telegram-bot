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

def add_homework(parse_message):
    
    inserted_row = db.create_homework("homework", {
        "dayweek": parse_message[0],
        "num": parse_message[1],
        "lesson": parse_message[2],
        "homework": parse_message[4],
        "date": parse_message[3]
    })
    return

def add_lesson(raw_message: str):
    raw_message = list(raw_message.text.split())
    answer = db.create_timetable_lesson("timesheet",{
        "dayweek": raw_message[0].capitalize(),
        "num": raw_message[1],
        "lesson": raw_message[2].capitalize()})
    return

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

def get_timetable_today():
    dayweek = _get_dayweek_today()
    answer = db.get_timetable_today("timesheet", dayweek)
    return answer

def get_timetable_tomorow():
    dayweek = _get_dayweek_tomorow()
    answer = db.get_timetable_tomorow("timesheet", dayweek)
    return answer    

def get_timetable_dayweek(raw_message):
    answer = db.get_timetable_dayweek("timesheet", raw_message)
    return answer

def get_all_timetable():
    return db.get_all_timetable("timesheet")

def delete_homework(raw_message):
    raw_message = list(raw_message.text.split())
    answer = db.delete_homework_homework("homework", raw_message[0], raw_message[1], raw_message[2])
    return

def delete_lesson(raw_message):
    raw_message = list(raw_message.text.split())
    answer = db.delete_lesson_timesheet("timesheet", raw_message[0], raw_message[1])
    return

def edit_timetable_lesson(raw_message):
    raw_message = list(raw_message.text.split())
    answer = db.edit_timetable_lesson("timesheet", raw_message[0], raw_message[1], raw_message[2])
    return

def edit_homework(*answer):
    answer = db.edit_homework_homework("homework", *answer)
    return

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

def _get_dayweek_today():
    days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    today = datetime.date.today()
    dayNumber=today.weekday()
    return days[dayNumber]

def _get_dayweek_tomorow():
    days=["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    tomorow = datetime.date.today() + datetime.timedelta(days=1)
    dayNumber=tomorow.weekday()
    return days[dayNumber]