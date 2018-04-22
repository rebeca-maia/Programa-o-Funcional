#retorne os 100 primeiros elementos da sequência de fibonacci
def fib_rec(n): #acha o n-ésimo número da sequência de fibonacci
	if n<1:
		return 0
	if n==1:
		return 1
	return fib_rec(n-1)+fib_rec(n-2)


if __name__=='__main__':
	print([fib_rec(i) for i in list(range(100))])
