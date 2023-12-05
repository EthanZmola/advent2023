import numpy as np 

file = open("day3Practice.txt")

all = ""
repeat = 0
for line in file:
    repeat = len(line)
    all+= line
all = all.replace('\n','')
