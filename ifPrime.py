from math import sqrt
from itertools import count, islice

# Determine whether it is a prime using itertools library
def is_prime1(n):
	if n < 2:
		return False
	for number in islice(count(2), int(sqrt(n)- 1)):
		if n % number == 0:
			return False
	return True

# Determine whether it is a prime using iteration
def is_prime2(n):
	if n < 2:
		return False
	for num in range(2, int(sqrt(n) + 1)): # Max divisor of a number is the sqrt(n)
		if n % num == 0:
			return False
	return True

print("Is 17 a prime: " + str(is_prime1(17)))
print("Is 35 a prime: " + str(is_prime1(35)))
print("Is 89 a prime: " + str(is_prime1(89)))


print("Is 17 a prime: " + str(is_prime2(17)))
print("Is 35 a prime: " + str(is_prime2(35)))
print("Is 89 a prime: " + str(is_prime2(89)))