l = raw_input().split()

n = l[0]
m = l[1]

s = 0L
for x in n:
	for y in m:
		s = s + (int(x)*int(y))

print s
