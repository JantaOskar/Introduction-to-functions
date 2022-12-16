def sum_eo(n, t):
    result = 0
    if t == "e":
        for i in range(0, n, 2):
            result += i
        return result
    elif t == "o":
        for i in range(1, n, 2):
            result += i
        return result
    else:
        return -1


x = sum_eo(7, "o")
print(x)


