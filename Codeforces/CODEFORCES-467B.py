# http://codeforces.com/problemset/problem/467/B
n, m, k = map(int, raw_input().split())
players_army = []

for i in range(m+1):
	players_army.append(int(raw_input()))
			
			
ans = 0	
for i in range(m-1, -1, -1):
	if bin(players_army[-1]^players_army[i]).count('1') <= k:
		ans += 1

print ans