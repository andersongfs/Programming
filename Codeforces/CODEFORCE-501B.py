# -*- coding: utf-8 -*-

def mudaNome(dicio, chaves):
	novoDicio = {}
	for i in chaves:
		if(dicio.has_key(i)):
			v = dicio[i]
			while(dicio.has_key(v)):
				todel = v
				v = dicio[v]
				del dicio[todel]

			novoDicio[i] = v
	return novoDicio

n = int(raw_input())
dic = {}
minhasChaves = []
for i in range(n):
	a, b = raw_input().split()
	dic[a] = b
	minhasChaves.append(a)

resp = mudaNome(dic, minhasChaves)
print len(resp)
for k in resp.keys():
	print k, resp[k]