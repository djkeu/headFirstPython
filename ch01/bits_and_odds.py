# Bits and odds, pieces of code from the book

import datetime

# P.17
this_day = datetime.date.today()
today =''

if this_day.weekday() == 5:
    today = 'Saturday'
elif this_day.weekday() == 6:
    today = 'Sunday'
else:
    today = ''

print(today)

if today == 'Saturday':
    print("Party!!")
elif today == 'Sunday':
    print("Recover...")
else:
    print("Werken, werken. Alsmaar werken")
