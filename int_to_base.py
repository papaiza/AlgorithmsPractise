import string


def int2base(x,base):
	if x == 0 :
		return 0
	digits = ""
	while x != 0:
		digits += str((int(x % base)))
		x /= base
	return digits[::-1]

print(int2base(42, 16))

