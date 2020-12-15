from ete3 import Tree
import sys


t = Tree(sys.argv[1])

total = 0

for node in t.traverse():
    loop = node.dist
    total = total + loop

print (total)
