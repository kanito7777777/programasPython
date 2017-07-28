def sumar(*a):
	s = []
	for i in a:
		s.append(i)
	return s

def sumar2(a, b):
	s = []
	s.append(a)
	s.append(b)
	return s

a = [ [3, 4, 5], [7, 3, 5], [1, 2, 1], [3, 4, 6] ]

#g = (c for c in a)
s = map(sumar, a)
#s = (d for d in a)
print s