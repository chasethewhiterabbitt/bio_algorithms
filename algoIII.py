# Different occurences of a substring 
# can overlap one another ex. ATA in CGATATATC
# This algorithm is a full proof way to find all substrings
# INPUT - full genome string and substring we are looking for
# ALGO - reads from input, splices every possible continuous
# four letter string, if any of them equal our substring
# the first position of the string is printed


f = open('algoIII.txt', 'r')

x = f.readline()
y = f.readline()

# Converts the string into a list then back to a string
# For some reason len() keeps adding 1 xtra character
# might be a bug in the text editor

x = list(x)
del(x[z-1])
x = "".join(x)

a = len(x) 
b = len(y)

for i in range (b - a+1):
	answer = y [i:i+a]
	if answer == x:
		print i
	
	



	
