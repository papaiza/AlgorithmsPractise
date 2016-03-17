sum = 0
n1 = 1
n2 = 1
n3 = 0 
while n2 < 4000000:
	if n2 % 2 == 0:
		sum += n2
	
	n3 = n1 + n2
	n1 = n2
	n2 = n3

print(sum)