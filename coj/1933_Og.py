import sys

while True:
	l = raw_input().split()
	a = int(l[0])
	b = int(l[1])

	if a + b == 0:
		break

	print a + b
