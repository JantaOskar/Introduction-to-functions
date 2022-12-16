def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)  # for debbuging
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


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

answer = multiply(18, 3)
print(answer)

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
