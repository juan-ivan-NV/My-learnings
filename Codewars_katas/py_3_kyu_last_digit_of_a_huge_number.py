def last_digit(lst):
    exp = 1
    for i in reversed(lst):
        exp = i ** (exp if exp < 4 else exp % 4 + 4)
    return exp % 10