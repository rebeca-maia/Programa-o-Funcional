def filtron(l,f):
	if l==[]:
		return []
	if f(l[0]):
		return [l[0]]+filtron(l[1:],f)
	return filtron(l[1:],f)


"""
escreva uma função que receba uma lista de numeros e um filtro e retorna uma lista com todos os elementos que satisfazem o filtro
"""


if __name__=='__main__':
	print(filtron([3,4,5,6,7,8],lambda x:x%2==0)) #função anônima: útil quando a função será usada apenas uma vez no programa, e tbm nn é complexa
