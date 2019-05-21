import random

from sobrenome import sobrenome
from names import names
from emails import emails
from UFs import UFs

corps = [" Corporation", " S/A"]
torre = ["","Torre 1", "Torre 2","Torre 3","Torre 4","Torre 5"]
andar = [	"1°",	"2°",	"3°",	"4°",	"5°",	"6°",	"7°",	"8°",	"9°",	"10°"]
def txt_empresa():
	text = open("txtEmpresa.txt", "a+")
	for i in range(1000):
		text.write("{}|{}|{}|{}|{}|{}|{}|{}|{}|{}\n".format(
			#ID
			i+1,
			#Nome Empresa
			sobrenome[i]+corps[random.randint(0,1)],
			#Email Empresa
			sobrenome[i]+emails[random.randint(0,3)],
			#Telefone
			random.randint(1000000000,9999999999),
			#CNPJ
			random.randint(10000000000000,99999999999999),
			#CEP
			random.randint(10000000,99999999),
			#Numero
			random.randint(1,9000),
			#UF
			UFs[random.randint(0,26)],
			#Complemento
			andar[random.randint(0,9)]+" andar - "+torre[random.randint(0,5)],
			#Responsavel Receptor
			names[i]
		))