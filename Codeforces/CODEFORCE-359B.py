# http://codeforces.com/problemset/problem/359/B
n,k = map(int, raw_input().split())
result = ""
 
for i in range(1, n+1):
	if k>0:
		result += str(2*i) + " " + str(2*i-1)
		k -=1
	else:
		result += str(2*i-1) + " " + str(2*i)
	if i!= n:
		result += " "
 
print result