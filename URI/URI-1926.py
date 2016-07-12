#https://www.urionlinejudge.com.br/judge/pt/problems/view/1926
import math

n = 1000000 + 2
sieve = [True]*(n)
ac_sum = [0] * (n)
sieve[0] = False
sieve[1] = False

limit = int(math.sqrt(n))

for i in range(2, limit):
	if(sieve[i]):		
		for j in range(i*i, n, i):
			sieve[j] = False


for i in range(2, n):
	if(sieve[i]):
		if(sieve[i-2] or sieve[i+2]):
			ac_sum[i] = ac_sum[i-1] + 1
			continue
	ac_sum[i] = ac_sum[i-1]


q = int(raw_input())
for i in range(q):
	a, b = map(int, raw_input().split())
	if(a > b):
		c = a
		a = b
		b = c
	print ac_sum[b] - ac_sum[a - 1]