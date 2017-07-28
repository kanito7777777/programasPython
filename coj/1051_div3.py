n = long(raw_input())

l = ''
cont = 0
for i in xrange(1, n+1):
	l = l + str(i)
	print l
	if long(l) % 3 == 0:
		cont += 1

print cont