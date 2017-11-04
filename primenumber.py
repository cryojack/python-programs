# prime numbers
print "\nWELCOME TO PRIME NUMBER FINDER"
print "===============================\n"
lr_str = input("Enter a lower range : ")
ur_str = input("Enter an upper range : ")
lower_range_int,upper_range_int = int(lr_str),int(ur_str)
num_int, i = 0,0
prime = False
prime_list = []
for num_int in range(lower_range_int,upper_range_int):
	prime = True
	if num_int > 1:
		for i in range(2,num_int):
			if num_int % i == 0:
				prime = False
	else:
		print "Number should be greater than 1!"
		break
	if prime:
		prime_list.append(num_int)
	#else:
		#print num_int , " is NOT PRIME"
print prime_list