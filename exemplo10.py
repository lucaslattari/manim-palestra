from manim import *

class ApplyMethodExample(Scene):
    def construct(self):
        square = Square().set_fill(RED, opacity=1.0)
        self.add(square)

        #anima mudando a cor de preenchimento
        self.play(square.animate.set_fill(WHITE))
        self.wait(1)

        #anima movimentando o objeto
        self.play(square.animate.shift(UP))
        self.wait(1)
