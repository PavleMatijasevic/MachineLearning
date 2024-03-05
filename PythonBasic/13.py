import random
import calendar

print(f"Random number: {random.randint(1,100)}")

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)




