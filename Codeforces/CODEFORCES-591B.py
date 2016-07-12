# http://codeforces.com/problemset/problem/591/B
# -*- coding: utf-8 -*-

dic = {}
n, m = map(int, raw_input().split())  # the length of the initial name and the number of designers hired
word = raw_input()
for i in range(n):
	if(dic.has_key(word[i])):
		dic[word[i]].append(i)
	else:
		dic[word[i]] = [i]
for i in range(m):
	x, y = raw_input().split()
	if(not dic.has_key(x)):
		dic[x] = []
	
	if(not dic.has_key(y)):
		dic[y] = []
	aux_x = dic[x]
	aux_y = dic[y]
	dic[x] = aux_y
	dic[y] = aux_x

result = [None] * n
for k in dic.keys():
	for i in dic[k]:
		result[i] = k

print "".join(result)