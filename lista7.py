import lista4

#quest1
def is_triang(a,b,c):
	if a<(b+c) and b<(a+c) and c<(b+a):
		return True
	return False

#quest2
def pal(s):
	if s==s[::-1]:
		return True
	return False

#questão 5
def primos(a,b,ra=[],rb=[]):
	if not ra and not rb:
		return primos(a,b,f(a),f(b))
	if max(ra,rb)==1:
		return True
	return False

	
if __name__=='__main__':
	#print(somatorio([i**2 for i in range(1,101)]))
	f=lambda n:[i for i in range(1,n+1) if igual(modulo(n,i),0)] #divisores de um inteiro positivo
	#print(f)
	print(primos(2,3))
	
