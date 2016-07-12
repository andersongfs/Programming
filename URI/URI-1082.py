# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1082
def getTreeValues(dic, dic2, s):
	for k in dic[s]:
		dic2[l].add(k)
		dic2[l] = getTreeValues(dic, dic2, dic[k])
	if( k != l):
		dic[k] = set()

def conectados(dic, dic2):
	for s in dic.keys():
		getTreeValues(s)


def imprimir(teste, dic):
	contador = 0
	print 'Case #%d:' %(teste+1)
	for l in dic.keys():
		if (len(dic[l]) > 0):
			lista = list(dic[l])
			lista.sort()
			contador+=1
			print lista
	print '%d connected components' %(contador)
	print

alfabeto = ['a', 'b', 'c','d', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
				'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

qtd_entrada = int(raw_input())
for t in range(qtd_entrada):
	v, a = map(int, raw_input().split())
	dic = {}
	for z in range(v):
		dic[alfabeto[z]] = set(alfabeto[z])

	for i in range(a):
		v1, v2 = raw_input().split()
		dic[v1].add(v2)
	dic2 = dic
	conectados(dic, dic2)

	imprimir(t, dic2)
