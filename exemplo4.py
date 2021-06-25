from manim import *

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT) #movimenta para esquerda
        square.shift(UP) #movimenta para cima
        triangle.shift(RIGHT) #movimenta para direita

        self.add(circle, square, triangle) #adiciona os 3 objs
        self.wait(1) #aguarda 1 segundo
