def formarLista(lnum, b):
	res = b%len(lnum)
	return int(lnum[res-1]);

def sacarUltimo(a, b):
	dos = [2,4,8,6]
	tres = [3,9,7,1]
	cuatro = [4,6]
	siete = [7,9,3,1]
	ocho = [8,4,2,6]
	nueve = [9,1]
	
	if a == 2:
		return formarLista(dos, b)
	elif a == 3:
		return formarLista(tres, b)
	elif a == 4:
		return formarLista(cuatro, b)
	elif a == 7:
		return formarLista(siete, b)
	elif a == 8:
		return formarLista(ocho, b)
	elif a == 9:
		return formarLista(nueve, b)


n = int(raw_input())

while n > 0:
	l = raw_input().split()

	a = l[0]
	b = l[1]

	if a[-1] == '0' or a[-1] == '1' or a[-1] == '5' or a[-1] == '6':
		print a[-1]
	else:
		print sacarUltimo(long(a[-1]), long(b[-1]))

	n = n - 1