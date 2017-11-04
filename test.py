# armstrong number
# an armstrong number is a number which is equal to the sum of the
# cubes of it's digits
# for example 153 is an armstrong number since :
# 1**3 = 1, 5**3 = 125, 3**3 = 27, 1+125+27 = 153

print "Armstrong numbers"
n_str = input("Enter a range : ")
range_int = int(n_str)
num_int = 0
while num_int <= range_int:
	num_int += 1
	print num_int
