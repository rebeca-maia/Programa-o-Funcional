#retorna os numeros triangulares entre 1 e 100
def triangula(n):
	if n<1:
		return 0
	return (n*(n+1))//2


if __name__=='__main__':
	print([triangula(i) for i in list(range(1,101))])
