def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(raw_input())
for i in range(n):
	l1 = raw_input()
	l2 = raw_input()
	result = gcd(int(l1, 2), int(l2, 2)) 
	if(result == 1):
		print 'Pair #%d: Love is not all you need!' %(i+1)
	else:
		print 'Pair #%d: All you need is love!' %(i+1)
