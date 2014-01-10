IF YOU ARE A RECRUITER PLEASE SEE ALGO IV

"Your mind is software, program it
Your body is a shell, change it 
Death is a disease, cure it
Extinction is approaching, fight it!"

 "The intermediate manifestation of the divine presence 
 which we call the DNA code has spent the last two billion years 
 making this planet a Garden of Eden. An intricate web 
 has been woven, a delicate fabric of 
 chemical-electrical-seed-tissue-organism-species. 
 A dancing, joyous harmony of energy transaction is rooted 
 in the 12 inches of topsoil which covers the 
 rock/mineral/fire core of this planet."

SUMMARY OF CODE

These algorithms sort through genetic information to find patterns in the data.

ALGO I:

INPUT: - string called text (genomic information), an integer k, l length of txt

Algorithm: - Uses the input to create a list of
every k sized string, called that value a kmer, 
and put into a list with kmers and frequencies

OUTPUT: - The kmer with the highest frequency, can be multiple answers 

ALGO II:

- Depending on the genome itself, codes that are "reverse complements"
of another can hold the same value/meaning/message, this program finds the 
reverse complement of another string

-INPUT: - a genome string (preferably a kmer) 
if 500 char are input, it will print 500

Algorithm: - first functions reverses the order of a string
the second function prints complement
i.e. 'A' for 'T' and 'C' for 'G' and vice versa

OUTPUT: - Prints the reverse complement of input string

ALGO III:

- The previous algorithms ignore the possibility that
different substrings can overlap one another
EX. ATA in CGATATATC, this is a full proof way to find all
substrings in the genome

INPUT: - A full genome and a substring to look for

Algorithm: - reads from input, splices every possible 
continuos four letter string, and compares them to our 
given substring  

OUTPUT: - the first position of every substring found that 
matches the substring we are looking for 

ALGO IV:

- When we are developing algorithms to sort through massive
genomic datasets sometimes we hear too much noise to decipher
what are/are not actual messages within the code

- Biologists suggest we look for the same messages clumped 
together, that perhaps it is the multiple messages creating 
some type of larger message. Its like the DNA screaming to 
the proteins "BIND HERE!"

- Algorithmically this is a little tougher than our previous problems
because our algorithm is complicated and our datasets are huge.
When I ran E Coli, which is about 5 million characters long (and is 
by no means the most complex organism in creation) it took about an hour 
to process the program. If your using big data sets on this program
you might want to use an off site server.

Input: This program can handle big data sets. The first input is
the genome, the second is the size of the kmer (genomic string we're looking for),
the size of the third is the size of the clump, and the fourth is number of times 
that kmer occurs inside the clump

Algorithm: - We splice off clumps, then search each clump for
kmers. If kmers occur within the clump the number of times that 
the input asked for then that kmer is added to a set

OUTPUT: - Kmers that occur t times within the clump (size L)





