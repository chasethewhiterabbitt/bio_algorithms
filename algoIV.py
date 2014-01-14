f = open('algoIV.txt', 'r')
genome = f.readline().strip()
k = int(f.readline())
L = f.readline()
t = f.readline()

len_genome = int(len(genome))

#I believe there is a bug adding 1 to the size of
#the first line of input, this piece of code deletes it
genome = list(genome)
del(genome[len_genome-1])
genome = "".join(genome)

l = []

for i in range (len_genome - k + 1):
	kmer = genome[i:i +k]
	# list of every possible kmer
	l.append(kmer)

d = {}
for i in range (len(l)):
#Dictionary is made up of a frequency counter (line 1)
#line two appends the location of each indice to d
#Still a little unclear about [0], [1], keep the code for later
	try:
		d[l[i]][0] += 1
		d[l[i]][1].append(i)
	except KeyError:
		d[l[i]] = [1, [i]]

print d

# figure out what this does it might be the answer to the question
kmer_list=filter(lambda x: d[x][0]==4, d.keys())
print kmer_list

# So sliding list 
#collections counter






      
  
   



  
