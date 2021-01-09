#!/usr/bin/python3
import sys

l = []

for line in sys.stdin:
	line = line.strip()
	if line[0]!="#":
		x = line.split()
		l.append((str(x[0]),str(x[1])))

l.sort(key=lambda x:x[0],reverse=False)
for i in l:
	s=i[0].strip()+","+str(i[1])
	print(s)
