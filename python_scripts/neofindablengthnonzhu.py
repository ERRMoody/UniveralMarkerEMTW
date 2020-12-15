from ete3 import Tree
import sys

t = Tree(sys.argv[1])
tips = []
for tip in t:
    tips.append(tip.name)

Archaea = open("taraarc.csv")
Bacteria = open("tarabac.csv")

archaea = []
bacteria = []

for line in Archaea:
    this_id = line.strip()
    if this_id in tips:
        archaea.append(this_id)

for line in Bacteria:
    this_id = line.strip()
    if this_id in tips:
        bacteria.append(this_id)

all_taxa = archaea + bacteria
ancestorA = t.get_common_ancestor(archaea)
ancestorB = t.get_common_ancestor(bacteria)
ancestorR = t.get_common_ancestor(all_taxa)

t.unroot()
ab_dist = ancestorA.get_distance(ancestorB)
ba_dist = ancestorB.get_distance(ancestorA)
root_dist_a = ancestorA.get_distance(ancestorR)
root_dist_b = ancestorB.get_distance(ancestorR)

print (sys.argv[1])

if ab_dist == root_dist_a:
    t.set_outgroup(ancestorA)
    ab_dist = ancestorB.get_distance(ancestorA)
    print(float(ab_dist)*2.0)
elif ba_dist == root_dist_b:
    t.set_outgroup(ancestorB)
    ba_dist = ancestorA.get_distance(ancestorB)
    print(float(ba_dist)*2.0)
else:
    print(float(ab_dist))

