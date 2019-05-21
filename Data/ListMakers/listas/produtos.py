import random



def preencheProduto():
    produtos= []
    letra = ["Xat","Zeta","Ion","Mecha","Tec","Giga","Deta","Sum","Minus","Beta","Alfa","Omega","Omni","Prism","Vector","Tera","Core","Tick","Top","Quantum"]
    for i in range(100000):
        produtos.append(letra[random.randint(0,19)]+str(random.randint(1000,9999))+("-" if random.randint(0,10) <= 5 else '/')+(str(random.randint(10,99)) if random.randint(0,10) <= 5 else str(random.randint(100,999))))

    return produtos
