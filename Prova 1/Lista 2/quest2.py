"""
escreva um função que receba duas listas numéricas e retorne uma lista com elementos da entrada intercalados
obs.: as listas não precisam ter o mesmo tamanho
"""
def intercala(array1,array2):
	if (not array1) and (not array2):
		return []
	elif not array1:
		return array2
	elif not array2:
		return array1
	else:
		return [array1[0],array2[0]]+ intercala(array1[1:],array2[1:])

if __name__=='__main__':
	print(intercala([1,2,3,4],[5,6,7,8,1]))
