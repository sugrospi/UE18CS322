#!/usr/bin/python3
import sys
file=sys.argv[1]


V ={}
adj={}
c ={}



f1 = open(file,"r")

for f in f1.readlines():
	f = f.strip()
	x1,x2 = f.split(',')
	x1=x1.strip()
	x2=x2.strip()
	V[x1] = x2	

for line in sys.stdin:
	line=line.strip()
	
	l1,l2 = line.split('|')
	lx= l2.split(',')
	l1 = l1.strip()
	
	adj[l1] = []
	for i in lx:
		adj[l1].append(i)
		
	
	c[l1] = float(V[l1])/len(adj[l1])


l=[]
temp=[]
for node in sorted(adj.keys()):
	l.append((node,0))
	if adj[node]!=[]:
		for child in adj[node]:
			# if child in adj.keys():
			l.append((child,c[node]))
			temp.append(child)
				





for i in l:
	s=str(i[0])+","+str(i[1])
	print(s)




