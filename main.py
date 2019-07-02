from grafo import *
from random import randint

grafo = Grafo()

maximo = 10000
for i in range(maximo):
    # 680 x 576
    index = randint(1,maximo)
    coordenada_atual = (randint(-680, 680), randint(-353, 353))
    grafo.inserir(chave=index, coordenada=coordenada_atual)

print(grafo.mostrar())