def IsMoreValidPassword(password ):
	passStr = "" + str(password) + ""


	# It is a six-digit number.
	if len(passStr) != 6:
		return False
	i = 1
	while i < len(passStr):
		d1 = passStr[i-1]
		d2 = passStr[i]
		if d1 > d2:
			return False
		i = i + 1

	chunks = []
	chunk = passStr[0]

	i = 1
	while i < len(passStr):
		if (passStr[i] == passStr[i - 1]):
			chunk = chunk + str(passStr[i])
		elif chunks != None:
			chunks = chunks.append(chunk)
			chunk = "" + str(passStr[i])
		i = i + 1

	# break it into chunks based on repeating numbers
	# chunks := make([]string,0)
	# chunk := string(passStr[0])

	# for i := 1; i < len(passStr); i++ {
	# 	if passStr[i] == passStr[i-1] {
	# 		chunk += string(passStr[i])
	# 	} else {
	# 		chunks = append(chunks,chunk)
	# 		chunk = string(passStr[i])
	# 	}
	# }

	# append last chunk
	if chunks != None:
		chunks = chunks.append(chunk)

	# one of the chunks must be 2
	foundDouble = False
	print(chunks)
	# for _,ch := range(chunks) {
	# 	if len(ch) == 2 {
	# 		foundDouble = true
	# 	}
	# }

	if foundDouble == False:
		return False

	return True

def Part2(start, end):
  i = 0
  validPasswords = 0
  while i < end:
    if (IsMoreValidPassword(i)):
      validPasswords = validPasswords + 1
    i = i + 1

  return validPasswords

START = 264360
END = 746325
print("Answer:", Part2(START, END))