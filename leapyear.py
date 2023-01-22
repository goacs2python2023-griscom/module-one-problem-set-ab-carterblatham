def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 400 != 0 and year % 100 == 0:
        return False
    else:
        return True

year = int(input("Please enter a year: "))

if is_leap_year(year) == True:
    print("The year " + str(year) + " is a leap year.")
else:
    print("The year " + str(year) + " is NOT a leap year.")