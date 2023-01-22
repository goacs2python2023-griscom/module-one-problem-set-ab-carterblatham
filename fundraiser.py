def money_raised(tickets):
    return tickets * 5 - 50

tickets = int(input("How many tickets were sold? "))
print("You raised " + str(money_raised(tickets)) + " dollars.")