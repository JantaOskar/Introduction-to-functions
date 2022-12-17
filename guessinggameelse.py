import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number, try again: ".format(temp))


help(get_integer)

highest = 1000
answer = random.randint(1, highest)
print(answer)   #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0


while guess != answer:
    guess = get_integer(": ")
    if guess == answer:
        print("Well done, you guessed it")
        break
    elif guess == 0:
        print("Game over")
        break
    if guess < answer:
        print("Please guess higher")
        print("Enter '0' to quit")
    else:   #guess must be greater than answer
        print("Please guess lower")
        print("Enter '0' to quit")


