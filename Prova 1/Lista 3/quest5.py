"""
gere os n primeiros quadrados perfeitos
"""
def gerar_n_quad_perf(limite,s=0,i=1):
	def quad_perf(n):
		return n**2
	if limite==0:
		return []
	return gerar_n_quad_perf(limite-1)+[quad_perf(limite)][::-1]

if __name__=='__main__':
	print(gerar_n_quad_perf(6))
