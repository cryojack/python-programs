# generate all permutations of the following letters 
#'m','r','i','d','u','l' to check if my name is shown
import random
chars = 'ldrium'
name = ''
name_list = []
n = 0
for i in range(0,1000):
	for j in range(0,6):
		name += random.choice(chars)
	name_list.append(name)
	name = ''

while n != len(name_list):
	print name_list[n]
	n += 1