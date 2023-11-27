# Head first Python, p.17
import datetime


this_day = datetime.date.today()
# today =''  # No need to define var today here

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
    print("Werken, werken. \nAlsmaar werken.")


# Cleaner version
print()

if this_day.weekday == 5:
    print("Feestjuh!!!")
elif this_day.weekday ==6:
    print(".. ka .. t .. er ..")
else:
    print("werke werke \nalsmaar werke.")

print()
