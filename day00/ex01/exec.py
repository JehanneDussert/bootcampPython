import sys

sys.argv.pop(0)
reversedWord = ""
str_len = len(sys.argv)
str_less = str_len - 1
while str_len > 0:
	for word in reversed(sys.argv[str_len - 1]):
		reversedWord += word.swapcase()
	if str_len != 1:
		reversedWord += " "
	str_len -= 1
print(reversedWord)
