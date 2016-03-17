import string


def int2base(x,base):
	if x == 0 :
		return 0
	digits = []
	while x != 0:
		digits.append(int(x % base))
		x /= base
	reversed = digits[::-1]
	return str(reversed)

print(int2base(42, 16))

