#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter
import sys

dic={}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    if word not in dic.keys():
        dic[word]=0

    dic[word]+=1


print('%s' % (dic["reco"]))
print('%s' % (dic["unreco"]))

   

