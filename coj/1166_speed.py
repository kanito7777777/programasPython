n = int(raw_input())

while n > 0:
	x = int(raw_input())
	l = raw_input().split()

	par =  [i for i in l if int(i)%2 == 0]
	impar =  [i for i in l if int(i)%2 != 0]
	
	print "%d even and %d odd." %(len(par), len(impar))

	n -= 1