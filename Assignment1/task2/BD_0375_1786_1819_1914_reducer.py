#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
dct = {}

for line in sys.stdin:
    line = line.strip()

    word, count = line.split('\t')
    if word not in dct.keys():
    	dct[word] = 0
    dct[word] += 1

li = []  
for data in dct.keys():
	li.append((data,dct[data]))
li.sort()
for data in li:
	print("%s,%s"%(data[0],data[1]))

    

