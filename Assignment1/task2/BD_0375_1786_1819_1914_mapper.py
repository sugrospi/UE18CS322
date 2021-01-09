#!/usr/bin/python3
import json
import sys

def clean(dct):
	if not(all(x.isalpha() or x.isspace() for x in dct["word"])):
		return False
	elif not(len(dct["countrycode"]) == 2 and dct["countrycode"].isupper()):
		return False
	elif dct["recognized"] not in (True,False):
		return False
	elif not(len(dct["key_id"]) == 16 and dct["key_id"].isnumeric()):
		return False
	elif len(dct["drawing"]):	
		for x in dct["drawing"]:
			if len(x) == 2:
				if len(x[0]) == len(x[1]):
					if len(x[0]) == 0:
						return False
					for i in range(len(x[0])):
						if not(isinstance(x[0][i],int)) or not(isinstance(x[1][i],int)):							
							return False
				else:
					return False
			else:
				return False
	else:
		return False
	return True		
	

temp = []	
for line in sys.stdin:
	n = len(sys.argv) 
	s = " "
	req = s.join(sys.argv[1:n-1])
	k = sys.argv[-1]
	if clean(json.loads(line.strip())):
		li = list(json.loads(line.strip()).values())
		if req == li[0]:
			x1 = li[5][0][0][0]
			y1 = li[5][0][1][0]
			x1 = x1**2
			y1 = y1**2
			dist = (x1+y1)**0.5
			if dist > int(k):
				temp.append((li[1],1))
							
			else:
				pass	
		else:
			pass
	else:
		pass

temp.sort()

for data in temp:
	print("%s\t%s"%(data[0],data[1]))

