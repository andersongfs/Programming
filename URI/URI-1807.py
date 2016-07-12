n = int(raw_input())
 
def potenciacaoComMod(base, potencia):
	if(potencia == 0):
		return 1 % 2147483647
	elif(potencia == 1):
		return base % 2147483647
	elif(base == 3 and potencia >= 99999999):
		return 482373875 * potenciacaoComMod(base, potencia - 99999999) % 2147483647
	elif(base == 3 and potencia >= 9999999):
		return 126629593 * potenciacaoComMod(base, potencia - 9999999) % 2147483647
	elif(base == 3 and potencia >= 999999):
		return 405365503 * potenciacaoComMod(base, potencia - 999999) % 2147483647
	else:
		if(potencia % 2 ==0):
			return potenciacaoComMod(base * base, potencia/2) % 2147483647
		else:
			return base * potenciacaoComMod(base, potencia-1) % 2147483647
 
print potenciacaoComMod(3,n)






#   Outra forma de calcular exponenciacao
#def expo(a, b):
#  result = 1
#
#  while (b):
#    if (b%2==1):
#      result *= a
#    
#    b /= 2
#    a *= a
#  
#  return result

