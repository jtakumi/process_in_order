import os,json

array = [[10,20],[30,40],[50,60],[70,80],[90,100]]

with open('./array_test/test.txt',"r") as f:
    d = f.readline()
    d =list(d.replace('\n',''))
for i in d:
    l = d[i][0]
    r = d[i][1]

for j in d:
    if l[j] in array and r[j] in array:
        print('true')
    else:
        print('false')