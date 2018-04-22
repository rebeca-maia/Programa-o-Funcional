"""
entrada: lista e um booleano informando se a lista será crescente ou decrescente
saída : lista ordenada
"""

def my_len(l):
	if not l:
		return 0
	return 1+my_len(l[1:])	

def ordena(chave,indice,l,temp=0):
	if chave>my_len(l)-1: #se a chave passada for que o ultimo indice da lista, retorna a lista
		return l
	elif l[indice]<=l[chave]:
		return ordena(chave+1,indice+1,l)
	else:
		temp=l[chave]
		l[chave]=l[indice]
		l[indice]=temp
		if indice==0:
			return ordena(chave+1,indice+1,l)
		else: return ordena(chave-1,indice-1,l)
	
		
def tipo_ordena(chave,indice,l,reverso):
	if reverso==True:
		return ordena(chave,indice,l)[::-1]
	else: return ordena(chave,indice,l)
	

if __name__=='__main__':
	print(tipo_ordena(1,0,[0,9,8,7,1,6],False))
