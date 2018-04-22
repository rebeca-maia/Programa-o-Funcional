"""
entrada: duas listas de inteiros
retorno: maior elemento das duas listas
"""
def my_len(l):
	if not l:
		return 0
	return 1+my_len(l[1:])
	
def ordena(chave,indice,l,temp=0):
	if chave>my_len(l)-1: 
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

def maior(r,s):
	if my_len(r)==1 and my_len(s)==0:
		return r[0]
	elif my_len(s)==1 and my_len(r)==0:
		return s[0]
	elif my_len(r)>1 and my_len(s)==0:
		return ordena(1,0,r)[my_len(r)-1]
	elif my_len(s)>1 and my_len(r)==0:
		return ordena(1,0,s)[my_len(s)-1]
	else:
		if ordena(1,0,r)[my_len(r)-1]> ordena(1,0,s)[my_len(s)-1]:
			return ordena(1,0,r)[my_len(r)-1]
		else:
			return ordena(1,0,s)[my_len(s)-1]

if __name__=='__main__':
	print(maior([1,5,7,8],[4,6,7,10,1]))
	
		
