# https://www.urionlinejudge.com.br/judge/pt/problems/view/1424
# -*- coding: utf-8 -*-
while(True):
	try:
		n, m = map(int, raw_input().split()) # n, the number of elements in the array, and m the number of queries
		l = map(int, raw_input().split())

		dic = {}
		for i in range(len(l)):
			if(dic.has_key(l[i])):
				dic[l[i]].append(i+1) #index + 1 to show correctly output
			else:
				dic[l[i]] = [i+1]

		for i in range(m):
			k, v = map(int, raw_input().split()) # k-th occurrence (from left to right) of an integer v
			if(dic.has_key(v)):
				if(len(dic[v]) < k):
					print 0
				else:
					print dic[v][k-1]
			else:
				print 0

	except EOFError:
		break