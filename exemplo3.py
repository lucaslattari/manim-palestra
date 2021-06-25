from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle) #adiciona círculo sem animação
        self.wait(1) #aguarda 1 segundo
        self.remove(circle) #remove círculo
        self.wait(1) #aguarda 1 segundo antes de encerrar

        
