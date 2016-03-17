# Greatest Common Divisor
def gcd(a, b):
	x = a
	y = b
	while y != 0:
		x_new = y
		y_new = x % y
		x = x_new
		y = y_new
	return x

print(gcd(44, 64))
print(gcd(10000000000001, 9999999999999))
