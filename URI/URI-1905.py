# https://www.urionlinejudge.com.br/judge/pt/problems/view/1905
mapa = []
def dfs(x,y):
	global mapa
	if(not(x == y == 0) and mapa[x][y] != 0):
		return
	mapa[x][y] = -1
	if(0<= x+1 < 5 and 0 <= y < 5): dfs(x+1,y)
	if(0<= x < 5 and 0 <= y+1 < 5): dfs(x,y+1)
	if(0<= x-1 < 5 and 0 <= y < 5): dfs(x-1,y)
	if(0<= x < 5 and 0 <= y-1 < 5): dfs(x,y-1)
 
for i in range(int(raw_input())):
	mapa = []
	for j in range(5):
		entrada = raw_input()
		while(not entrada.strip()):
			entrada = raw_input()
		mapa.append(map(int,entrada.split()))
	dfs(0,0)
	if mapa[4][4] == -1:
		print "COPS"
	else: print "ROBBERS"