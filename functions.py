def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a `string` is a palindrome.

    The function accepts only alphanumeric characters in a string.

    :param string: The String to be checked.
    :return: True if palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a `string` is a palindrome.

    The function ignores whitespace, capitalistaion and
    punctuation in the sentence.

    :param sentence: The String to be checked.
    :return: True if palindrome, False if not a palindrome.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # for debbuging
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonnaci(n: int) -> int:
    """Return the `n` th Fibonnaci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonnaci(i))

p = fibonnaci()

# sentence_input = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence_input):
#     print("'{}' is a palindrome".format(sentence_input))
# else:
#     print("'{}' is not a palindrome".format(sentence_input))
#
# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# answer = multiply(18, 3)
# print(answer)

#
# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)
