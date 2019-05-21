import random
from names import names

def txt_vendas():
	text = open("txtVendasMongo","a+")
	text.write("id,produto,quantidade,preco,data,id_funcionario,id_empresa,responsavel_compra\n")
	for i in range(10000000):
		quantidade = random.randint(500,5000)
		produto = random.randint(1,6)
		preco = 0
		if produto == 1:
			preco = quantidade*457
		elif produto == 2:
			preco = quantidade*494
		elif produto == 3:
			preco = quantidade*179
		elif produto == 4:
			preco = quantidade*117
		elif produto == 5:
			preco = quantidade*337
		elif produto == 6:
			preco = quantidade*192

		text.write("{},{},{},{},{},{},{},{}\n".format(
			#ID
			i+1,
			#Produto
			produto,
			#Quantidade
			quantidade,
			#Preço
			preco,
			#data
			str(random.randint(1,28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(2000,2019)),
			#id Funcionario
			random.randint(1,100),
			#id empresa
			random.randint(1,1000),
			#Responsavel compra
			names[random.randint(0,999)]

		))
