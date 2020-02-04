from typing import List, NamedTuple, Optional
from collections import namedtuple
import pytz

import db


answer = namedtuple("home","work")
# Homework(dayweek='Понедельник',num=1,date="2020-02-02", defaults=("None",))
print(answer.dayweek)