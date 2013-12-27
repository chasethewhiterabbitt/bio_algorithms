# This is my first bio-algorithm
# This solves the most frequent words problem
# That is how do we find out what strings are occurring
# the most frequently, it is how we begin to synthesize meaning 
# from huge datasets of genomic code


#raw_input() is the text file we are inputting at the command line
text = raw_input()
# k equals the number inside the raw input and converts to an integer
# not sure how this happens
k = int(raw_input())
#l is the character length of the text
l = len(text)

# d stores about 25 strings of their DNA and their frequencies
d = {}
# for loop 32 - 4 + 1 
for i  in range (l - k + 1):
	#kmer slice text i  and i + k
	
	# THE KMER ALGORITHM
	# kmer are groups of 4 in a row that are spliced off the gene into groups
	# There should be 32 or maybe a few more, for each +1, a new group 
	# were spliced off going forward
	
	kmer = text[i : i + k]
	
	# During the iteration of kmer within d, kmer is given a counter as a key
	# so if there are 2 occurrences, 2 will be the key
	
	if kmer in d:
		d[kmer] += 1
	
	#if not kmer = 1
	
	else:
		d[kmer] = 1
		
		
		## Anything above this point has created data
		## Below this line will pull what we want from the data
		
# .values() refers to the keys		
# max returns the largest item in an iterable or among parameter agvs
#So max frequency equals three
max_frequency = max(d.values())


# answer = NOT ANY KMERS THAT EQUAL 1
# kmer for kmer - iterates through kmers
# freq or freq in d.items somehow = 1 
# if freq == max_frequency is false, which might make freq in d.items false
# Therefore not copying into answer

answer = [kmer for kmer, freq in d.items() if freq == max_frequency]
#formats the dictionary
print(' '.join(answer))





