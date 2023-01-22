def dad(top, bottom):
    d_count = 0
    a_count = 0
    both_count = 0
    for i in range(3):
        this_card = top[i].lower() + bottom[i].lower()
        if "d" in this_card and not "a" in this_card:
            d_count += 1
        elif "a" in this_card and not "d" in this_card:
            a_count += 1
        elif "a" in this_card and "d" in this_card:
            both_count += 1
    while a_count < 1:
        a_count += 1
        both_count -= 1
    while d_count < 2:
        d_count += 1
        both_count -= 1
    return "yes" if d_count >= 2 and a_count >= 1 and both_count >= 0 else "no"
        

top_letters = input("What are the letters on the top of the cards? ")
bottom_letters = input("What are the letters on the bottom of the cards? ")
print(top_letters)
print(bottom_letters)
print(dad(top_letters, bottom_letters))