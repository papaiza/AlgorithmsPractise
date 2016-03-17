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
	u.append(1)
	v.append(y)
	while u[i] <= x:
		i += 1
		u.append(u[i - 1] + u[i-1])
		v.append(v[i-1]+ v[i-1])
	return u, v, i

# Multiplication done only by addition, subtraction and <= 
#	Case 1 where x >= u[i -1 ]					Case 2 where x < u[i -1 ]
# |0---------2^i-1---x--------2^i--|			|0-------x--2^i-1--------2^i--|
#			 u[i-1]			  u[i]							u[i-1]		 u[i]
def multiply_3(x, y):
	u, v, j = createU(x,y)
	i = j
	a = 0
	while i != 0:
		# Case 2 does not satisfy the if
		i -= 1
		# Case 1, satisfies the if
		if u[i] <= x:
			x -= u[i]
			a += v[i]
	return a


print(multiply_1(4, 6))
print(multiply_2(4, 6))
print(multiply_3(4, 6))






