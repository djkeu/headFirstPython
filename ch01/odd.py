from datetime import datetime

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

right_this_time = datetime.today().minute

"""
Alt:
time_now = datetime.today()
right_this_minute = time_now.minute
"""

if right_this_time in odds:
    print("Deze minuut ziet er nogal oneven uit.")
else:
    print("Dit is geen oneven minuut zeg.")
    