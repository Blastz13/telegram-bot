import os
from typing import Dict, List, Tuple

import sqlite3

conn = sqlite3.connect("finance.db", check_same_thread=False)
cursor = conn.cursor()


def insert(table: str, column_values: Dict):
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
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


# CRUD
def create_homework(table: str, column_values: Dict):
    """Add homework"""
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def create_timetable_lesson(table: str, column_values: Dict):
    """Add lesson in timetable"""
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def get_today_homework(table: str, date: str) -> List[Tuple]:
    """Return today homework"""
    cursor.execute(f"""SELECT timesheet.dayweek, homework.date, timesheet.num, timesheet.lesson , homework.homework 
                        FROM homework INNER JOIN timesheet 
                        ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num AND homework.lesson = timesheet.lesson
                        WHERE homework.date = '{date}'""")
    rows = cursor.fetchall()
    return rows


def get_tomorow_homework(table: str, date: str) -> List[Tuple]:
    """Return tomorow homework"""
    cursor.execute(f"""SELECT timesheet.dayweek , homework.date, timesheet.num, timesheet.lesson , homework.homework 
                        FROM homework INNER JOIN timesheet 
                        ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num AND homework.lesson = timesheet.lesson
                        WHERE homework.date = '{date}'""")
    rows = cursor.fetchall()
    return rows


def get_week_homework(table: str, date) -> List[Tuple]:
    """Return week homework"""
    cursor.execute(f"""SELECT timesheet.dayweek, homework.date, timesheet.num, timesheet.lesson , homework.homework 
                        FROM homework INNER JOIN timesheet
                        ON homework.dayweek = timesheet.dayweek AND homework.num = timesheet.num AND homework.lesson = timesheet.lesson
                        WHERE date BETWEEN '{date.date_start}' AND '{date.date_end}' ORDER BY homework.date""")
    rows = cursor.fetchall()
    return rows


def get_timetable_today(table: str, dayweek: str) -> List[Tuple]:
    """Displays the schedule for the day of the today"""
    cursor.execute(f"""SELECT * 
                    FROM {table} 
                    WHERE dayweek LIKE '{dayweek}%'""")
    rows = cursor.fetchall()
    return rows


def get_timetable_tomorow(table: str, dayweek: str) -> List[Tuple]:
    """Displays the schedule for the day of the tomorow"""
    cursor.execute(f"""SELECT * 
                    FROM {table} 
                    WHERE dayweek LIKE '{dayweek}%'""")
    rows = cursor.fetchall()
    return rows


def get_timetable_dayweek(table: str, dayweek: str) -> List[Tuple]:
    """Displays the schedule for the day of the week"""
    columns_joined = ", ".join(dayweek)
    cursor.execute(f"""SELECT * 
                    FROM {table} 
                    WHERE dayweek LIKE '{dayweek}%'""")
    rows = cursor.fetchall()
    return rows


def get_all_timetable(table: str) -> List[Tuple]:
    """Displays the schedule for the day of the week"""
    cursor.execute(f"""SELECT * FROM timesheet ORDER BY dayweek ='Понедельник'    DESC,
                                                              dayweek ='Вторник'   DESC,
                                                              dayweek ='Среда' DESC,
                                                              dayweek ='Четверг'  DESC,
                                                              dayweek ='Пятница'    DESC,
                                                              dayweek ='Суббота'  DESC,
                                                              dayweek ='Воскресенье' DESC""")
    rows = cursor.fetchall()
    return rows


# Delete
def delete_homework_homework(table: str, dayweek: str, num: str, date: str):
    """Remove homework from timetable"""
    cursor.execute(f"""DELETE FROM '{table}' 
                        WHERE dayweek='{dayweek}' 
                        AND num='{num}' 
                        AND date='{date}'""")
    rows = conn.commit()
    return rows


def delete_lesson_timesheet(table: str, dayweek: str, num: str):
    """Remove lesson from timetable"""
    cursor.execute(f"""DELETE FROM '{table}' 
                        WHERE dayweek='{dayweek}' 
                        AND num='{num}'""")
    rows = conn.commit()
    return rows


# Update
def edit_timetable_lesson(table: str, dayweek: str, num: int, lesson: str):
    """Edits a lesson"""
    cursor.execute(f"""UPDATE '{table}' 
                        SET lesson='{lesson}' 
                        WHERE num='{num}' 
                        AND dayweek='{dayweek}'""")
    rows = conn.commit()
    return rows


def edit_homework_homework(table: str, *answer):
    """Edits a homework"""
    cursor.execute(f"""UPDATE '{table}' 
                        SET homework='{answer[0][3]}' 
                        WHERE num='{answer[0][1]}' 
                        AND dayweek='{answer[0][0]}' 
                        AND date='{answer[0][2]}'""")
    rows = conn.commit()
    return rows

