"""
retorne os numeros primos entre 1 e 100
"""
def eh_primo(numero):
    return True if sum([ 1 for div in range(2,numero) if numero % div == 0 ]) == 0 else False

	
if __name__=='__main__':
	print([x for x in list(range(1,101)) if eh_primo(x)])
	


