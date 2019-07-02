from random import *

class No:
    def __init__(self, chave, valor):
        self.esquerda = None
        self.chave = chave
        self.valor = valor
        self.direita = None

    def __repr__(self):
        return f"""({self.esquerda}, {self.valor}, {self.direita})"""
