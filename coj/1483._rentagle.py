l = raw_input()
t = l

if t == "square":
	a = int(raw_input())
	print a * a
elif t == "rectangle":
	l = raw_input().split()
	a = int(l[0])
	b = int(l[1])
	print a * b