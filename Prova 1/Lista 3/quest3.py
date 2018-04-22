#criptografa uma string a partir de uma chave
def my_len(l):
		if not l:
			return 0
		return 1+my_len(l[1:])	
		
def cripto(fr,chave,d={}):
	def quebra(chave):
		return [chave[:my_len(chave)//2]],[chave[(my_len(chave)//2)+1:]]
	def montar_dict(li,lj,d={}):
		if my_len(li)==0:
			return d
		else:
			d[""+li[0]+""]=""+lj[0]+""
			d[""+lj[0]+""]=""+li[0]+""
			return montar_dict(li[1:],lj[1:],d)
	if my_len(fr)==0:
		return ""
	else:
		d=montar_dict(quebra(chave)[0][0],quebra(chave)[1][0])
		try:
			return ""+d[fr[0]]+""+cripto(fr[1:],chave)
		except KeyError:
			return fr[0]+cripto(fr[1:],chave)
		
if __name__=='__main__':
	print(cripto("SAPATO","TENIS/POLAR"))
