# A simple password generator
import random
password = ''
pass_list = []
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*.'
for i in range(0,20):
	for j in range(0,8):
		password += random.choice(chars)
	pass_list.append(password)
	password = ''
print pass_list