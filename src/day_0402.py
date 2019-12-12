def IsValidPassword(password):
    passStr = "" + str(password) + ""

    if len(passStr) != 6:
        return False

    foundAdjacent = False
    i = 1
    while i < len(passStr):
        d1 = passStr[i - 1]
        d2 = passStr[i]

        # Two adjacent digits are the same (like `22` in `122345`).
        if d1 == d2:
            foundAdjacent = True

        # Going from left to right, the digits never decrease; they only ever increase or stay the same (like `111123` or `135679`).
        if d1 > d2:
            return False
        i = i + 1

    if foundAdjacent == False:
        return False

    return True


def isValidPassword2(password):
    password = "" + str(password) + ""
    if len(password) != 6:
        return False
    i = 1
    while i < len(password):
        d1 = password[i - 1]
        d2 = password[i]

        if d1 == d2:
            return True
        i = i + 2
    return False


def Part1(start, end):
    validPasswords = []

    i = start
    while i < end:
        if IsValidPassword(i):
            validPasswords.append(i)
        i = i + 1
    return validPasswords


def Part2(passwords):
    validPasswords = 0

    for x in passwords:
        if isValidPassword2(x):
            validPasswords = validPasswords + 1
    return validPasswords


START = 264360
END = 746325

PASSWORDS = Part1(START, END)
print(Part2(PASSWORDS))
