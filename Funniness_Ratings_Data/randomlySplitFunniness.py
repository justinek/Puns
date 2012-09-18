import sys, re, string, random

f = open(sys.argv[1], "r")
f1 = open("normalized.long.split1.csv", "w")
f2 = open("normalized.long.split2.csv", "w")

firstline = 0
for l in f:
    if firstline == 0:
        firstline = l
        f1.write(l)
        f2.write(l)
    else:
        if random.randint(0,1) == 0:
            f1.write(l)
        else:
            f2.write(l)

