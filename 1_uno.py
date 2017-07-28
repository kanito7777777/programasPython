a = 26
b = 11.3890
c = 5
d = 3.58789

#suma
s = a + c
print "suma de enteros: " + str(s)
print "suma de enteros:", s
print "%d + %d = %d" %(a, c, s)

s = b + d
print "suma de reales:", s
print "%f + %f = %.2f" %(b, d, s)

#restar
r = a - c
print "La resta es =", r

#multiplicar
m = a * d
print "La multiplicacion es =", m

#dividir
div = a / float(c)
print "%d / %d = %.2f" %(a,c,div) , " ---- ",
div = b / d
print "%.2f / %.2f = %.2f" %(b,d,div)

#modulo
md = d % b
print "El modulo es=", md

#exponente

exp = c ** 3
print "El exponente de 5 ^ 3 =", exp 



#cadenas
print "\n============cadenas========"

cad = """hola
a 
todos
nosotros
"""

print cad

cad = "hola" * 3
print cad 
