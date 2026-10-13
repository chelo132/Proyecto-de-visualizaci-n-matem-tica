"""
Proyecto: Plano Tangente y Aproximación Lineal
Asignatura: Cálculo Avanzado — Lista N.º 6
Función: f(x, y) = xy²
Punto: (a, b) = (2, 1)
Valor a aproximar: f(1.98, 1.03)
"""

from manim import *
import numpy as np


# ── Configuración global ─────────────────────────────────────────────────────
config.background_color = "#0f0f1a"


# ── Función y constantes ──────────────────────────────────────────────────────
def f(x, y):
    """Función asignada: f(x, y) = xy²"""
    return x * y**2


def L(x, y):
    """Aproximación lineal: L(x, y) = x + 4y - 4"""
    return x + 4 * y - 4


A, B   = 2.0, 1.0      # Punto de tangencia
FAB    = f(A, B)       # f(2, 1) = 2
X0, Y0 = 1.98, 1.03   # Punto a aproximar
FX_AB  = 1.0           # fx(2, 1) = 1
FY_AB  = 4.0           # fy(2, 1) = 4


# ── Helper: encabezado reutilizable ──────────────────────────────────────────
def crear_encabezado(escena, texto, color=TEAL):
    """Dibuja título + línea separadora y los retorna como (titulo, sep)."""
    titulo = Text(texto, font_size=38, color=color)
    titulo.to_edge(UP, buff=0.4)
    sep = Line(LEFT * 6.2, RIGHT * 6.2, color=color, stroke_width=1)
    sep.next_to(titulo, DOWN, buff=0.15)
    escena.play(Write(titulo), run_time=0.8)
    escena.play(Create(sep), run_time=0.4)
    return titulo, sep


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 0 — Introducción al problema
# ════════════════════════════════════════════════════════════════════════════
class Escena00Introduccion(Scene):
    """
    Presenta el problema: función asignada, punto de tangencia
    y la pregunta central que guía el video.
    """

    def construct(self):
        # ── Título principal ──────────────────────────────────────────────
        titulo = Text("Plano Tangente", font_size=52, color=TEAL)
        subtitulo = Text("y Aproximación Lineal", font_size=38, color=TEAL_B)
        titulo.to_edge(UP, buff=0.45)
        subtitulo.next_to(titulo, DOWN, buff=0.2)

        self.play(Write(titulo), run_time=1.2)
        self.play(Write(subtitulo), run_time=0.8)
        self.wait(0.4)

        sep = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=1.5)
        sep.next_to(subtitulo, DOWN, buff=0.3)
        self.play(Create(sep))

        # ── Fila 1: Función ───────────────────────────────────────────────
        label_func = Text("Función asignada:", font_size=26, color=GRAY_B)
        func_tex   = MathTex(r"f(x,\,y) = xy^2", font_size=40, color=WHITE)
        fila1 = VGroup(label_func, func_tex).arrange(RIGHT, buff=0.35)
        fila1.next_to(sep, DOWN, buff=0.55)

        self.play(FadeIn(label_func), Write(func_tex))
        self.wait(0.4)

        # ── Fila 2: Punto ────────────────────────────────────────────────
        label_pto = Text("Punto de tangencia:", font_size=26, color=GRAY_B)
        pto_tex   = MathTex(r"(a,\,b) = (2,\,1)", font_size=40, color=YELLOW)
        fila2 = VGroup(label_pto, pto_tex).arrange(RIGHT, buff=0.35)
        fila2.next_to(fila1, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_pto), Write(pto_tex))
        self.wait(0.4)

        # ── Fila 3: Valor a aproximar ────────────────────────────────────
        label_apr = Text("Valor a aproximar:", font_size=26, color=GRAY_B)
        apr_tex   = MathTex(r"f(1.98,\;1.03) = \;?", font_size=40, color=GREEN_B)
        fila3 = VGroup(label_apr, apr_tex).arrange(RIGHT, buff=0.35)
        fila3.next_to(fila2, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_apr), Write(apr_tex))
        self.wait(0.5)

        # ── Pregunta central ─────────────────────────────────────────────
        pregunta = Text(
            "¿Cómo podemos usar el plano tangente para aproximar\n"
            "el valor de una función cerca de un punto conocido?",
            font_size=25,
            color=BLUE_B,
            line_spacing=1.35,
        )
        pregunta.to_edge(DOWN, buff=0.55)
        caja = SurroundingRectangle(pregunta, color=BLUE_B, buff=0.22, corner_radius=0.12)

        self.play(Write(pregunta), Create(caja), run_time=1.5)
        self.wait(3)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 1 — Función y superficie 3D
