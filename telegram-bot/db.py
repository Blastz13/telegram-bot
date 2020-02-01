import os
from typing import Dict, List, Tuple

import sqlite3


conn = sqlite3.connect("db/finance.db", check_same_thread = False)
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def fetchall(table: str, columns: List[str]) -> List[Tuple]:
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    """Проверяет, инициализирована ли БД, если нет — инициализирует"""
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='expense'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()

check_db_exists()
# # insert("lessons", {"dayweek":"Вторник","lesson":"Химия","homework":"Параграф 3"})

# def fetch_timetable_dayweek(table: str, columns: str) -> List[Tuple]:
#     """Вisplays the schedule for the day of the week"""
#     columns_joined = ", ".join(columns)
#     cursor.execute(f"SELECT * FROM {table} WHERE dayweek LIKE '{columns}%'")
#     rows = cursor.fetchall()
    
#     return rows


def create_homework(table: str, column_values: Dict):
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()

def create_timetable_lesson(table: str, column_values: Dict):
    """Add lesson in timetable"""
    columns = ', '.join( column_values.keys() )
    values = [tuple(column_values.values())]
    placeholders = ", ".join( "?" * len(column_values.keys()) )
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()

# insert_homework ("homework", {"dayweek":"Пятница","lesson":"Астрономия","homework":"Параграф 1","num":2,"date":"07-02-2020"})

def delete_timetable_lesson(table: str, dayweek: str, num: str):
    """Remove lesson from timetable"""
    cursor.execute(f"DELETE FROM '{table}' WHERE dayweek='{dayweek}' AND num='{num}'")
    rows = conn.commit()
    
    return rows   



def edit_timetable_lesson(table: str, dayweek: str, num: int, lesson: str, homework=""):
    """Edits a lesson"""
    cursor.execute(f"UPDATE '{table}' SET homework='{homework}', lesson='{lesson}', homework='{homework}' WHERE num='{num}' and dayweek='{dayweek}'")
    rows = conn.commit()
    
    return rows

def get_today_homework(table: str, date: str) -> List[Tuple]:

    # cursor.execute(f"SELECT timesheet.dayweek, timesheet.num, timesheet.lesson, homework.homework FROM timesheet LEFT OUTER JOIN homework ON homework.dayweek = timesheet.dayweek, homework.num = timesheet.num")
    cursor.execute(f"SELECT timesheet.dayweek , timesheet.num, timesheet.lesson , homework.homework FROM homework INNER JOIN timesheet ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num WHERE homework.date = '04-02-2020'")
    rows = cursor.fetchall()
    return rows
# print(get_today_homework("homework","04-02-2020"))
# create_timetable_lesson("homework", {"dayweek":"Вторник","lesson":"Химия","homework":"Параграф 3","num":1,"date":"04-02-2020"})

def get_tomorow_homework(table: str, date: str) -> List[Tuple]:

    # cursor.execute(f"SELECT timesheet.dayweek, timesheet.num, timesheet.lesson, homework.homework FROM timesheet LEFT OUTER JOIN homework ON homework.dayweek = timesheet.dayweek, homework.num = timesheet.num")
    cursor.execute(f"SELECT timesheet.dayweek , timesheet.num, timesheet.lesson , homework.homework FROM homework INNER JOIN timesheet ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num WHERE homework.date = '04-02-2020'")
    rows = cursor.fetchall()
    return rows

def get_week_homework(table: str, date: str) -> List[Tuple]:

    # cursor.execute(f"SELECT timesheet.dayweek, timesheet.num, timesheet.lesson, homework.homework FROM timesheet LEFT OUTER JOIN homework ON homework.dayweek = timesheet.dayweek, homework.num = timesheet.num")
    cursor.execute(f"SELECT timesheet.dayweek, homework.date, timesheet.num, timesheet.lesson , homework.homework FROM homework INNER JOIN timesheet ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num where date between '04-02-2020' and '11-02-2020'")
    rows = cursor.fetchall()
    return rows

