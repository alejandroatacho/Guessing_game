import random

max_num = input("what is the maximum number?: ")
#min_num = input("what is the minimum number?: ")
'''
if max_num.isdigit():
    max_num = int(max_num)
    if max_num <= 0:
        print("Please type a number larger then zero next time")
        quit()
    else:
        print("Please type a number next time.")
        quit()'''
random_number = random.randint(0, int(max_num))

# print(random_number)
while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    if user_guess == random_number:
        print("You got it!")
    else:
        print("You got it wrong!")
