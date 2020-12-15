import sys
from statistics import mean

meanlist = []
#sys.argv[1] should be a .rate file from iqtree

with open (sys.argv[1],'r') as f:
    for line in f:
        x = line.split()
        if len(x) == 4:
            meanlist.append(x[1])
        else:
            pass

meanlist.pop(0)

meanlist = list(map(float, meanlist))

print (sys.argv[1],mean(meanlist),sep=',')
