def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number i divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string otherwise.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

# my solution
input("Play Fizz Buzz.   Press ENTER to start")
print()

for i in range(1, 102, 2):
    if i == 101:
        print("Congratulations - you win")
        break
    print(fizz_buzz(i))
    print("Your turn")
    guess = input()
    if guess != fizz_buzz(i+1):
        print("Wrong - you lose, the correct answer was {}".format(fizz_buzz(i+1)))
        break


# Tim solution
# next_number = 0
# while next_number < 99:
#     next_number += 1
#     print(fizz_buzz(next_number))
#     next_number += 1
#     correct_answer = fizz_buzz(next_number)
#     players_answer = input("Your go: ")
#     if players_answer != correct_answer:
#         print("Wrong - you lose, the correct answer was {}".format(fizz_buzz(correct_answer)))
#         break
# else:
#     print("Well done, you reached {}".format(next_number))
