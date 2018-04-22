#retorna a n-ésima linha do triângulo de pascal
def pascal(n,k=0):
	def fat(x):
		if not x:
			return []
		return x*fat(x-1)
	def combina(n,k):
		#print(fat(n))
		return fat(n)/(fat(k)*fat(n-k))
	if k>n-1:
		return []
	return combina(n,k)+pascal(n,k+1)
	 
		
	
if __name__=='__main__':
	r=pascal(2)
	print(r)
	
