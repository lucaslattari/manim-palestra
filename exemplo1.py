#importamos a manim
from manim import *

#toda animação na manim deve ser uma classe que herda de Scene
class SquareToCircle(Scene):
    #as ações passo a passo a serem realizadas na animação devem estar inseridas
    #dentro de um método construct()
    def construct(self):
        circle = Circle()  #cria um novo objeto círculo
        circle.set_fill(PINK, opacity=0.5)  #define a cor e a transparência
        self.play(Create(circle))  #mostra o círculo na tela
