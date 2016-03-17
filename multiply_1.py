# Grade school multiplication
# Loop through and sum x, y times
def multiply_1(x, y):
	sum = 0
	while x != 0:
		x = x - 1
		sum += y
	return sum
# Use division to make process faster
def multiply_2(x,y):
	sum = 0
	while x != 0:
		if x % 2 == 0:
			x /= 2
			y *= 2
		else:
			x -= 1
			sum += y
	return sum
# Create the doubling values before hand
def createU(x, y):
	i = 0
	u = []
	v = []
	u[i] = 1
	v[i] = y
	while u[i] <= x:
		i += 1
		u[i] = u[i - 1] + u[i-1]
		v[i] = v[i-1]+ v[i-1]
	return u, v

def multiply_3(x, y):


print(multiply_1(4, 6))
print(multiply_2(4, 6))