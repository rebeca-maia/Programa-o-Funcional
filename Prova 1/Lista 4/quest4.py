#retorna os numeros perfeitos entre 1 e 100
def eh_primo(numero):
    return True if sum([ 1 for div in range(2,numero) if numero % div == 0 ]) == 0 else False
    
def divisores(n):
	return [i if i in list(range(1,n))if n%i==0]
	
def listsoma(l):
	if len(l)==1:
		return l[0]
	return l[0]+listsoma(l[1:])

def perfeito(n):
	if eh_primo(n): return False
	if listasoma(divisores(n))==n: return True


if __name__=='__main__':
	print([j for j in list(range(1,101)) if perfeito(j)) 
