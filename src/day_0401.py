def check_ascending(n):
    return "".join(sorted(n)) == n


def check_repeat(n):
    for digit1, digit2 in zip(n, n[1:]):
        if digit1 == digit2:
            return True


def check_two_consecutive_digits(n):
    repeat_count = 0
    for n1, n2 in zip(n, n[1:]):
        if n1 == n2:
            repeat_count += 1
        else:
            if repeat_count == 1:
                return True
            repeat_count = 0
    return repeat_count == 1


p1_count = 0

START = 264360
END = 746325

for n in range(START, END):
    n = str(n)
    if check_ascending(n):
        if check_repeat(n):
            p1_count += 1
print('Result : ' + str(p1_count))
