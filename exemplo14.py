from manim import *
class MathematicalEquation(Scene):
    def construct(self):

        # Write equations
        equation1 = MathTex("2x^2-5x+2")
        eq_sign_1 = MathTex("=")
        equation2 = MathTex("2x^2-4x-x+2")
        eq_sign_2 = MathTex("=")
        equation3 = MathTex("(x-2)(2x-1)")

        #posiciona as equações entre o sinal de =
        equation1.next_to(eq_sign_1, LEFT)
        equation2.next_to(eq_sign_1, RIGHT)

        #posiciona segunda equação abaixo da 1 equação
        eq_sign_2.shift(DOWN)
        equation3.shift(DOWN)

        #alinha segunda equação abaixo da 1 equação
        eq_sign_2.align_to(eq_sign_1, LEFT)
        equation3.align_to(equation2, LEFT)

        #agrupa equações
        eq_group = VGroup(equation1, eq_sign_1, equation2, eq_sign_2, equation3)

        self.play(Write(eq_group))
        self.wait()
