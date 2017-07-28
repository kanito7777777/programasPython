n = raw_input()
#print reduce(lambda n,m: n+m, sorted(n))
n = sorted(n)

s = ""
for i in n:
	s += i

print s