from manim import *

class MobjectPlacement(Scene):
    def construct(self):
        #encadeamento também funciona
        circle = Circle().move_to(LEFT * 2)
        square = Square().next_to(circle, LEFT)
        triangle = Triangle().align_to(circle, LEFT)

        self.add(circle, square, triangle)
        self.wait(1)
