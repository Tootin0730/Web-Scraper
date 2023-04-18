from random import randint

user_choice = int(input("Guess a number between 1~50: "))

pc_choice = randint(1, 50)

if user_choice == pc_choice:
    print("You won!")
elif user_choice > pc_choice:
    print("Lower!", pc_choice)
elif user_choice < pc_choice:
    print("Higher!", pc_choice)