import random

from produtos import preencheProduto
from nomedeEmpresas import empresas
from listaUF import uf
from pagamento import pagamento
from listaRua import ruas
from tipoEmail import email
from complemento import complemento
from precoUnitario import precoUnitario
from primNome import primNome
from allProductsPreco import preco

#produtos = preencheProduto()
#precoUni = precoUnitario()
#
#def listProd():
#
#    text = open("listaProduto.txt", "w+")
#
#    text.write("_id,modelo,valor_unitario,versao\n\n")
#
#
#
#    for i in range(500000):
#        text.write("{},{},{},{}\n".format(
#            i+1,                                            #id
#            produtos[random.randint(0,99999)],                                    #modelo
#            random.randint(60,1000),                        #valor u
#            str(random.randint(2000,2019))                  #versao
#        ))
#
#
#
#listProd()
#
#def listConta():
#    text = open("listaConta.txt", "w+")
#
#    text.write("cnpj,nome,telefone,email,num_Func,cep,rua,numero,complemento,uf\n") #"complemento"
#
#    for i in range(500000):
#        nomeEmpresa = empresas[random.randint(0,193)]
#        secNomeEmpresa = primNome[random.randint(0,78)]
#        text.write("{},{},{},{},{},{},{},{},{}\n".format(
#            random.randint(10000000000000,99999999999999),        #cnpj
#            nomeEmpresa + ' ' + secNomeEmpresa,                                            #nome
#            random.randint(1000000000,9999999999),                  #telefone
#            (nomeEmpresa + secNomeEmpresa if random.randint(0,10) <= 5 else nomeEmpresa) + email[random.randint(0,5)],               #email
#            str(random.randint(20,500)), #num_func
#            str(random.randint(10000,99999)) + "-" + str(random.randint(100,999)),                         #cep
#            ruas[random.randint(0,599)],                                                #ruas
#            uf[random.randint(0, 26)],
#            random.randint(2,999),                                 #numero
#            complemento[random.randint(0,19)]     #complemento
#
#        ))
#
#listConta()
#
#
def valorT(quantidade, valorU):
    valorTotal = quantidade * valorU
    str(valorTotal)
    return valorTotal

f = open("allCnpjs.txt")
cnpjs = f.read().splitlines()

f = open("allProductsIDs.txt")
prodIds = f.read().splitlines()

def listPedido():

    text = open("listaPedido.txt","w+")

    text.write("cnpj, quantidade, valorT,produtos, pagamento \n")

    for i in range(1000000):  #range( 5000000 )
        quant = random.randint(1, 100)
        indexProd = random.randint(0, 499999)
        text.write("{},{},{},{},{}\n".format(
            cnpjs[random.randint(0,499999)],  # ou i+1
            quant,
            str(valorT(quant, preco[indexProd])),
            prodIds[indexProd],
            pagamento[random.randint(0,3)]
        ))

listPedido()
