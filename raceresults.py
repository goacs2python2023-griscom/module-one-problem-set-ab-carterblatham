def race_results(your_time, t2, t3, t4):
    times = [your_time, t2, t3, t4]
    times.sort()
    if times.index(your_time) == 0:
        return "gold"
    elif times.index(your_time) == 1:
        return "silver"
    elif times.index(your_time) == 2:
        return "bronze"
    else:
        return "imaginary"

your_time = input("Please enter your time: ")
t1 = input("Please enter competitor 1's time: ")
t2 = input("Please enter competitor 2's time: ")
t3 = input("Please enter competitor 3's time: ")

print("You won a " + race_results(your_time, t1, t2, t3) + " medal!")