#http://codeforces.com/problemset/problem/268/C
n, m = map(int, raw_input().split())
points = min(n, m) + 1

print points

for i in range(points):
	print i, points-i-1