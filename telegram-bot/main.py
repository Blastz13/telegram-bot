# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types, apihelper

import output
import exceptions
import expenses
from course import course_currency
from weather import weather_forecast
from categories import Categories
from timesheet import Homework, Lesson

import config


bot = telebot.TeleBot(token=os.getenv("TOKEN"))

user_markup_menu = telebot.types.ReplyKeyboardMarkup(True, True)
user_markup_menu.row("/timesheet")
user_markup_menu.row("/finance")
user_markup_menu.row("/course")
user_markup_menu.row("/weather")

user_markup_menu_timesheet = telebot.types.ReplyKeyboardMarkup(True, True)
user_markup_menu_timesheet.row("/homework")
user_markup_menu_timesheet.row("/schedule")
user_markup_menu_timesheet.row("/menu")

user_do_menu_timesheet = telebot.types.ReplyKeyboardMarkup(True, True)
user_do_menu_timesheet.row("/today")
user_do_menu_timesheet.row("/tomorow")
user_do_menu_timesheet.row("/week")
user_do_menu_timesheet.row("/add")
user_do_menu_timesheet.row("/edit")
user_do_menu_timesheet.row("/delete")
user_do_menu_timesheet.row("/menu")

user_markup_finance = telebot.types.ReplyKeyboardMarkup(True, True)
user_markup_finance.row("/today")
user_markup_finance.row("/month")
user_markup_finance.row("/expenses")
user_markup_finance.row("/categories")
user_markup_finance.row("/menu")

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    """Отправляет приветственное сообщение и помощь по боту"""

    bot.send_message(message.from_user.id,
                     "Здравствуйте😉!\n"
                     "Я Бот, который умеет:\nРаботать с расписанием📖/timesheet\nCледить за финансами💰 "
                     "/finance\nОтслеживать курс валют💵 /course\nПоказывать погоду🌤 /weather\n ",
                     reply_markup=user_markup_menu)


@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.from_user.id, "Меню Бота:", reply_markup=user_markup_menu)


@bot.message_handler(commands=['timesheet'])
def start_message(message):
    """Ввывод меню бота для расписания"""
    bot.send_message(message.from_user.id, "Команды Расписания:", reply_markup=user_markup_menu_timesheet)


@bot.message_handler(commands=['homework'])
def start_message(message):
    """Ввывод команд для дз"""
    msg = bot.send_message(message.chat.id, "Выберите команду:", reply_markup=user_do_menu_timesheet)
    bot.register_next_step_handler(msg, process_command_step_homework)


