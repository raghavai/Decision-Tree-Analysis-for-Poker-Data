#!/usr/bin/python

import sys
val = 0
keyval = {}
keygen = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j'}
for line in sys.stdin:
    data = line.strip().split(",")
    a,b,c,d,e,f,g,h,i,j,cls = data
    for x in range(len(data)-1):
	key = keygen[x]+'_'+data[x]+' _'+cls	
	if keyval.has_key(key):
	    val = keyval[key] 
	    val += 1
	    keyval[key] = val
	else:
	    keyval[key] = 1
for k,v in keyval.items():
    print(k,v)

