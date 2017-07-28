def sumar(a, b):
	return a + b

s = sumar(5 , 2)
print "suma de enteros", s

s = sumar(7.3, 3.456432)
print "suma de reales", s

s = sumar('A' , 'B')
print "suma de caracteres", s

s = sumar("ingenieria ", "informatica")
print "suma de cadenas:", s


#s = map(sumar, [3, 2, 4], [4, 2, 1])
s = sumar([3, 2, 4], [4, 2, 1])
print "suma de listas:", s

s = sumar((2,3), (1,3))
print "suma de tuplas:", s