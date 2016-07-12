#https://www.urionlinejudge.com.br/judge/pt/problems/view/1802
p = map(int, raw_input().split())
m = map(int, raw_input().split())
f = map(int, raw_input().split())
q = map(int, raw_input().split())
b = map(int, raw_input().split())
k = int(raw_input())
combinacoes = []
for a in p[1:]:
	for a1 in m[1:]:
		for a2 in f[1:]:
			for a3 in q[1:]:
				for a4 in b[1:]:
					combinacoes.append(a+a1+a2+a3+a4)

combinacoes.sort(reverse=True)

print sum(combinacoes[:k])