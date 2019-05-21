import random

def precoUnitario():
    precoUni = []
    for i in range(1000):
        precoUni.append(random.randint(20,50))
    return precoUni

precoUnitario()