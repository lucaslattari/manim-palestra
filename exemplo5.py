from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        #movimenta 2 unidades para a esquerda
        circle.move_to(LEFT * 2)
        #posiciona o quadrado à esquerda do círculo
        square.next_to(circle, LEFT)
        #alinhamento em relação as bordas
        triangle.align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)
