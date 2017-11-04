#This program prints a multiplication table upto count_int

num1_int = 1
num2_int = 1
res_int = 0
count_int = 10

while num1_int <= count_int:
	res_int = num1_int * num2_int
	print num1_int , " x " , num2_int , " = " , res_int
	num2_int += 1
	if num2_int > count_int:
		num2_int = 1
		num1_int += 1