months = [31,28,31,30,31,30,31,31,30,31,30,31]
startWeekday = 1

i = 0
weekDay = 1
month = 1
day = 1
year = 1901
while not ((day == 1) & (month == 1) & (year == 2001)):
    #print(day, month, year)
    if (day == 1) & (weekDay == 6):
        i += 1
    day += 1
    weekDay = (weekDay+1) % 7
    if day > months[month-1]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
            if year%4 == 0:
                months[1] = 29
            else:
                months[1] = 28
print(i)