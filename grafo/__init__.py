from no import *
from desenhar import *

class Grafo:
    def __init__(self):
        self.no_raiz = None

    def inserir(self, chave, coordenada):
        if self.no_raiz is None:
            self.no_raiz = No(chave=chave, valor=coordenada)
        else:
            self._inserir(chave=chave, valor=coordenada, no_atual=self.no_raiz)

    def _inserir(self, chave, valor, no_atual):
        if chave < no_atual.chave:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(chave=chave, valor=valor)
            else:
                self._inserir(chave=chave, valor=valor, no_atual=no_atual.esquerda)
        elif chave > no_atual.chave:
            if no_atual.direita is None:
                no_atual.direita = No(chave=chave, valor=valor)
            else:
                self._inserir(chave=chave, valor=valor, no_atual=no_atual.direita)

    def mostrar(self):
        desenhar = Desenhar()
        desenhar.desenhar(self.no_raiz)

        return f"Raíz -> {self.no_raiz.valor} \nGrafo: \n\t{self.no_raiz}"

        