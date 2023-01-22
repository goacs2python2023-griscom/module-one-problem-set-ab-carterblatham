def compare_dates(year_1, year_2, month_1, month_2, day_1, day_2):
    if year_1 > year_2:
        return 1
    elif year_1 < year_2:
        return 2
    elif month_1 > month_2:
        return 1
    elif month_1 < month_2:
        return 2
    elif day_1 > day_2:
        return 1
    elif day_1 < day_2:
        return 2

year_1 = input("Please enter a value for the year of the first date: ")
month_1 = input("Please enter a value for the month of the first date: ")
day_1 = input("Please enter a value for the day of the month of the first date: ")
year_2 = input("Please enter a value for the year of the second date: ")
month_2 = input("Please enter a value for the month of the second date: ")
day_2 = input("Please enter a value for the day of the month of the second date: ")

print("Date " + str(compare_dates(year_1, year_2, month_1, month_2, day_1, day_2)) + " occurred later.")