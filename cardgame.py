def dad(top, bottom):
    d_count = 0
    a_count = 0
    for i in range(3):
        if top[i].lower() == "d" or bottom[i].lower() == "d":
            d_count += 1
        if top[i].lower() == "a" or top[i].lower() == "a":
            a_count += 1
    return "yes" if d_count >= 2 and a_count >= 1 else "no"

top_letters = input("What are the letters on the top of the cards? ")
bottom_letters = input("What are the letters on the bottom of the cards? ")
print(dad(top_letters, bottom_letters))