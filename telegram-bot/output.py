import timesheet
row=""

# homework= timesheet.get_tomorow_homework()
# for i in range(0, len(homework)):
#     if i == 0:
#         row=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     elif homework[i][0] != homework[i-1][0]:
#         row+=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     row+=f"{homework[i][2]}: {homework[i][3]}\n"
# print(row)

# homework= timesheet.get_week_homework()
# for i in range(0, len(homework)):
#     if i == 0:
#         row=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     elif homework[i][0] != homework[i-1][0]:
#         row+=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     row+=f"{homework[i][2]}: {homework[i][3]}\n"

# print(row)

# homework = timesheet.get_timetable_today()
# for i in range(0, len(homework)):
#     if i == 0:
#         row=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     elif homework[i][0] != homework[i-1][0]:
#         row+=f"--------------\n{homework[i][0]}\n{homework[i][1]}\n{homework[i][2]}: {homework[i][3]}\n"
#         continue
#     row+=f"{homework[i][2]}: {homework[i][3]}\n"

# print(row)

homework = timesheet.get_all_timetable()
for i in range(0, len(homework)):
    if i == 0:
        row=f"--------------\n{homework[i][0]}\n{homework[i][1]}.{homework[i][2]}\n"
        continue
    elif homework[i][0] != homework[i-1][0]:
        row+=f"--------------\n{homework[i][0]}\n{homework[i][1]}.{homework[i][2]}\n"
        continue
    row+=f"{homework[i][1]}.{homework[i][2]}\n"

print(row)