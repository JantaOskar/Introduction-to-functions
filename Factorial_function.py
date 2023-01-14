def factorial(number: int) -> int:
    """Return number!"""
    if number == 0:
        return 1
    multiplier = 1
    result = 1
    for i in range(1, number + 1):
        result = multiplier * result
        multiplier += 1
    return result


for i in range(0, 36):
    print(i, factorial(i))
