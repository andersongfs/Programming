#https://www.urionlinejudge.com.br/judge/pt/problems/view/1107
dimensoes = raw_input()
while dimensoes != "0 0":
    dimensoes = map(int, dimensoes.split())
    altura = dimensoes[0]
    comprimento = dimensoes[1]
 
    escultura = map(int, raw_input().split())
    cortes = 0
 
    for i in range(comprimento):
        if escultura[i] == altura:
            continue
        else:
            if i == 0:
                cortes = altura - escultura[i]
            else:
                if escultura[i] >= escultura[i-1]:
                    continue
                else:
                    cortes += escultura[i-1] - escultura[i]
    print cortes
    dimensoes = raw_input()