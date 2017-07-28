def sumar(a, b):
	return a + b

def sumarRango(*a):
	s = 0
	for i in a:
		s += i
	return s 

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
		

a = 5
b = 34
s = sumar(a,b)
print "Enteros: la suma de %d + %d = %d " %(a,b,s)

a = 0.003
b = 34.43
s = sumar(a,b)
print "Reales: la suma de %.3f + %.3f = %.3f" %(a,b,s)

a = "saul "
b = "mamani"
s = sumar(a,b)
print "Cadenas: la suma es %s + %s = %s" %(a,b,s)


s = sumarRango(1,2,3,4,5)
print "La suma de varios numeros es: ", s

n = input("Ingrese N para factorial:" )
f = factorial(int(n))
print "El fatorial de",n,"es: ", f

s = "saul\n"
print s * 5
