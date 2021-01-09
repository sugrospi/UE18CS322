#!/usr/bin/python3
import sys
from operator import add

from pyspark.sql import SparkSession

def fun(x):
        return(x.word,x.recognized,x.Total_Strokes,x.countrycode)

if __name__ == "__main__":
        spark = SparkSession\
        .builder\
        .appName("Task2")\
        .getOrCreate()
        l = []
        for i in sys.argv:
                l.append(i)
        shape_stat = l.pop()
        shape = l.pop()
        file = l.pop(0)
        k =int( l.pop())
        req = " ".join(l)
        if k<=0:
                print(0)
                sys.exit(-1)
        df1 = spark.read.load(shape_stat,format="csv",interSchema="true",header = "true")
        df2 = spark.read.load(shape,format="csv",interSchema="true",header="true")
        df1 = df1.drop("word")
        jn = df1.join(df2 ,on="key_id")
        jn2 = jn.rdd.map(lambda x:fun(x)).filter(lambda x: x[0] == req and x[1].upper() == "FALSE" and int(x[2]) < k)
        filteredop = jn2.collect()
        if len(filteredop) == 0:
                print(0)
                sys.exit(-1)

        jn3 = jn2.map(lambda x:(x[3],1)).reduceByKey(add)
        op = jn3.collect()
        op.sort(key = lambda x : x[0] ,reverse = False)

        for i,j in op:
                print("%s,%i"%(i,j))