def process_command_step_homework(message):
    if message.text == "/today":
        try:
            answer = Homework().get_today_homework()
            bot.send_message(message.from_user.id,
                             output.one_day_homework(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Домашнего задания нету",
                             reply_markup=user_markup_menu_timesheet)

    elif message.text == "/tomorow":
        try:
            answer = Homework().get_tomorow_homework()
            bot.send_message(message.from_user.id,
                             output.one_day_homework(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Домашнего задания нету",
                             reply_markup=user_markup_menu_timesheet)

    elif message.text == "/week":
        try:
            answer = Homework().get_week_homework()
            bot.send_message(message.from_user.id,
                             output.week_homework(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Домашнего задания нету",
                             reply_markup=user_markup_menu_timesheet)

    elif message.text == "/add":
        msg = bot.send_message(message.chat.id,
                               "Введите данные в формате:\n{День недели} {Номер урока} {Название предмета} {Дату в "
                               "формате Y-m-d}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, add_homework)

    elif message.text == "/edit":
        msg = bot.send_message(message.chat.id,
                               "Введите данные в формате:\n{День недели} {Номер урока} {Дату в формате Y-m-d}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, edit_homework)

    elif message.text == "/delete":
        msg = bot.send_message(message.chat.id,
                               "Введите данные в формате:\n{День недели} {Номер урока} {Дату в формате Y-m-d}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, delete_homework)


def add_homework(message):
    try:
        answer = list(message.text.split())
        msg = bot.send_message(message.chat.id,
                               "Введите домашнее задание :",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, add_homework_hm, answer)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    return


def add_homework_hm(message, answer):
    try:
        response = message.text
        answer.append(response)
        response = Homework().add_homework(answer)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Добавлено", reply_markup=user_markup_menu_timesheet)
    return


def edit_homework(message):
    try:
        answer = list(message.text.split())
        msg = bot.send_message(message.chat.id, "Введите домашнее задание :", reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, edit_homework_hm, answer)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    return


def edit_homework_hm(message, answer):
    try:
        response = message.text
        answer.append(response)
        response = Homework().edit_homework(answer)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Изменено", reply_markup=user_markup_menu_timesheet)
    return


def delete_homework(message):
    try:
        answer = Homework().delete_homework(message)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Удалено", reply_markup=user_markup_menu_timesheet)
    return


@bot.message_handler(commands=['schedule'])
def start_message(message):
    """Ввывод команд для расписания"""
    msg = bot.send_message(message.chat.id, "Выберите команду:", reply_markup=user_do_menu_timesheet)
    bot.register_next_step_handler(msg, process_command_step_schedule)


def process_command_step_schedule(message):
    if message.text == "/today":
        try:
            answer = Lesson().get_timetable_today()
            bot.send_message(message.from_user.id,
                             output.one_day_timetable(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Расписание отсутствует",
                             reply_markup=user_markup_menu_timesheet)

    elif message.text == "/tomorow":
        try:
            answer = Lesson().get_timetable_tomorow()
            bot.send_message(message.from_user.id,
                             output.one_day_timetable(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Расписание отсутствует",
                             reply_markup=user_markup_menu_timesheet)

    elif message.text == "/week":
        try:
            answer = Lesson().get_all_timetable()
            bot.send_message(message.from_user.id,
                             output.week_timetable(answer),
                             reply_markup=user_markup_menu_timesheet)
        except:
            bot.send_message(message.from_user.id,
                             "Расписание отсутствует",
                             reply_markup=user_markup_menu_timesheet)
    elif message.text == "/add":
        msg = bot.send_message(message.chat.id,
                               "Введитие данные в формате:\n"
                               "{День недели} {Номер урока} {Название предмета}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, add_schedule)

    elif message.text == "/edit":
        msg = bot.send_message(message.chat.id,
                               "Введитие данные в формате:\n{День недели} {Номер урока} "
                               "{Название предмета на которое хотите изменить}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, edit_schedule)

    elif message.text == "/delete":
        msg = bot.send_message(message.chat.id, "Введитие данные в формате:\n{День недели} {Номер урока}",
                               reply_markup=user_markup_menu_timesheet)
        bot.register_next_step_handler(msg, delete_schedule)


def add_schedule(message):
    try:
        answer = Lesson().add_lesson(message)
    except:
        bot.send_message(message.chat.id,
                         "Ошибка",
                         reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Добавлено", reply_markup=user_markup_menu_timesheet)
    return


def edit_schedule(message):
    try:
        answer = Lesson().edit_lesson(message)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Изменено", reply_markup=user_markup_menu_timesheet)
    return


def delete_schedule(message):
    try:
        Lesson().delete_lesson(message)
    except:
        bot.send_message(message.chat.id, "Ошибка", reply_markup=user_markup_menu_timesheet)
        return
    bot.send_message(message.chat.id, "Удалено", reply_markup=user_markup_menu_timesheet)
    return


@bot.message_handler(commands=['finance'])
def start_message(message):
    """Ввывод меню бота для финансов"""
    bot.send_message(message.from_user.id, "Добавлять расходы: 250 такси\n"
                                           "Сегодняшняя статистика: /today\n"
                                           "За текущий месяц: /month\n"
                                           "Последние расходы: /expenses\n"
                                           "Категории трат: /categories",
                                           reply_markup=user_markup_finance)


@bot.message_handler(commands=['expenses'])
def list_expenses(message):
    """Отправляет последние несколько записей о расходах"""
    last_expenses = expenses.last()
    if not last_expenses:
        bot.send_message(message.from_user.id, "Расходы ещё не заведены")
        return

    last_expenses_rows = [
        f"{expense.amount} руб. на {expense.category_name} — нажми "
        f"/del{expense.id} для удаления"
        for expense in last_expenses]
    answer_message = "Последние сохранённые траты:\n\n* " + "\n\n* " \
        .join(last_expenses_rows)
    bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(regexp="^[0-9]{1,}")
def add_expense(message):
    """Добавляет новый расход"""
    try:
        answ = message.text
        expense = expenses.add_expense(answ)
    except:
        bot.send_message(message.from_user.id, "Вы ввели неверную команду")
        return
    answer_message = "Добавлены траты {} руб на {}\n\n".format(expense.amount, expense.category_name)
    bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(regexp="/del[0-9]{1,}")
def del_expense(message):
    """Удаляет одну запись о расходе по её идентификатору"""
    try:
        row_id = int(message.text[4:])
        expenses.delete_expense(row_id)
        answer_message = "Удалил"
        bot.send_message(message.from_user.id, answer_message)
    except:
        answer_message = "Вы ввели неверную команду"
        bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(commands=['categories'])
def categories_list(message):
    """Отправляет список категорий расходов"""
    categories = Categories().get_all_categories()
    answer_message = "Категории трат:\n\n* " + \
                     ("\n* ".join([c.name + ' (' + ", ".join(c.aliases) + ')' for c in categories]))
    bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(commands=['today'])
def today_statistics(message):
    """Отправляет сегодняшнюю статистику трат"""
    answer_message = expenses.get_today_statistics()
    bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(commands=['month'])
def month_statistics(message):
    """Отправляет статистику трат текущего месяца"""
    answer_message = expenses.get_month_statistics()
    bot.send_message(message.from_user.id, answer_message)


@bot.message_handler(commands=['course'])
def start_message(message):
    """Функция для ввывода курса валют"""
    user_do_menu_course = telebot.types.ReplyKeyboardMarkup(True, True)
    user_do_menu_course.row("USD")
    user_do_menu_course.row("EUR")
    user_do_menu_course.row("RUR")
    user_do_menu_course.row("UAH")
    msg = bot.send_message(message.chat.id, "Введите валюту или выберите из списка:", reply_markup=user_do_menu_course)
    bot.register_next_step_handler(msg, process_coin_step)


def process_coin_step(message):
    try:
        menu_remove = types.ReplyKeyboardRemove()
        user_markup_after_do = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup_after_do.row("/menu")
        user_markup_after_do.row("/course")
        bot.send_message(message.chat.id, course_currency(message.text), reply_markup=user_markup_after_do)

    except Exception as e:
        bot.reply_to(message, 'ooops!')


@bot.message_handler(commands=['weather'])
def start_message(message):
    """Функция для ввывода погоды"""
    user_do_menu_weather = telebot.types.ReplyKeyboardMarkup(True, True)
    user_do_menu_weather.row("Рузаевка")
    user_do_menu_weather.row("Саранск")
    user_do_menu_weather.row("Москва")
    user_do_menu_weather.row("Санкт-Петербург")
    msg = bot.send_message(message.chat.id,
                           "Введите город или выберите из списка:",
                           reply_markup=user_do_menu_weather)
    bot.register_next_step_handler(msg, process_weather_step)


def process_weather_step(message):
    try:
        menu_remove = types.ReplyKeyboardRemove()
        user_markup_after_do = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup_after_do.row("/menu")
        user_markup_after_do.row("/weather")
        bot.send_message(message.chat.id, weather_forecast(message.text), reply_markup=user_markup_after_do)

    except Exception as e:
        bot.reply_to(message, 'ooops2!')


if __name__ == '__main__':
    bot.polling()
