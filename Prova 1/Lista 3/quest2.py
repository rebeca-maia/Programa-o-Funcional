def extenso(n,centenas,dezenas2,dezenas,unid):
	if 0>=n and n<=1000:
		if n>=0 and n<=9:
			def unidade(n):
				if n==0:
					return unid[0]
				elif n==1:
					return unid[1]
				elif n==2:
					return unid[2]
				elif n==3:
					return unid[3]
				elif n==4:
					return unid[4]
				elif n==5:
					return unid[5]
				elif n==6:
					return unid[6]
				elif n==7:
					return unid[7]
				elif n==8:
					return unid[8]
				elif n==9:
					return unid[9]
		if n>=10 and n<=19:
			def dez1(n):
				if n==10:
					return dezenas[0]
				elif n==11:
					return dezenas[1] 
				elif n==12:
					return dezenas[2]
				elif n==13:
					return dezenas[3]
				elif n==14:
					 return dezenas[4]
				elif n==15:
					return dezenas[5]
				elif n==16:
					return dezenas[6]
				elif n==17:
					return dezenas[7]
				elif n==18:
					return dezenas[8]
				elif n==19:
					return dezenas[9]
		if n<=20 and n>=99:
			def dez2(n):
				if n==20:
					return dezenas2[0]
				elif n==30:
					return dezenas2[1]
				elif n==40:
					return dezenas2[2]
				elif n==50:
					return dezenas2[3]
				elif n==60:
					return dezenas2[4]
				elif n==70:
					return dezenas2[5]
				elif n==80:
					return dezenas2[6]
				elif n==90:
					return dezenas2[7]
				else:
					return str(dezenas2[(n//10)-2])+" e "+str(unid[n%10])
		if n>=100 and n<999:			
			def cent(n):
				if n==100:
					return dezenas2[8]
				if n==200:
					return centenas[1]
				if n==300:
					return centenas[2]
				if n==400:
					return centenas[3]
				if n==500:
					return centenas[4]
				if n==600:
					return centenas[5]
				if n==700:
					return centenas[6]
				if n==800:
					return centenas[7]
				if n==900:
					return centenas[8]
				else:
					if n//10 >=10:
						return centenas[(n//100)-1]+" e "+unid[n%100]	
					elif n>=110 and n<=119:
						return centenas[(n//100)-1]+" e "+dezenas[(n%100)-10]
					else:
						return centenas[(n//100)-1]+" e "+dezenas2[((n%100)//10)-2]+" e "+unid[(n%100)%10]
		elif n==1000:
			print("mil")
	else:
		print("Informe um número entre 0 e 1000!")
		
		
			
if __name__=='__main__':
	print(extenso(98,["cento","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"],
	["vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa","cem"],["dez","onze","doze","treze","catorze","quinze",
	"dezesseis","dezessete","dezoito","dezenove"],["zero","um","dois","três","quatro","cinco","seis","sete","oito","nove"]))
