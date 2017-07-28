n = int(raw_input())

if n == 0:
	print "1"
else:
	s = 0L
	for i in xrange(1, abs(n)+1):
	 	s += i

	if n > 0:
		print s
	else:
		print (s - 1) * (-1)