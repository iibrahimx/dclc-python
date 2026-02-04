from datetime import datetime, timedelta
import time
import calendar


# -----------------------------
# Exercise 1: Print Current Date and Time
# -----------------------------
print("=========== Exercise 1 ===========")
# datetime.now() gives current date + time on your computer
print(datetime.now())


# -----------------------------
# Exercise 2: Convert String Into Datetime Object
# -----------------------------
print("\n=========== Exercise 2 ===========")
date_string = "Feb 25 2020 4:20PM"

# strptime means: string parse time
# %b = short month name (Feb)
# %d = day number
# %Y = 4-digit year
# %I = hour in 12-hour format
# %M = minutes
# %p = AM/PM
date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(date_object)


# -----------------------------
# Exercise 3: Subtract a Week From a Given Date
# -----------------------------
print("\n=========== Exercise 3 ===========")
given_date = datetime(2020, 2, 25)

# timedelta(days=7) represents 7 days
new_date = given_date - timedelta(days=7)
print(new_date.date())  # .date() prints only date part


# -----------------------------
# Exercise 4: Format DateTime
# -----------------------------
print("\n=========== Exercise 4 ===========")
given_date = datetime(2020, 2, 25)

# strftime formats date into a nice string
# %A = full weekday name, %d = day number, %B = full month name, %Y = year
print(given_date.strftime("%A %d %B %Y"))


# -----------------------------
# Exercise 5: Find Day of Week
# -----------------------------
print("\n=========== Exercise 5 ===========")
given_date = datetime(2020, 7, 26)

# %A gives weekday name
print(given_date.strftime("%A"))


# -----------------------------
# Exercise 6: Add Week to Given Date
# -----------------------------
print("\n=========== Exercise 6 ===========")
given_date = datetime(2020, 3, 22, 10, 0, 0)

# Add 7 days and 12 hours
future_date = given_date + timedelta(days=7, hours=12)
print(future_date)


# -----------------------------
# Exercise 7: Print Current Time in Milliseconds
# -----------------------------
print("\n=========== Exercise 7 ===========")
# time.time() gives seconds since Jan 1, 1970 (Unix timestamp)
# multiply by 1000 to convert seconds to milliseconds
current_time_ms = int(time.time() * 1000)
print(current_time_ms)


# -----------------------------
# Exercise 8: Convert Datetime into String
# -----------------------------
print("\n=========== Exercise 8 ===========")
given_date = datetime(2020, 2, 25)

# str() converts datetime object into a string like "YYYY-MM-DD HH:MM:SS"
date_as_string = str(given_date)
print(date_as_string)


# -----------------------------
# Exercise 9: Calculate the date 4 months from the current date
# -----------------------------
print("\n=========== Exercise 9 ===========")
given_date = datetime(2020, 2, 25).date()

months_to_add = 4
new_month = given_date.month + months_to_add
new_year = given_date.year

# If month passes 12, wrap around and increase year
if new_month > 12:
    new_month = new_month - 12
    new_year = new_year + 1

# Get last day of the target month (to avoid invalid dates)
last_day = calendar.monthrange(new_year, new_month)[1]

# Keep the same day if possible, else clamp to last day
new_day = given_date.day
if new_day > last_day:
    new_day = last_day

new_date = given_date.replace(year=new_year, month=new_month, day=new_day)
print(new_date)


# -----------------------------
# Exercise 10: Calculate Days Between Two Dates
# -----------------------------
print("\n=========== Exercise 10 ===========")
date_1 = datetime(2020, 2, 25)
date_2 = datetime(2020, 9, 17)

# Subtracting two datetimes gives a timedelta
difference = date_2 - date_1
print(difference.days, "days")
