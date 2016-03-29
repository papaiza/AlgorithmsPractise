# Largest Prime factor
# max = 600851475143
max = 57
sqrt = Math.sqrt(max)
factor = 2
lastFactor = 1
while max > 1 do
	if max % factor == 0
		lastFactor = factor
		max /= factor
		while max % factor == 0 do
			max /= factor
		end
	end	
	factor += 1
end

puts lastFactor