# program to write string to a file

c_str = raw_input("Enter your string : "),
f_file = open("testfile.txt","w")
c_str = str(c_str)
f_file.write(c_str)
f_file.close()