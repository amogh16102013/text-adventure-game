import random
number = random.randint(0,50)
wrong = 0
flag = True
while flag:
    guess = int(input("guess a number: \n"))
    if number > guess:
        if abs(number - guess) <= 10:
            print("number is too low, you are <= ten away")
        else:
            print("number is too low, you are more than ten away from the number")
        wrong += 1
    elif number < guess:
        if abs(number - guess) <= 10:
            print("number is too high, you are >= ten away")
        else:
            print("number is too high, you are more than ten away from the number")
        wrong += 1
    else:
        print("you guessed the number")
        print(f"you got {wrong} incorrect guesses")
        flag = False