"""
retorna os n primeiros numeros primos
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
	
	
if __name__=='__main__':
	print(gerar_n_primos(10))
