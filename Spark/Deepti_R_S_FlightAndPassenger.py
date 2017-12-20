import sys
from operator import add
from pyspark import SparkContext

sc=SparkContext(appName='AvgNumFlights')

lines1=sc.textFile(sys.argv[1]).map(lambda s: s.encode("ascii", "ignore").split(','))\
            .map(lambda s: (s[1].split(' ')[0].split('/')[0]+'/'+s[1].split(' ')[0].split('/')[2]+', '+s[3]+', '+s[4],int(s[5])))\
            .reduceByKey(add)


output = lines1.collect()

lines2 = sc.textFile(sys.argv[2]).map(lambda s: s.encode("ascii", "ignore").split(',')) \
        .map(lambda s: (s[1].split(' ')[0].split('/')[0] + '/' + s[1].split(' ')[0].split('/')[2] + ', ' + s[3] + ', ' + s[4], int(s[5]))) \
        .reduceByKey(add)

output = lines2.collect()

lines=lines1.join(lines2).sortByKey()
output = lines.collect()
for (Key,Value) in output:
    print("%s, %i, %i" % (Key,Value[0],Value[1]))
