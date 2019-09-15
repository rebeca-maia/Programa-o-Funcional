
class Fibonacci():                                                                                  
	def __init__(self):
		self.seq = [0, 1]
       #   
	def __iter__(self):
		return self
	                                                                              
	def next(self):
		self.seq.append(sum(self.seq))
		del self.seq[0]
		return self.seq[-1] #acessando ultimo elemento da lista
                                                                                          

"""
2.Crie um gerador count(start=1,step=1). Exemplo: count(10)-> 10,11,12...
"""
class Count():
	def __init__(self, valor, passo = 1):
		self.valor = valor - passo
		self.passo = passo

	def __iter__(self):
		return self

	def next(self):
		self.valor += self.passo
		return self.valor

"""
3.Crie o gerador ciclo(coleção). Ex.: ciclo('ABCD') -> A B C D A B C...
"""	
class Ciclo():
	def __init__(self, colecao):
		try:
			_ = (x for x in colecao)
		except TypeError as e:
			raise e
		else:
			self.colecao = colecao
			self.indice = -1

	def __iter__(self):
		return self

	def next(self):
		if self.indice < len(self.colecao)-1:
			self.indice += 1
			return self.colecao[self.indice]
		else:
			self.indice = 0
			if len(self.colecao) > 0:
				return self.colecao[self.indice]
			else:
				raise StopIteration
				
"""
4. Crie o iterador repetir(n,i).Ex.: repetir(10,3)-> 10 10 10
"""
class Repeat():

	def __init__(self, objeto, max = None):
		self.objeto = objeto

		if max is not None:
			self.qtd = max
			self.limite = True	#Possui um limite
		else:
			self.limite = False	#Não possui um limite

	def __iter__(self):
		return self

	def next(self):
		if self.limite == True:
			if self.qtd > 0:
				self.qtd -= 1
				return self.objeto
			else:
				raise StopIteration
		else:
			return self.objeto

"""
	5.Executa uma função sobre dois elementos da lista por vez
"""
class Accumulate():
	def __init__(self, colecao, funcao = lambda x, y: x + y):
		try:
			_ = (x for x in colecao)
			_ = funcao(1,1)
		except Exception as e:
			raise e
		else:
			self.colecao = colecao
			self.funcao = funcao
			self.indice = -1
			self.ult_val = None

	def __iter__(self):
		return self

	def next(self):
		if self.indice < len(self.colecao) - 1 and len(self.colecao) > 0:
			self.indice += 1
			if self.ult_val == None:
				self.ult_val = self.colecao[self.indice]
				return self.ult_val
			else:
				self.ult_val = self.funcao(self.ult_val, self.colecao[self.indice])
				return self.ult_val
		else:
			raise StopIteration
"""
6.Crie o iterador chain(s1,s2,s3,...). Ex.: chain('ABCD','EFGH') ->A B C D E F G H
"""
class Chain():
	def __init__(self, *colecoes):
		self.indice = -1
		self.ind_lis_atual = 0
		self.colecoes = colecoes
		self.lista_atual = None

	def __iter__(self):
		return self

	def next(self):
		if len(self.colecoes) > 0 and self.ind_lis_atual < len(self.colecoes):
			if self.indice < len(self.colecoes[self.ind_lis_atual])-1:
				self.indice += 1
				return self.colecoes[self.ind_lis_atual][self.indice]
			else:
				self.indice = 0
				self.ind_lis_atual += 1 #proxima lista

				if self.ind_lis_atual is not len(self.colecoes):
					#verificando se a proxima existe
					return self.colecoes[self.ind_lis_atual][self.indice]
				else:
					raise StopIteration
		else:
			raise StopIteration

if __name__ == '__main__':
	#k = Count(50,1)
	#k = Ciclo('REBECA')
	#k = Repeat(10,10)
	#k = Accumulate([1,2,3,4,5,6,7,8,9,10])
	#k = Chain([1,2,3,4],"funcio")
	fib = Fibonacci()
	
	for i in range(10):
		print(fib.next())
	
	
	for i in range(10):
		print(k.next())
	
