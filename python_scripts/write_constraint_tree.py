from __future__ import print_function
import os, re, sys
from Bio import SeqIO

#read in a sequence alignment, write a constraint tree for IQ-Tree in which bacteria and archaeal monophyly is enforced
target_tree = sys.argv[1]
#map tip IDs to domain
tip_to_domain = {}
inh = open("arcbac.csv")
for line in inh:
	fields = re.split("\t", line.rstrip())
	tip_to_domain[fields[0]] = fields[1]
inh.close()

bacts = []
arcs = []

#read the alignment
seqs = SeqIO.index(sys.argv[1], "fasta")
for rec in seqs:
	species = seqs[rec].id
	if tip_to_domain[species] == "Archaea":
		arcs.append(species)
	elif tip_to_domain[species] == "Bacteria":
		bacts.append(species)
	else:
		print("Problem with species " + str(species))

#print constraint tree
bact_bit = ",".join(bacts)
arc_bit = ",".join(arcs)

tree = "((" + bact_bit + "),(" + arc_bit + "));"
print(tree)
