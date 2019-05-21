import random
from names import names
from UFs import UFs
from sobrenome import sobrenome

sexo = ["F","M","NB","F","M","F","M","F","M","F","M"]

def txt_funcionario():
	text = open("txtFuncionario.txt","a+")
	for i in range(100):
		text.write("{}|{}|{}|{}|{}|{}|{}\n".format(
			#ID
			i+1,
			#NOME
			names[random.randint(0,999)]+" "+sobrenome[random.randint(0,1063)],
			#Unidade (UF)
			UFs[random.randint(0,26)],
			#Email
			"BD"+str(random.randint(0,10000000))+"@espacial.com",
			#Telefone
			random.randint(10000000,999999999),
			#CPF
			(i+1)*100,
			#Sexo
			sexo[random.randint(0,10)]

		))