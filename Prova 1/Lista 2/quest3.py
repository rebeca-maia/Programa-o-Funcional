def fib(m):
	if m<1:
		return 0
	if m==1:
		return 1
	return fib(m-1)+fib(m-2)

if __name__=='__main__':
	print(fib(4))
"""
retorna o nésimo termo da sequência de fibonacci
"""
