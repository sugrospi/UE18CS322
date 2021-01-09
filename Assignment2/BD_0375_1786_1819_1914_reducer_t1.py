#!/usr/bin/python3

from operator import itemgetter
import sys

file=sys.argv[1]

dic ={}

for line in sys.stdin:
	line = line.strip()
	l1,l2 = line.split(',')
	l1 = l1.strip()
	l2 = l2.strip()
	if l1 not in dic.keys():
		dic[l1] = []
	dic[l1].append(l2)



for node in  sorted(dic.keys()):
	a=dic[node]
	st=""
	for i in a:
		st+=str(i)+","
	st=st[0:-1]
	s=node.strip()+"|"+st

	print(s)


f3=open(file,'w')

for i in sorted(dic.keys()):
	# str1=""+i.strip()+", 1"+"\n"

	
	f3.write(i.strip()+",1"+"\n")
	
f3.close()










