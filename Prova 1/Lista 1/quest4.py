"""
escreva uma função que receba duas listas e retorne uma lista de tuplas com os elementos de ambas as listas de entrada que tenham o mesmo
índice. Complete com um caractere - caso as listas tenham tamanhos diferentes.
"""
def combina(l1,l2):
	def my_len(l):
		if not l:
			return 0
		return 1+my_len(l[1:])
	def func2(la,lb):
		if la==[] and lb==[]:
			return [] 
		elif my_len(la) ==0:
			return [('-',lb[0])]+func2([],lb[1:])
		elif my_len(lb)==0:
			return [(la[0],'-')]+func2(la[1:],[])
		else:
			return [(la[0],lb[0])]+func2(la[1:],lb[1:])
	return func2(l1,l2)

if __name__=='__main__':
	print(combina([1,2,4,5,6,3,8],[5,7,8,4,9]))
	
