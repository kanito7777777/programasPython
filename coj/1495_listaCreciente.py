n = int(raw_input())

a = []
for i in xrange(0,n):
	a.append(int(raw_input()))

p = sorted(a)

for x in p:
	print x
#print