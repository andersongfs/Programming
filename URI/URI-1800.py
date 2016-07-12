#https://www.urionlinejudge.com.br/judge/pt/problems/view/1800
q, e = map(int, raw_input().split())
escritoriosVisitados = set().union(map(int, raw_input().split()))
 
for i in range(q):
    escritorio = int(raw_input())
    if escritorio in escritoriosVisitados:
        print 0
    else:
        escritoriosVisitados.add(escritorio)
        print 1