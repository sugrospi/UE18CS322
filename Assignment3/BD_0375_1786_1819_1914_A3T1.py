#!/usr/bin/python3
import sys
from operator import add

from pyspark.sql import SparkSession

def parse(x,word,recognized,Total_Strokes):
	xs = x.split(',')
	return xs[word],xs[recognized],xs[Total_Strokes]
	
	
def cnt(x):
	return x[1],int(x[2])
	
if __name__ == "__main__":
	spark = SparkSession\
	        .builder\
	        .appName("Task1")\
	        .getOrCreate()
	l = []
	for i in sys.argv:
		l.append(i)
	file = l.pop(0)	
	link = l.pop()
	l.pop()
	req = " ".join(l)        	       	
	lines = spark.read.text(link).rdd.map(lambda r : r[0])
	li = lines.take(1)[0].split(',')
	word = li.index("word")
	timestamp = li.index("timestamp")
	recognized = li.index("recognized")
	key_id = li.index("key_id")
	Total_Strokes = li.index("Total_Strokes")
	counts = lines.map(lambda x:parse(x,word,recognized,Total_Strokes)).filter(lambda x: x[0] == req)
	filteredop = counts.collect()
	if len(filteredop) == 0:
		print("0.00000")
		print("0.00000")
		sys.exit(-1)
	number = counts.map(lambda x:(x[1],1)).reduceByKey(add)		
	number = number.collect()
	addn = counts.map(lambda x:cnt(x)).reduceByKey(add)
	addn = addn.collect()
	if len(number) == 2:
		ans1 = (addn[0][1]/number[0][1])
		ans2 = (addn[1][1]/number[1][1])
		print(round(ans1,5))
		print(round(ans2,5))
		sys.exit(-1)
	else:
		if number[0][0].upper() == 'FALSE':
			ans1 = "0.00000"
			ans2 = (addn[0][1]/number[0][1])
			print(ans1)
			print(round(ans2,5))
		else:
			ans2 = "0.00000"
			ans1 = (addn[1][1]/number[1][1])
			print(round(ans1,5))
			print(ans2)
