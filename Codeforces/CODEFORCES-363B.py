def sumSliceOfList(vector, start, end):
	result = 0
	for i in range(start, end):
		result += vector[i]
	return result

n, k = map(int, raw_input().split())
l = map(int, raw_input().split())
index = 1
smallerSum = sumSliceOfList(l, 0, k)
lastSum = smallerSum

for i in range(1, n-k+1):
	lastSum = (lastSum - l[i-1]) + l[i+k-1]
	
	if (lastSum < smallerSum):
		index = i+1
		smallerSum = lastSum

print index
