"""
escreva uma função que recebe uma lista e um pivô e retorna duas listas, uma com todos os números menores que o pivô e outra com os maiores
ou iguais. Não permita que ocorra IndexError
"""
#primeira solução
def piv(l,i):
	def menores(lm):
		if lm==[]:
			return []
		if lm[0]<l[i]:
			return [lm[0]]+menores(lm[1:])
		return menores(lm[1:])
	def maiores(lM):
		if lM==[]:
			return []
		if lM[0]>=l[i]:
			return [lM[0]]+maiores(lM[1:])
		return maiores(lM[1:])
	try:
		return menores(l),maiores(l)
	except IndexError:
		return l,[]
		

#segunda solução
def menor_maior(l,i):
	def separa(cl,lm,lM): #cl é uma cópia de l
		if cl==[]:
			return lm,lM
		if cl[0]<l[i]:
			return separa(cl[1:],lm+[cl[0]],lM) # se o primeiro elemento for menor que o pivo, acrescenta na lm
		return separa(cl[1:],lm,lM+[cl[0]]) #senão, na lM
	try:
		return separa(l,[],[])
	except IndexError:
		return l,[]

#terceira solução
def pivo(l,i):
	def compara(l2,f):
		if l2==[]:
			return []
		return f(l2[0],l[i])+compara(l2[1:],f)
	try:
		return compara(l,lambda x,y:[x] if x<y else []),compara(l,lambda x,y:[x] if x>=y else [])
	except IndexError:
		return l,[]
		

if __name__=='__main__':
	lm,LM=piv([24,5,787,34,8,95,1,6],4)
	print(lm)
	print(LM)
	print()
	lm1,LM1=menor_maior([24,5,787,34,8,95,1,6],4)
	print(lm1)
	print(LM1)
	print()
	lm2,LM2=pivo([24,5,787,34,8,95,1,6],4)
	print(lm2)
	print(LM2)
