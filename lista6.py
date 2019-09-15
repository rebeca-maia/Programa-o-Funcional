import math

class Vetor:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
	
	def modulo(self):
		return math.sqrt((self.x**2)+(self.y**2)+(self.z**2))
	
	def mult_escalar(self,esc):
		 return (self.x*esc,self.y*esc,self.z*esc)
		
	def soma_vetor(self,v2):
		return (self.x+v2[0],self.y+v2[1],self.z+v2[2])
		
	def produto_escalar(self,v2):
		return self.x*v2[0]+self.y*v2[1]+self.z*v2[2]

	def exibir(self):
		print("("+str(self.x)+", "+str(self.y)+", "+str(self.z)+")")
		
	
class Matriz:
	def __init__(self,els):
		self.els=els
	
	
	def getN_Linhas(self,i=0):
		if i<len(self.els):
			return self.getN_Linhas(i+1)
		return i
	
	def getN_Colunas(self,j=0):
		return len(self.els[0])
	
	def busca_el(self,i,j):
		return self.els[i-1][j-1]
	
	
	def mult_esc(self,s,r=[],r2=[],i=0,j=0):
		if i<self.getN_Linhas():
			if j<self.getN_Colunas():
				return self.mult_esc(s,r+[self.els[i][j]*s],r2,i,j+1)
			else:
				return self.mult_esc(s,[],r2+[r],i+1,0)
			return self.mult_esc(s,[]+[r],i+1,j)
		else:
			return r2		
	
	def mult_matrix(self,m2,r=[],i=0,j=0,val=0,k=0):
		if len(m2) == self.getN_Colunas():
			if i<self.getN_Linhas():
				return self.mult_matrix(m2,r.append([]),i,j,val,k)
				if j<len(m2[i]):
					if k<self.getN_Linhas():
						return self.mult_matrix(m2,r,i,j,val + self.els[i][k]*m2[k][j],k+1)
					return self.mult_matrix(m2,r[i].append(val),i,j+1,val,k)
				return self.mult_matrix(m2,r,i+1,j,val,k)
			return r
					
    
	def transposta(self,r=[],r2=[],i=0,j=0):
		if i<self.getN_Linhas():
			if j<self.getN_Colunas():
				return self.transposta(r+[self.els[i][j]],r2,i+1,j)
			else:
				return r2
		else:
			return self.transposta([],r2+[r],0,j+1)

		
if __name__=='__main__':
	c=Vetor(3,8,2)
	"""print(c.mult_escalar(4))
	print(c.soma_vetor((1,2,3))
	print(c.produto_escalar((14,2,9)))
	c.exibir()
	"""
	m=Matriz([[3,2,7],[6,5,4],[0,4,9]])
	#print(m.getN_Linhas())
	#print(m.getN_Colunas())
	#print(m.busca_el(1,3))
	#print(m.mult_esc(2))
	#print(m.mult_matrix([0,0,2],[1,2,1],[1,0,3]))
	print(m.transposta())
