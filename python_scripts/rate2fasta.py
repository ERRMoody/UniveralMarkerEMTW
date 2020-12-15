from Bio import SeqIO
from Bio import AlignIO
import sys


cat1 = []
cat4 = []
#sys.argv[1] should be a .rate file from iqtree

with open (sys.argv[1],'r') as f:
    for line in f:
        x = line.split()
        if len(x) == 4:
            if x[2] == '1':
                cat1.append(x[0])
            elif x[2] == '4':
                cat4.append(x[0])
            else:
                pass
        else:
            pass

alignment = AlignIO.read(open(sys.argv[2]), "fasta")
#this should be the alignment in fasta format

for record in alignment:
    print ('\n>' + record.id)
    for i in cat4:
        print (record.seq[int(i)-1], end = '')
#change the cat variable in the for loop to print the different rate
