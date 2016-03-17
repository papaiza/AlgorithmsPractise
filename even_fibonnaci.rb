sum = 0
n1 = 1
n2 = 1
n3 = 0 
while n2 < 4000000 do 
	sum += n2 if n2 % 2 == 0
	n3 = n1 + n2
	n1 = n2
	n2 = n3
end

puts sum