# ════════════════════════════════════════════════════════════════════════════
class Escena01Superficie(ThreeDScene):
    """
    Presenta la función f(x,y)=xy² en 3D y marca el punto P=(2,1,2).
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        ejes = ThreeDAxes(
            x_range=[0, 4, 1],
            y_range=[-1, 3, 1],
            z_range=[-1, 6, 1],
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        superficie = Surface(
            lambda u, v: np.array([u, v, f(u, v)]),
            u_range=[0.5, 3.5],
            v_range=[-0.5, 2.5],
            resolution=(30, 30),
        )
        superficie.set_style(fill_opacity=0.75, stroke_opacity=0.2)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL, GREEN_B])

        punto_P = Sphere(radius=0.1, color=RED).move_to(np.array([A, B, FAB]))

        # Etiqueta fija en pantalla
        etiqueta = MathTex(r"f(x,y) = xy^2", font_size=36, color=WHITE)
        self.add_fixed_in_frame_mobjects(etiqueta)
        etiqueta.to_corner(UL, buff=0.4)

        self.play(Create(ejes), Write(labels), run_time=1.2)
        self.play(Write(etiqueta))
        self.play(Create(superficie), run_time=2)
        self.play(FadeIn(punto_P))
        self.begin_ambient_camera_rotation(rate=0.08)
        self.wait(4)
        self.stop_ambient_camera_rotation()


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 2 — Derivadas parciales
# ════════════════════════════════════════════════════════════════════════════
class Escena02Derivadas(Scene):
    """
    Calcula fx y fy paso a paso y muestra su interpretación geométrica.
    """

    def construct(self):
        titulo, sep = crear_encabezado(self, "Derivadas parciales")

        # ── Función de partida ────────────────────────────────────────────
        func_tex = MathTex(r"f(x,y) = xy^2", font_size=42)
        func_tex.next_to(sep, DOWN, buff=0.45)
        self.play(Write(func_tex))
        self.wait(0.6)

        # ── Derivada en x ─────────────────────────────────────────────────
        label_x = Text("Derivada parcial en x:", font_size=26, color=BLUE_B)
        label_x.next_to(func_tex, DOWN, buff=0.5).to_edge(LEFT, buff=0.6)

        fx_calc = MathTex(
            r"f_x(x,y) = \frac{\partial}{\partial x}(xy^2) = y^2",
            font_size=34,
        ).next_to(label_x, DOWN, buff=0.18).shift(RIGHT * 0.5)

        fx_eval = MathTex(r"f_x(2,\,1) = 1^2 = ", r"1", font_size=36)
        fx_eval[1].set_color(YELLOW)
        fx_eval.next_to(fx_calc, DOWN, buff=0.18).align_to(fx_calc, LEFT)

        self.play(FadeIn(label_x))
        self.play(Write(fx_calc))
        self.play(Write(fx_eval))
        self.wait(0.5)

        # ── Derivada en y ─────────────────────────────────────────────────
        label_y = Text("Derivada parcial en y:", font_size=26, color=GREEN_B)
        label_y.next_to(fx_eval, DOWN, buff=0.45).to_edge(LEFT, buff=0.6)

        fy_calc = MathTex(
            r"f_y(x,y) = \frac{\partial}{\partial y}(xy^2) = 2xy",
            font_size=34,
        ).next_to(label_y, DOWN, buff=0.18).shift(RIGHT * 0.5)

        fy_eval = MathTex(r"f_y(2,\,1) = 2(2)(1) = ", r"4", font_size=36)
        fy_eval[1].set_color(YELLOW)
        fy_eval.next_to(fy_calc, DOWN, buff=0.18).align_to(fy_calc, LEFT)

        self.play(FadeIn(label_y))
        self.play(Write(fy_calc))
        self.play(Write(fy_eval))
        self.wait(0.7)

        # ── Resumen final ─────────────────────────────────────────────────
        # Quitamos todo excepto título y separador
        self.play(
            FadeOut(func_tex),
            FadeOut(label_x), FadeOut(fx_calc), FadeOut(fx_eval),
            FadeOut(label_y), FadeOut(fy_calc), FadeOut(fy_eval),
        )

        r1 = MathTex(r"f_x(2,1) = ", r"1", font_size=46)
        r1[1].set_color(YELLOW)
        r2 = MathTex(r"f_y(2,1) = ", r"4", font_size=46)
        r2[1].set_color(YELLOW)

        resumen = VGroup(r1, r2).arrange(RIGHT, buff=1.5)
        resumen.next_to(sep, DOWN, buff=1.0).center()

        interpretacion = Text(
            "La superficie sube 1 unidad en dirección x\n"
            "y 4 unidades en dirección y, cerca de P = (2, 1, 2).",
            font_size=26,
            color=GRAY_B,
            line_spacing=1.4,
        ).next_to(resumen, DOWN, buff=0.6)

        self.play(Write(r1), Write(r2))
        self.wait(0.4)
        self.play(FadeIn(interpretacion, shift=UP * 0.2))
        self.wait(3)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 3 — Plano tangente 3D
# ════════════════════════════════════════════════════════════════════════════
class Escena03PlanoTangente(ThreeDScene):
    """
    Muestra la superficie, el punto P y el plano tangente animados en 3D.
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        ejes = ThreeDAxes(
            x_range=[0, 4, 1],
            y_range=[-1, 3, 1],
            z_range=[-1, 6, 1],
        )

        superficie = Surface(
            lambda u, v: np.array([u, v, f(u, v)]),
            u_range=[0.5, 3.5],
            v_range=[-0.5, 2.5],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.65, stroke_opacity=0.15)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL, GREEN_B])

        plano = Surface(
            lambda u, v: np.array([u, v, L(u, v)]),
            u_range=[0.5, 3.5],
            v_range=[-0.5, 2.5],
            resolution=(10, 10),
        )
        plano.set_style(fill_opacity=0.45, stroke_opacity=0.25)
        plano.set_color(ORANGE)

        punto_P = Sphere(radius=0.1, color=RED).move_to(np.array([A, B, FAB]))

        # Etiqueta fija del plano tangente
        ecuacion = MathTex(r"z = x + 4y - 4", font_size=32, color=ORANGE)
        self.add_fixed_in_frame_mobjects(ecuacion)
        ecuacion.to_corner(UR, buff=0.4)

        self.play(Create(ejes), run_time=1)
        self.play(Create(superficie), run_time=2)
        self.play(FadeIn(punto_P))
        self.wait(0.5)
        self.play(Create(plano), Write(ecuacion), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.07)
        self.wait(5)
        self.stop_ambient_camera_rotation()


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 4 — Aproximación lineal
# ════════════════════════════════════════════════════════════════════════════
class Escena04Aproximacion(Scene):
    """
    Construye L(x,y) a partir del plano tangente paso a paso.
    """

    def construct(self):
        titulo, sep = crear_encabezado(self, "Aproximación lineal")

        # Fórmula general
        general = MathTex(
            r"L(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)",
            font_size=32,
        ).next_to(sep, DOWN, buff=0.5)

        # Sustitución de valores
        sustit = MathTex(
            r"L(x,y) = 2 + 1\cdot(x-2) + 4\cdot(y-1)",
            font_size=34,
        ).next_to(general, DOWN, buff=0.5)

        # Simplificada
        simple = MathTex(
            r"L(x,y) = x + 4y - 4",
            font_size=46,
            color=YELLOW,
        ).next_to(sustit, DOWN, buff=0.6)
        caja = SurroundingRectangle(simple, color=YELLOW, buff=0.2, corner_radius=0.1)

        self.play(Write(general))
        self.wait(0.8)
        self.play(Write(sustit))
        self.wait(0.8)
        self.play(Write(simple), Create(caja))
        self.wait(3)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 5 — Estimación y análisis del error
