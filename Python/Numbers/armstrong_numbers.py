def is_armstrong_number(number):
    num_digits = len(str(number))
    sum = 0
    for x in str(number):
        y = int(x) ** num_digits
        sum += y

    if sum == number:
        return True
    return False