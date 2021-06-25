from manim import *

class MobjectOrder(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        #adiciona borda verde de largura 20
        circle.set_stroke(color=GREEN, width=20)
        #adiciona preenchimento amarelo sem transparência
        square.set_fill(YELLOW, opacity=1.0)
        #adiciona preenchimento rosa 50% transparente
        triangle.set_fill(PINK, opacity=0.5)

        self.add(triangle, square, circle)
        self.wait(1)
