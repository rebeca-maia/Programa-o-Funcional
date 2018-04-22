def quad_perf(n):
	return n**2
	
if __name__=='__main__':
	print([quad_perf(x) for x in list(range(1,100))])
