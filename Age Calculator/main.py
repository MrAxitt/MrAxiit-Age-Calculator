import datetime

# Intro
print("Welcome to Age Calculator!")

# Importing Data
now = datetime.datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day

#Data Collection
x_birth_year = int(input("Enter your birth year (YYYY):"))
if x_birth_year > current_year:
    print ("ERROR! Your birth year cannot be greater than current year.")
    exit()

x_birth_month = int(input(" Enter your birth month (MM):"))
if x_birth_month > 12:
    print ("ERROR! Your birth month cannot be greater than 12.")
    exit()

x_birth_day = int(input("Enter your birth day (DD):"))
if x_birth_day > 31:
    print ("ERROR! UYour birth month connot be greater than 31.")
    exit()

# Calculation
year = current_year - x_birth_year
if x_birth_month > current_month or (x_birth_month == current_month and x_birth_day > current_day):
    year -= 1

month = current_month - x_birth_month
if month < 0:
    month += 12

day = current_day - x_birth_day
if day < 0:
    day += 30
    month -= 1

if month < 0:
    month +=12
    year -=1

# Data Display
print (f"You are {day} days {month} months and {year} years old")
print ("Thank You for Using Age Calculator1")

