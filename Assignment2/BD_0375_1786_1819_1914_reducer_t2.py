#!/usr/bin/python3
import sys
from operator import itemgetter
c={}

for line in sys.stdin:
	line = line.strip()
	node,cont = line.split(',')
	if node not in c:
		c[node] = 0.
	c[node]+=float(cont)

 	

for node in sorted(c.keys()):
	val = 0.15 + 0.85 * c[node]
	st=node.strip()+","+str('%.5f'%val)
	print(st)
