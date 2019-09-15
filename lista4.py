def soma(n1,n2):
	return n1+n2

def inversao(n):
	return -n
	
def subtracao(n1,n2):
	return soma(n1,inversao(n2))

def igual(n1,n2):
	if (n1^n2): return False
	return True
	
def diferente(n1,n2):
	if igual(igual(n1,n2),False):
		return True
	return False
	#	

def incremento(n):
	return soma(n,1)
	
def decremento(n):
	return subtracao(n,1)


def multiplic_nat(n1,n2):
	if maior(n2,1):
		return soma(n1,multiplic_nat(n1,subtracao(n2,1)))
	return n1


def multiplic_int(n1,n2):
	if not n2:
		return 0
	if maior(n2,0):
		return soma(n1,multiplic_int(n1,decremento(n2)))
	return soma(inversao(n1,multiplic_int(n1,incremento(n2))))

def potencia(base,expo):
	if igual(expo,0): return 1
	if maior(expo,1):
		return multiplic_int(base,potencia(base,subtracao(expo,1)))
	return base
	#
 
def divisao(n1,n2,quo=0):
	if maior(n1,n2):
		return divisao(subtracao(n1,n2),n2,incremento(quo))
	return incremento(quo)
	
def raiz(n):
	return n**0.5
		
def absoluto(n):
	if menor(n,0): return inversao(n)
	return n
		
def modulo(n1,n2):
	def aux(r):
		if igual(n1,n2): return 0
		if igual(r,0): return r
		else:
			return r+n2
	return aux(subtracao(n1,multiplic_int(divisao(n1,n2),n2)))
	#

def somab(n1,n2):
	if (n1&n2) <<1:
		return somab((n1 ^ n2), (n1 & n2) << 1 )
	return n1 ^n2

	
def maior(n1,n2):
	if igual(subtracao(somab(n1,n2),absoluto(subtracao(n1,n2))) >>1,n2):
		return True
	return False

def menor(n1,n2):
	if igual(subtracao(somab(n1,n2),absoluto(subtracao(n1,n2))) >>1,n2):
		return False
	return True

def menorouigual(n1,n2):
	if menor(n1,n2) or igual(n1,n2):
		return True
	return False
	
def maiorouigual(n1,n2):
	if maior(n1,n2) or igual(n1,n2):
		return True
	return False
		
if __name__ == '__main__':
	#print(inversao(6))
	#print(subtracao(4,2))
	#print(multiplic_nat(12,2))
	#print(multiplic_int(-12,2))
	#print(potencia(2,3))
	#print(igual(2,2))
	#print(diferente(8,7))
	#print(divisao(9,3))
	#print(somab(99,2))
	#print(maior(99,2))
	#print(modulo(50,7))
	#print(raiz(4))
	#print(menor(1,6))
	#print(menorouigual(3,3))
	#print(maiorouigual(5,4))
