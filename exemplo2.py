from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()  #cria um quadrado
        square.flip(RIGHT)  #espelha objeto para a direita
        square.rotate(30 * DEGREES)  #rotaciona 30 graus

        self.play(Create(square))  #anima a criação do quadrado
        self.play(Transform(square, circle))  #transforma o quadrado em círculo (interpolação)
        self.play(FadeOut(square))  #faz o objeto desaparecer
