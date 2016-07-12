# http://codeforces.com/problemset/problem/18/C

n = int(raw_input())
numbers = map(int, raw_input().split())
accSum = [0]*n
reverseAccSum = [0]*n

for i in range(n):
	if i != 0:
		accSum[i] = numbers[i] + accSum[i-1]
		reverseAccSum[n-i-1] = numbers[n-i-1] + reverseAccSum[n-i]
	else:
		accSum[i] = numbers[i]
		reverseAccSum[n-i-1] = numbers[n-i-1]

output = 0

for i in range(n-1):
	if accSum[i] == reverseAccSum[i+1]:
		output +=1

print output