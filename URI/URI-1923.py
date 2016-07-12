# https://www.urionlinejudge.com.br/judge/pt/problems/view/1923
# -*- coding: utf-8 -*-
	
def bfsWithLevel(graph, root, level):
    queue = [root]
    result = []
    it = len( graph[queue[0]] ) + 1
    while level >= 1:
        this_it = it
        it = 0
        for i in range(this_it):
            if(not queue):
                break
            vertex = queue.pop(0)
            if(vertex  not in result):
                queue.extend(graph[vertex])
                result.append(vertex)
                it += len(graph[vertex])
                
        level -= 1
    return result[1:]

# the quantity of relations to be considered and the maximum relashionship degree
n, g = map(int, raw_input().split())  
graph = {}
answer = []
for i in range(n):
	a, b = raw_input().split()
	if(graph.has_key(a)):
		graph[a].add(b)
	else:
		graph[a] = set([b])
	if(graph.has_key(b)):
		graph[b].add(a)
	else:
		graph[b] = set([a])

result =  bfsWithLevel(graph,"Rerisson", g)
result.sort()
print len(result)
for i in range(len(result)):
    print result[i]