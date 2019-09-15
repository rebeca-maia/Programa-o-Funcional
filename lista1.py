def my_len(t): #item d
	if not t:
		return 0
	return 1+my_len(t[1])
	
def somatorio(t,s=0): #item a
	if t==None:
		return s
	return somatorio(t[1],s+t[0])


	
if __name__=='__main__':
	#print(my_len((1,(2,(3,(4,(5,None)))))))
	print(somatorio((1,(2,(3,(4,(5,None)))))))

