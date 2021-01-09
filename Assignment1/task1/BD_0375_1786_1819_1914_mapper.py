#!/usr/bin/python3
import json
import sys
import datetime
import calendar

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
				if len(x[0]) == len(x[1]) and len(x[0])!=0:
					
					for i in range(len(x[0])):
						if not(isinstance(x[0][i],int)) or not(isinstance(x[1][i],int)) :
							return False
				else:
					return False
			else:
				return False
	else:
		return False
	return True		
	
def findDay(date):
	born = datetime.datetime.strptime(date,'%Y-%m-%d').weekday()
	return (calendar.day_name[born])



for line in sys.stdin:
	
	n = len(sys.argv)
	req = "" 
	for i in range(1,n):

		req += sys.argv[i]

		if i != n-1:
			req += " "
	if clean(json.loads(line.strip())):

		li = list(json.loads(line.strip()).values())
		
		for x in li[:1]:

			if x == req:
				if li[3] == True:
					print("reco\t%s"%(1))
				else:
					if findDay(li[2][:10]) in ("Sunday", "Saturday"):
						print("unreco\t%s"%(1))

	else:
		pass

