# Deeply proud of this one, I almost want to take out the 
# comments because of how simple it is

f = open('algoIV2.txt', 'r')
genome = f.readline().strip()
k = int(f.readline())
L = f.readline()
t = f.readline()

x = int(len(genome))
L = int(L)
t = int(t)
k = int(k)
print x

# found is the set that holds our answer
found = set()
# the range is the length of the genome minus 
# the length of the clump
for i in range(x - L):
	# splicing off our clumps
	clump = genome[i:i+L]
	# a new for loop now searching within our clump
	for j in range(L-k):
	# splicing off our kmers
	   kmer = clump[j:j+k]
	   # count the kmers within our clumps and compares to 
	   # t (the number of times a kmer should occur in a clump
	   if clump.count(kmer) == t:
	      # add said kmer to the set
	      found.add(kmer)
print found