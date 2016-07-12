# http://codeforces.com/problemset/problem/520/B
import sys
sys.setrecursionlimit(99999)
def calculate_steps(n, m, steps):
	if(m == n):
		return steps
	elif(m % 2 == 0 and m > n):
		return calculate_steps(n, m/2, steps+1)
	else:
		return calculate_steps(n, m+1, steps+1)


n, m = map(int, raw_input().split())
print calculate_steps(n, m, 0)