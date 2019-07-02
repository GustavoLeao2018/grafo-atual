from turtle import *
from time import sleep

class Desenhar:
    def __init__(self):
        self.screen = Screen()
        self.pen = Pen()
        self.pen.shape('turtle')
        

    def desenhar(self, no_atual, e_d=None):
        if e_d == None:
            self.pen.color('yellow')
        if e_d == False: 
            self.pen.color('red')
        if e_d == True: 
            self.pen.color('blue')

        if no_atual is not None:
            self.desenhar(no_atual.esquerda, True)
            # self.pen.penup()
            self.pen.goto(no_atual.valor)
            self.pen.down()
            self.pen.circle(3)
            # self.pen.penup()
            self.pen.forward(5)
            self.pen.down()
            self.pen.color('black')

            texto = f'Chave: {no_atual.chave} Valor: {no_atual.valor}'
            self.pen.write(texto)
            print(texto)
            sleep(1)
            self.desenhar(no_atual.direita, False)
    