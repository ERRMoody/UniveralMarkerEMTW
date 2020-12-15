from __future__ import print_function
import os, re, sys
from ete3 import Tree

target_tree = sys.argv[1]
#map tip IDs to domain
tip_to_domain = {}
inh = open("genomemetadata.tsv")
for line in inh:
	fields = re.split("\t", line.rstrip())
	tip_to_domain[fields[0]] = fields[21]
inh.close()

num_arch = 0
num_bact = 0

tree = Tree(target_tree)
for tip in tree:
	the_domain = tip_to_domain[tip.name]
	if the_domain == "Archaea":
		num_arch += 1
	elif the_domain == "Bacteria":
		num_bact += 1
	else:
		print("Problem with " + str(tip.name) + "'s domain assignment.")
	tip.add_feature("domain",the_domain)

print(sys.argv[1] + "\tNum_arch\t" + str(num_arch))
print(sys.argv[1] + "\tNum_bact\t" + str(num_bact))

#now check domain monophyly
arch = tree.check_monophyly(values=["Archaea"], target_attr="domain")[0:2]
bact = tree.check_monophyly(values=["Bacteria"], target_attr="domain")[0:2]
print(sys.argv[1] + "\t" + str(arch[0]) + "\t" + str(arch[1]) + "\t" + str(bact[0]) + "\t" + str(bact[1]))
	
