import random
from alimentos import alimentos


def txt_produto():
	text = open("txtProdutos.txt", "a+")
	for i in range(6):
		text.write("{}|{}|{}|{}|{}\n".format(
			#ID
			i+1,
			#Nomes
			alimentos[i],
			#Preço
			random.randint(80,501),
			#Quantidade disponivel
			random.randint(1000,6001),
			#Estoque
			random.randint(12000,15000)
		))
