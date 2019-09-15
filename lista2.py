#Funções para lista encadeada
"""6.Tamanho da lista"""
def my_len(t):
	if not t:
		return 0
	return 1+my_len(t[1])
	
"""5.Somatório da Lista"""
def somatorio(t,s=0):
	if t==None:
		return s
	return somatorio(t[1],s+t[0])
	
"""
1.Adicionar(valor)
	fim(append)
	em qualquer posição(insert)
	início(push)
"""
def push_front(v,t):
	return (v,t)

def insert(v,i,t):
	if i==0:
		return (v,t)
	return (t[0],insert(v,i-1,t[1]))
	
def my_append(v,t):
	return insert(v,my_len(t),t)
	
"""
2.Remover(valor)
	fim(pop)
	em qualquer posição(remove)
	início(pop_front)
	remover valor(delete)
"""
def pop_front(t):
	return t[1]

def pop(t):
	if t==None or t[1]==None:
		return None
	return (t[0],pop(t[1]))
	
def remove_(i,t):
	if i==0:
		return t[1]
	return (t[0],remove_(i-1,t[1]))

def delete(v,t):
	if not t:
		return None
	if t[0]==v:
		return delete(v,t[1])
	return (t[0],delete(v,t[1]))
	
"""14.Busca um valor, dado um índice"""
def busca_valor(t1,j,i=0): 
	if i==j:
		return t1[0]
	return busca_valor(t1[1],j,i+1)
		
def transforma(t,k=0,copl=[]):#transforma uma tupla encadeada em uma lista
	return [busca_valor(t,e) for e in list(range(my_len(t)))]
	
"""
3.Ordenar
	crescente
	decrescente
"""	
def my_lenl(l):
	if not l:
		return 0
	return 1+my_lenl(l[1:])	
	
#Insertion-sort	
def ordena(chave,indice,l,temp=0):
	if chave>my_lenl(l)-1: #se a chave passada for que o ultimo indice da lista, retorna a lista
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
	
		
def tipo_ordena(l,reverso,chave=1,indice=0):
	if reverso==True:
		return ordena(chave,indice,l)[::-1]
	else: return ordena(chave,indice,l)
	
"""9. Alterar um valor num índice específico"""
def altera_valor(v,i,t):
	if not t:
		return None
	if i==0:
		return (v,t[1])
	return (t[0],altera_valor(v,i-1,t[1]))

"""15.Inverter Tupla"""	
def inverter(t): 
	if t==None:
		return None
	return (inverter(t[1]),t[0])	

"""10. Concatenar duas listas"""
def concatena(lis1, lis2):
	return tuple(tipo_ordena(lis1+lis2,False))

"""12.Conta o numero de ocorrencias de um valor"""
def conta_ocorrencias(lis,c):
	if my_lenl(lis)==0:
		return 0
	if lis[0]==c:
		return 1+conta_ocorrencias(lis[1:],c)
	return conta_ocorrencias(lis[1:],c)
#Questão 7
def head_tail(t):
	if my_len(t)==0:
		return None
	return t[0],t[1]

#11. Alterar valores da lista,dada uma função
def my_map(lis, func):
	if my_lenl(lis) == 0:
		return []
	return [func(lis[0])] + my_map(lis[1:], func)	
	
#Questão 4
def maximo_minimo(lista):
	if my_lenl(lista)==0:
		return []
	return ordena(1,0,lista)[0], ordena(1,0,lista)[my_lenl(lista)-1]

#Questão 8
def busca_trueorfalse(lista,valor):
	if my_lenl(lista)==0:
		return False
	if lista[0]== valor:
		return True
	return busca_trueorfalse(lista[1:],valor)

#Questão 13
def slice_(l,inicio,fim,passo):
	return tuple(l[inicio:fim:passo])
			
if __name__=='__main__':
	print(my_len((1,(2,(3,(4,(5,None)))))))
	print(push_front(8,(1,(2,(3,(4,(5,None)))))))
	print(insert(6,3,(1,(2,(3,(4,(5,None)))))))
	print(my_append(9,(1,(2,(3,(4,(5,None)))))))
	print(inverter((1,(2,(3,(4,(5,None)))))))
	print(altera_valor(7,2,(1,(2,(3,(4,(5,None)))))))
	print(tuple(transforma((1,(2,(3,(4,(5,None))))))))
	print(tuple(tipo_ordena(transforma((9,(5,(1,(7,(8,None)))))),False)))
	print(concatena(transforma((12,(2,(8,(4,(5,None)))))),transforma((3,(6,(1,(4,(5,None))))))))
	print(conta_ocorrencias(transforma((1,(2,(1,(2,(0,(1,None))))))),1))
	print(head_tail((1,(2,(3,(4,(5,None)))))))
	print(tuple(my_map(transforma((1,(3,(4,(2,(5,(9,(10,None)))))))), lambda x: x**2)))
	print(maximo_minimo(transforma((3,(6,(1,(4,(5,None))))))))
	print(busca_trueorfalse(transforma((1,(3,(4,(2,(5,(9,(10,None)))))))),10))
	print(slice_(transforma((1,(2,(3,(4,(5,None)))))),0,4,1))
