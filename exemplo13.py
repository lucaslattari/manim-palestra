from manim import *

class MovingFrame(Scene):
     def construct(self):
        #escreve a equação
        equation = MathTex("2x^2-5x+2", "=", "(x-2)(2x-1)")

        self.play(Write(equation)) #cria a equação

        #adiciona retângulos
        framebox1 = SurroundingRectangle(equation[0], buff=.1)
        framebox2 = SurroundingRectangle(equation[2], buff=.1)

        self.play(Create(framebox1))  #cria o retângulo

        self.wait() #espera 1 segundo
        #movimentação do retângulo entre as equações
        self.play(ReplacementTransform(framebox1, framebox2))
