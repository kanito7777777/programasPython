while True:
	n = int(raw_input())
	if n == 0:
		break

	abin = str(bin(n))[2:]
	print "The parity of", abin ,"is", abin.count('1') , "(mod 2)."