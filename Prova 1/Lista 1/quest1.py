"""
escreva uma função que receba uma lista ou tupla e retorne a soma de todos os números
"""
def soma(l):
	if l==() or l==[]:
		return 0
	try:
		return l[0]+0+soma(l[1:])
	except TypeError:
		return soma(l[1:])

r=soma(l=[3,6,4,7,9])
print(r)
