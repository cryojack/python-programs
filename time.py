# This program takes input as seconds and returns the output in the
# the following format : Hrs - Mins - Secs

remSeconds = 0
hours , minutes , seconds = 0 , 0 , 0

inputSeconds_int = int(input("please enter the time in seconds : "))
hours = inputSeconds_int / 3600
remSeconds = inputSeconds_int % 3600
minutes = remSeconds / 60
if minutes >= 60 :
	hours += 1
	minutes = 0
seconds = remSeconds % 60
if seconds >= 60 :
	minutes += 1
	seconds = 0
print "Hrs : ",hours," Mins : ",minutes," Secs : ",seconds