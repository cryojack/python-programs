# This program checks for even and odd numbers

range_int = 0
n1_int,n2_int,res_int = 1,1,0
n_even_int,n_odd_int = 0,0
print "enter a range : "
range_int = int(input())
while n2_int <= range_int:
	res_int = n1_int * n2_int
	print n1_int, " x " , n2_int , " = " , res_int
	n1_int += 1
	if (res_int % 2) == 0:
		print "EVEN"
		n_even_int += 1
	else:
		print "ODD"
		n_odd_int += 1
	if n1_int > range_int:
		n2_int += 1
		n1_int = 1
print "Even count = ", n_even_int
print "Odd count = ", n_odd_int