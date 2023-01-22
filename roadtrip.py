def cost(distance, fuel_efficiency, cost_of_gallon):
    return distance / fuel_efficiency * cost_of_gallon

distance = int(input("How far did you travel (in miles)? "))
fuel_efficiency = int(input("What is the fuel efficiency of your car (in mpg)? "))
cost_of_gallon = int(input("How much does a gallon of fuel cost (in dollars)? "))

print("Your trip costs " + str(cost(distance, fuel_efficiency, cost_of_gallon)) + " dollars.")