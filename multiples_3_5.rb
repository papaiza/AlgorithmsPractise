sum = 0
1000.times do |n|
	if n % 5 == 0 and n % 3 == 0
		sum += n
	elsif n % 5 == 0
		sum += n
	elsif n % 3 == 0
		sum += n
	end
end

puts "The sum is #{sum}"