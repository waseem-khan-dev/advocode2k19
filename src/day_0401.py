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

def Part1(start, end):
  validPasswords = 0

  i = start
  while i < end:
    if IsValidPassword(i):
      validPasswords = validPasswords + 1
    i = i + 1
  return validPasswords

START = 264360
END = 746325
print("Part 1: ", Part1(START, END))