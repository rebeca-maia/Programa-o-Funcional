"""
descobrir se um natural n é primo
"""
def primo(n,div=2):
	if n<=1:
		return False
	elif n==div:
		return True
	if n%div==0 and div<n:
		return False
	else:
		return primo(n,div+1)
	
	
if __name__=='__main__':
	print(primo(3))
		
