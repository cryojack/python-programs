# Find the longest word in a given string
print "Find your word in the given file"
c_str =  raw_input("Enter your word : ")
c_words = ""
c_file = 'testfile.txt'
f_file = open(c_file,'r')
c_words = f_file.read()
f_file.close()
c_list = c_words.split()
for i in range(len(c_list)):
	if c_str == c_list[i]:
		print "{} > {}".format(c_list[i],i+1)