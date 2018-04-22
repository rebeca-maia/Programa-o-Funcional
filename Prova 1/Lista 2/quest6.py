"""
produto cartesiano da lista1 com a lista2
"""
def prod_cart(l1,l2):
	def aux(la,lb):
		if not la:
			return []
		if not lb:
			return aux(la[1:],l2) #consumindo la
		return [(la[0],lb[0])]+aux(la,lb[1:]) #consumindo lb
	return aux(l1,l2)

if __name__=='__main__':
	print(prod_cart([1,2,3,4],[5,6,7,8]))
