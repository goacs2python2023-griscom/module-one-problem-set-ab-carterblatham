# The guidelines at the bottom confused me so I may
# not have followed them perfectly, but I still successfully
# made the program

def probability(target_rolls, outcomes):
    outcome_count_1 = 0
    outcome_count_2 = 0
    for o in outcomes:
        if o == target_rolls[0]:
            outcome_count_1 += 1
    probability_1 = outcome_count_1 / 6
    for o in outcomes:
        if o == target_rolls[1]:
            outcome_count_2 += 1
    probability_2 = outcome_count_2 / 6
    return probability_1 * probability_2

target_rolls = []
outcomes = []

for i in range(2):
    target_rolls.append(input("Please enter desired outcome " + str(i + 1) + ": "))
for i in range(6):
    outcomes.append(input("Please enter possible outcome " + str(i + 1) + ": "))

print(str(probability(target_rolls, outcomes)))