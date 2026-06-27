# x = 5
# if x > 3:
#     print("x is greater than 3")
# elif x == 3:
#     print("x is equal to 3")
# else:
#     print("x is less than 3")

# number = 20
# guess = int(input("guess a number"))
# if number > guess:
#     if abs(guess - number) <= 10:
#         print("your number is too small, but you are <= 10 away")
#     else:
#         print("your number is too small, you're more than 10 away")
# elif number < guess:
#     if abs(number - guess) <= 10:
#         print("your number is too large, but you are <= 10 away")
#     else:
#         print("your number is too large, you're more than 10 away")
# else:
#     print("you guessed the number")





number = 20
wrong = 0
flag = True
while flag:
    guess = int(input("guess a number"))
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

# name = "amogh"
# print("my name is {name}")

# print(f"my name is {name}")

# age = 15
# print(f"I am {age} years old")