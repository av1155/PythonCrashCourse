import random
import sys


def startGame():
    print("Guess the number! From 0 to 20")

    attemps = 10
    for i in range(attemps, 0, -1):
        if i == 3:
            print("You have three more attemps. Choose wisely!")

        random_number = random.randint(0, 20)
        user_guess = input("\nWhat is your guess? (Q to quit)\n> ")

        if user_guess.lower() == "q":
            main()
        elif int(user_guess) < 0 or int(user_guess) > 20:
            print("Write a valid number, between 0 and 20.")
            i += 1

        if int(user_guess) == random_number:
            print("You win! Guess is correct")
            print("The number was:", random_number)
            main()
        elif int(user_guess) != random_number:
            print("EHHH... wrong")
            print("The number was:", random_number)
        else:
            main()


def main():
    while True:
        print("Q to quit, R to replay, S to start")
        user_choice = input("Enter your choice: ")

        if user_choice.lower() == "q":
            sys.exit()

        if user_choice.lower() == "s":
            startGame()

        if user_choice.lower() == "r":
            startGame()


if __name__ == "__main__":
    main()
