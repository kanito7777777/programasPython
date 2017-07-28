n = int(raw_input())

while n > 0:
	a = long(raw_input())
	if(a % 6 == 0):
		print "YES"
	else:
		print "NO"
	n = n - 1