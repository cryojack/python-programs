# program to count words, characters

def countWord():
	c_str,c_char = "",""
	c_str = raw_input("Enter a string : ")
	c_char = c_str.split()
	print "Word count : ", len(c_char)

def countChar():
	c_str,c_char = "",""
	charcount_int = 0
	c_str = raw_input("Enter a string : ")
	for c_char in c_str:
		if c_char is not " " or "\t" or "\n":
			charcount_int += 1
	print "Character count : ", charcount_int