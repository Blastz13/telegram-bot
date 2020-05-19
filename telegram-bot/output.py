import timesheet


def one_day_homework(homework):
    row = ""
    homework.sort(key=lambda a: a[1])
    for i in range(0, len(homework)):
        if i == 0:
            row = f"{homework[i][0]}\n------------------\n{homework[i][1]}\n" \
                  f"{homework[i][2]}. {homework[i][3]}: {homework[i][4]}\n "
            continue
        elif homework[i][0] != homework[i - 1][0]:
            row += f"{homework[i][0]}\n------------------\n{homework[i][1]}\n" \
                   f"{homework[i][2]}. {homework[i][3]}: {homework[i][4]}\n"
            continue
        row += f"{homework[i][2]}. {homework[i][3]}: {homework[i][4]}\n"
    return row


def week_homework(homework):
    row = ""
    for i in range(0, len(homework)):
        if i == 0:
            row = f"------------------\n{homework[i][0]}\n{homework[i][1]}\n" \
                  f"{homework[i][2]}: {homework[i][3]} :  {homework[i][4]}\n"
            continue
        elif homework[i][0] != homework[i - 1][0]:
            row += f"------------------\n{homework[i][0]}\n{homework[i][1]}\n" \
                   f"{homework[i][2]}: {homework[i][3]} :  {homework[i][4]}\n"
            continue
        row += f"{homework[i][2]}: {homework[i][3]} :  {homework[i][4]}\n"
    return row


def one_day_timetable(homework):
    row = ""
    homework.sort(key=lambda a: a[1])
    for i in range(0, len(homework)):
        if i == 0:
            row = f"------------------\n{homework[i][0]}\n" \
                  f"{homework[i][1]}. {homework[i][2]}\n"
            continue
        elif homework[i][0] != homework[i - 1][0]:
            row += f"------------------\n{homework[i][0]}\n" \
                   f"{homework[i][1]}. {homework[i][2]}\n"
            continue
        row += f"{homework[i][1]}. {homework[i][2]}\n"
    return row


def week_timetable(homework):
    row = ""
    for i in range(0, len(homework)):
        if i == 0:
            row = f"--------------\n{homework[i][0]}" \
                  f"\n{homework[i][1]}.{homework[i][2]}\n"
            continue
        elif homework[i][0] != homework[i - 1][0]:
            row += f"--------------\n{homework[i][0]}" \
                   f"\n{homework[i][1]}.{homework[i][2]}\n"
            continue
        row += f"{homework[i][1]}.{homework[i][2]}\n"
    return row
