# program to take input and read them

def take_input():
	print "\nWelcome to data entry!"
	print "======================\n"
	print "1. Enter data"
	print "2. View entries"
	print "3. Exit"
	print "\nEnter your option : ",
	try:
		option_int = int(raw_input())
		if option_int == 1:
			enter_data()
		elif option_int == 2:
			view_data()
		elif option_int == 3:
			return None
	except ValueError:
		print "NOT VALID ENTRY"
		take_input()

def enter_data():
	print "\nEntering data..."
	c_str = raw_input()
	f_file = open("testfile.txt","a")
	f_file.write(c_str)
	f_file.write('\n')
	f_file.close()
	take_input()

def view_data():
	print "\nViewing data"
	f_file = open("testfile.txt","r")
	c_str = f_file.read()
	print c_str
	f_file.close()
	take_input()

take_input()