t = int(raw_input())

while t > 0:
	l = raw_input()
	l = l.split()

	n = int(l[0])
	m = int(l[1])

	v = [[],[],[],[],[]]

	for i in xrange(0, m):
		nums = raw_input()
		j = 0
		for x in nums.split():
			x = int(x)
			v[j].append(x)
			j += 1

	maxi = 0
	gana = 0    
	for i in xrange(0, n):
		#s = reduce(lambda n,m:n+m, v[i])
		s = sum(v[i])
		if s > maxi:
			maxi = s
			gana = i + 1

	print gana

	t -= 1





####Wimport sys, math
#nums = []

#for line in sys.stdin:
#   for word in line.split():
#      nums.append(float(word))
#nums.reverse()
#for num in nums:
 #  print("%.4f" % math.sqrt(num))