def verificar(a, b, c):
	return a * a + b * b == c * c

while True:
	n = raw_input()
	l = n.split(' ')

	a = int(l[0])
	if a == 0:
		break
	else:
		b = int(l[1])
		c = int(l[2])

		res = verificar(a, b, c) or verificar(a, c, b) or verificar(b, c, a)
 
		if res:
			print "right"
		else:
			print "wrong"