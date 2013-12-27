# This bio_algoII
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'
# FIX CODE AND SHIP!

# In some DNA sequences, the reverse complement is equal to the original
# So this code will find the reverse complement
# The first function reverse will find the reverse of text
# complement will find the the complement of the output of reverse
# This program is for short string input only

text = raw_input()
leng = len(text)

## Save this function
# It takes a string and reverses it like gnirts(string)

def reverse(x):
    lst = []
    for i in range(0,len(x)):

		# list iterates 0 --> 1, as values are added to 10 --> 9
		# reversing the list
        lst.append(x[len(x)-(i+1)])

    lst = ''.join(lst)
    return lst

def complement (y):
	ls = []
	
	for base in y:
		if base == 'A':
			ls.append('T')
		elif base == 'G':
			ls.append('C')
		elif base == 'C':
			ls.append('G')
		elif base == 'T':
			ls.append('A')
	print ''.join(ls)
	
answer = reverse(text)


complement(answer)