import fileinput

for l in fileinput.input():
	l = l.split()

	a = l[0]
	b = l[1]

	p = 0
	res = True
	for x in a:
		p = b.find(x, p)
		if p == -1:
			res = False

	if res:
		print "Yes"
	else:
		print "No"
