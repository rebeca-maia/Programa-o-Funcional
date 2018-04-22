"""
escreva uma função que receba um natural n e uma função geradora. A função deve retornar uma lista de n números gerados de acordo com a 
geradora.
"""

def gerar_n_primos(limite,temp=2):
	def primo(n,div=2):
		if n<=1:
			return False
		elif n==div:
			return True
		if n%div==0 and div<n:
			return False
		else:
			return primo(n,div+1)
	if limite==0:
		return []
	else:
		if primo(temp):
			return [temp]+gerar_n_primos(limite-1,temp+1)
		return gerar_n_primos(limite,temp+1)

def gerar_n_fib(limite):
	def fib(m):
		if m<1:
			return 0
		if m==1:
			return 1
		return fib(m-1)+fib(m-2)
	if limite==0:
		return []
	else:
		return gerar_n_fib(limite-1)+[fib(limite-1)][::-1]
		
def gerar_n_triang(limite):
	def triangula(n):
		if n<1:
			return 0
		return (n*(n+1))//2
	if limite==0:
		return []
	else: return gerar_n_triang(limite-1)+[triangula(limite-1)][::-1]
	

def geradora(numb,name):
	if name=="primo":
		return gerar_n_primos(numb)
	elif name=="fibonacci":
		return gerar_n_fib(numb)
	elif name=="triangular":
		return gerar_n_triang(numb)
	else:
		print("Não existe!")
	
if __name__=='__main__':
	print(geradora(5,"fibonacci"))
	print()
	print(geradora(5,"primo"))
	print()
	print(geradora(5,"triangular"))
		
