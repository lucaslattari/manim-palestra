from manim import *

class SomeAnimations(Scene):
    def construct(self):
        square = Square()
        self.add(square)

        #objeto aparecendo
        self.play(FadeIn(square))

        #objeto rotacionando
        self.play(Rotate(square, PI/4))

        #objeto sendo removido
        self.play(FadeOut(square))

        self.wait(1)

        