# ════════════════════════════════════════════════════════════════════════════
class Escena05EstimacionError(Scene):
    """
    Calcula L(1.98, 1.03), el valor real f(1.98, 1.03) y el error absoluto.
    """

    def construct(self):
        titulo, sep = crear_encabezado(self, "Estimación y error")

        # Aproximación
        aprox_label = Text("Aproximación lineal:", font_size=26, color=YELLOW)
        aprox_label.next_to(sep, DOWN, buff=0.5).to_edge(LEFT, buff=0.6)

        aprox = MathTex(
            r"L(1.98,\;1.03) = 1.98 + 4(1.03) - 4 = ", r"2.10",
            font_size=36,
        ).next_to(aprox_label, DOWN, buff=0.2).shift(RIGHT * 0.4)
        aprox[1].set_color(YELLOW)

        # Valor real
        real_label = Text("Valor real:", font_size=26, color=GREEN_B)
        real_label.next_to(aprox, DOWN, buff=0.45).to_edge(LEFT, buff=0.6)

        real = MathTex(
            r"f(1.98,\;1.03) = 1.98 \cdot (1.03)^2 \approx ", r"2.100582",
            font_size=36,
        ).next_to(real_label, DOWN, buff=0.2).shift(RIGHT * 0.4)
        real[1].set_color(GREEN_B)

        # Error
        error_label = Text("Error absoluto:", font_size=26, color=RED_B)
        error_label.next_to(real, DOWN, buff=0.45).to_edge(LEFT, buff=0.6)

        error = MathTex(
            r"E = |f - L| = |2.100582 - 2.10| \approx ", r"0.000582",
            font_size=34,
        ).next_to(error_label, DOWN, buff=0.2).shift(RIGHT * 0.4)
        error[1].set_color(RED_B)

        # Interpretación
        interp = Text(
            "Error relativo ≈ 0.028 %  —  aproximación muy precisa\n"
            "porque (1.98, 1.03) está muy cerca de (2, 1).",
            font_size=24,
            color=GRAY_B,
            line_spacing=1.35,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(aprox_label), Write(aprox))
        self.wait(0.7)
        self.play(FadeIn(real_label), Write(real))
        self.wait(0.7)
        self.play(FadeIn(error_label), Write(error))
        self.wait(0.5)
        self.play(FadeIn(interp, shift=UP * 0.15))
        self.wait(3)
