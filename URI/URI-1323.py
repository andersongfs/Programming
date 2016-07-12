# -*- coding: utf-8 -*-


def qtd_quadrados(num):
	if(num == 1):
		return 1
	return num * num + qtd_quadrados(num - 1)

while (True):
	num = int(raw_input())
	if(num == 0):
		break
	print qtd_quadrados(num)
