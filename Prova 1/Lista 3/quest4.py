"""
informe um inteiro n e retorne a aproximação de pi
"""
def aprox_pi(n,s=0,a=3):
	if n==1:
		return 1-(1/3)
	elif n>1:
		if a==((2*n)+1):
			return 1-s
		return aprox_pi(n,s+((1/a)+(((-1)**n)/((2*n)+1))),a+2)
	
		
if __name__=='__main__':
	print((aprox_pi(5)))
