def sum_divisors(number):
    summa = 0
    for digit in range(1, number + 1):
        if number % digit == 0:
            summa += digit
    return summa


def sum_numbers(num):
    total = 0
    for digit in range(1, num + 1):
        if digit % 2 == 0:
            total -= digit
        else:
            total += digit

    return total






