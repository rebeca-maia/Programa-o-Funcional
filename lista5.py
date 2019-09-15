def my_len(l):
	if not l:
		return 0
	return 1+my_len(l[1:])	

def divisiveis(l,n,i=0,s=0):
	if i<my_len(l):
		if l[i]%n==0:
			return divisiveis(l,n,i+1,s+l[i])
		return divisiveis(l,n,i+1,s)
	return s

def cifra_cesar(s,alf="ABCDEFGHIJKLMNOPQRSTUVWXYZ",sn="",i=0):
	def busca_indice(s,alf,i=0):
		if s==alf[0]: 
			return i
		return busca_indice(s,alf[1:],i+1)
	if i<my_len(s):
		return cifra_cesar(s,alf,sn+alf[busca_indice(s[i],alf)+3],i+1)
	return sn	
	#	

#Retorna os elementos em comum entre duas listas
def el_comum(la,lb,ln=[],i=0):
	def aux(e,lb,j=0):
		if j<len(lb):
			if e==lb[j]:
				return [e]+aux(e,lb,j+1)
			return aux(e,lb,j+1)
		return []
	if not la or not lb: 
		return ln
	if i<len(la):
		return el_comum(la,lb,ln+aux(la[i],lb),i+1)
	return ln
	
	#
def senhaforte(s,i=0):
	if not s:return
	if type(s[i])==int or (s[i]=="#" or s[i]=="@" or s[i]=="$" or s[i]=="%" or s[i]=="*" or s[i]=="+" or s[i]=="=" or s[i]=="§") or (s[i].islower() or s[i].isupper()) and i<len(s):
		return True
	elif not(type(s[i])==int or (s[i]=="#" or s[i]=="@" or s[i]=="$" or s[i]=="%" or s[i]=="*" or s[i]=="+" or s[i]=="=" or s[i]=="§")) or (s[i].islower() or s[i].isupper()) and i<len(s):
		return senhaforte(s,i+1)
	return False 

def somavetorial(v,w,r=[],i=0):
	if len(v) != len(w):
		return None
	if i<len(v):
		return somavetorial(v,w,r+[v[i-1]+w[i-1]],i+1)
	return tuple(r)	

def product_esc(v,w,r=0,i=0):
	if (not v) or (not w) or (len(v) != len(w)): return None
	def mul(i):
		return v[i]*w[i]
	if i<len(v):
		return product_esc(v,w,r+mul(i),i+1) 
	return r

	
if __name__ == '__main__':
	#print(divisiveis([1,2,3,5,6,12,27],3))
	#print(cifra_cesar("REBECA"))
	print(el_comum([1,2,3,7,9,5],[1,5,8,4,3]))
	#print(senhaforte("1rE3c4#"))
	#print(somavetorial((1,4),(6,2)))
	#print(product_esc((2,4,8),(6,3,7)))
	
