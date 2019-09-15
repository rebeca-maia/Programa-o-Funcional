#quest3
def add(e,i,c):
	if type(c)==list: return c[:i]+[e]+c[i:]
	if type(c)==tuple: return c[:i]+ (e,) + c[i:]
	return c[:i]+e+c[i:]

#quest4
def equacao(a,b,c):
	def delta(a,b,c):
		return (b**2)-(4*a*c)
	def baskara(d):
		if d<0:
			return None
		elif d==0:
			return (-b)/(2*a)
		return (-b-(d**0.5))/(2*a) , (-b+(d**0.5))/(2*a)
	return baskara(delta(a,b,c))

#quest2
def perimetro(*v):
	def dist(p1,p2):
		return (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))**0.5
	def aux(t,c=0):
		if (t-1)==c:
			return dist(v[-1],v[0])
		return dist(v[c],v[c+1])+aux(t,(c+1))
	return aux(tam(v))

#quest1
def conta(colecao,e):
	if not colecao:return 0
	if colecao[0]==e:
		return 1+conta(colecao[1:],e)
	return conta(colecao[1:],e)

#quest5
class No:
    def __init__(self, chave, val):
        self._chave = chave
        self._val = val
        self._esq = None
        self._dir = None

    def set_children(self, e, d):
        self._esq = e
        self._dir = d

    def dados(self):
        return self._chave, self._val

    def filho_esq(self):
        return self._esq

    def filho_dir(self):
        return self._dir
        
        
class BinarySearchTree:
    def __init__(self):
        self.raiz = None

    def insert(self, chave, val):
        self.raiz = self.__insert(self.raiz, chave, val)

    def __insert(self, v, chave, val):
        if v:
            v_chave, x = v.dados() # Ignoring x actually
            esq = v.filho_esq()
            dire = v.filho_dir()
            if chave < v_chave:
                esq = self.__insert(esq, chave, val)
            else:
                dire = self.__insert(dire, chave, val)
            v.set_children(esq,dire)
            return v
        else:
            return No(chave, val)        
        
    # #   		
if __name__=='__main__':
	#print(add("1",3,"134567"))
	#print(equacao(1,-3,2))
	#print(conta("ARARA","A"))
	
    
