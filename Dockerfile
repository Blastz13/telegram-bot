FROM python:3.8

WORKDIR /home

ENV TOKEN="1094632546:AAGu4SvzqVs9wB4t1y7X1nzzJhFc4-yasms"

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . ./

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/home/telegram-bot/main.py"]
