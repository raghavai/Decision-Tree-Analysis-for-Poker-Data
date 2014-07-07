#!/usr/bin/python

import sys
import math
li = []
attrfreq,entropy,valfreq,we_en = {},{},{},{}
counter = 0
val,cnt = 0,0
total = 0
for line in sys.stdin:
	data = line.replace("(",'').replace(")",'').replace("'",'')
	data = data.strip().split(',')
	li.append(data)
	if data[0][0] == 'a':
		counter += int(data[1])
	key = data[0][:4]
	if attrfreq.has_key(key):
		val = attrfreq[key]
		val += int(data[1])
		attrfreq[key] = val
	else:
		attrfreq[key] = int(data[1])

for x in range(len(li)):	
	key1 = li[x][0][:4]
	key2 = li[x][0][-1]
	if attrfreq.has_key(key1):
		if entropy.has_key(key1):
			val = int(li[x][1])/float(attrfreq[key1])
			val = -val*math.log(val,2)
			entropy[key1] += val
		else:
			val = int(li[x][1])/float(attrfreq[key1])
			val = -val*math.log(val,2)
			entropy[key1] = val
	if valfreq.has_key(key2):
		cnt = valfreq[key2]
		cnt += int(li[x][1])
		valfreq[key2] = cnt
	else:
		valfreq[key2] = int(li[x][1])

#total entropy
for key in valfreq:
	val = (valfreq[key]/10)/float(counter)
	val = -val*math.log(val,2)
	total += float(val)
				

for key in entropy:
	if attrfreq.has_key(key):
		char = key[0]
		if we_en.has_key(char):
			val = we_en[char]
			val += (attrfreq[key]/float(counter))*float(entropy[key])
			we_en[char] = val
		else:
			val = (attrfreq[key]/float(counter))*float(entropy[key])
			we_en[char] = val
				


'''for k,v in attrfreq.items():
	print(k,v)	
print(li)
print(counter)
for k,v in entropy.items():
	print(k,v)
for k,v in we_en.items():
	print(k,v)
for k,v in valfreq.items():
	print(k,v)
print(total)'''
for k,v in we_en.items():
	v = total - v
	print(k,v)

