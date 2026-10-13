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


def crear_tarjeta_hud(mobject, color_borde=TEAL, buff=0.2, opacity=0.85):
    """Crea una tarjeta semitransparente con borde para dar alto contraste sobre fondos 3D."""
    fondo = RoundedRectangle(
        corner_radius=0.15,
        fill_color="#0b0b14",
        fill_opacity=opacity,
        stroke_color=color_borde,
        stroke_width=1.5,
        width=mobject.width + 2 * buff,
        height=mobject.height + 2 * buff,
    ).move_to(mobject)
    return VGroup(fondo, mobject)



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
    Presenta la función f(x,y)=xy² en 3D, el punto base (2,1) en el plano xy,
    su elevación a la superficie P=(2,1,2), y una rotación clara.
    """

    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        # Ejes 3D con rangos balanceados
        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[-0.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=6,
            y_length=5,
            z_length=4.5,
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Superficie f(x,y) = x * y^2
        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.5, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.72, stroke_opacity=0.15)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_B])

        # Elementos en plano xy: punto (a,b,0) y proyección
        pos_base = ejes.c2p(A, B, 0)
        pos_P = ejes.c2p(A, B, FAB)

        punto_base = Dot3D(point=pos_base, radius=0.08, color=YELLOW)
        linea_elevacion = DashedLine(pos_base, pos_P, color=YELLOW_B, stroke_width=4, dash_length=0.1)
        punto_P = Dot3D(point=pos_P, radius=0.11, color=RED)

        # Textos 2D fijos en pantalla
        etiqueta_func = MathTex(r"z = f(x,y) = xy^2", font_size=34, color=WHITE)
        etiqueta_p = MathTex(r"P = (2,\, 1,\, f(2,1)) = (2,\, 1,\, 2)", font_size=30, color=YELLOW)
        panel_2d = VGroup(etiqueta_func, etiqueta_p).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        panel_2d.to_corner(UL, buff=0.4)
        self.add_fixed_in_frame_mobjects(panel_2d)

        # Animaciones secuenciales
        self.play(Create(ejes), Write(labels), run_time=1.2)
        self.play(Write(etiqueta_func), run_time=0.8)
        self.play(Create(superficie), run_time=2.2)
        self.wait(0.5)

        # Mostrar proyección de (2,1) y elevar hasta P
        self.play(FadeIn(punto_base), run_time=0.8)
        self.play(Create(linea_elevacion), run_time=1)
        self.play(FadeIn(punto_P), Write(etiqueta_p), run_time=1)
        self.wait(0.8)

        # Giro de cámara para apreciar la curvatura de la superficie
        self.move_camera(theta=-15 * DEGREES, phi=65 * DEGREES, run_time=3.5)
        self.wait(1.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 3 — Plano tangente 3D y Comportamiento Local (Zoom)
# ════════════════════════════════════════════════════════════════════════════
class Escena03PlanoTangente(ThreeDScene):
    """
    Construye visualmente el plano tangente a partir de las pendientes fx y fy,
    muestra el plano z = x + 4y - 4, hace zoom local al punto de tangencia
    para evidenciar f ≈ L, e ilustra la aproximación en (1.98, 1.03).
    """

    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES)

        # Ejes 3D
        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[-0.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=6,
            y_length=5,
            z_length=4.5,
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        # Superficie f(x,y)
        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.6, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.6, stroke_opacity=0.1)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_C])

        # Punto de tangencia P = (2, 1, 2)
        pos_P = ejes.c2p(A, B, FAB)
        punto_P = Dot3D(point=pos_P, radius=0.11, color=RED)

        # Curvas sobre la superficie que pasan por (2,1):
        # 1. Curva variando x (con y=1 fijo): f(x,1) = x
        curva_x = ParametricFunction(
            lambda t: ejes.c2p(t, 1.0, f(t, 1.0)),
            t_range=[1.0, 3.0],
            color=BLUE_A,
            stroke_width=4,
        )
        # 2. Curva variando y (con x=2 fijo): f(2,y) = 2y^2
        curva_y = ParametricFunction(
            lambda t: ejes.c2p(2.0, t, f(2.0, t)),
            t_range=[0.3, 1.8],
            color=GREEN_A,
            stroke_width=4,
        )

        # Vectores/rectas tangentes correspondientes a fx=1 y fy=4
        v_tan_x = Line(ejes.c2p(1.2, 1.0, 1.2), ejes.c2p(2.8, 1.0, 2.8), color=YELLOW, stroke_width=5)
        v_tan_y = Line(ejes.c2p(2.0, 0.4, -0.4), ejes.c2p(2.0, 1.6, 4.4), color=YELLOW, stroke_width=5)

        # Plano tangente z = x + 4y - 4 alrededor de (2,1)
        plano = Surface(
            lambda u, v: ejes.c2p(u, v, L(u, v)),
            u_range=[1.0, 3.0],
            v_range=[0.2, 1.8],
            resolution=(12, 12),
        )
        plano.set_style(fill_opacity=0.45, stroke_opacity=0.3)
        plano.set_color(ORANGE)

        # Elementos 2D fijos en pantalla
        lbl_ecuacion = MathTex(r"\text{Plano Tangente: } z = x + 4y - 4", font_size=30, color=ORANGE)
        lbl_info = Text("Las pendientes fx=1 y fy=4 generan el plano tangente.", font_size=22, color=GRAY_B)
        info_group = VGroup(lbl_ecuacion, lbl_info).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        info_group.to_corner(UL, buff=0.4)
        self.add_fixed_in_frame_mobjects(info_group)

        # 1. Mostrar superficie y punto P
        self.play(Create(ejes), Write(labels), run_time=1)
        self.play(Create(superficie), FadeIn(punto_P), run_time=1.8)
        self.wait(0.5)

        # 2. Mostrar curvas sobre la superficie y sus pendientes tangentes
        self.play(Create(curva_x), Create(curva_y), run_time=1.5)
        self.play(Create(v_tan_x), Create(v_tan_y), run_time=1.2)
        self.wait(0.8)

        # 3. Formación del plano tangente
        self.play(Write(lbl_ecuacion), FadeIn(lbl_info), run_time=0.8)
        self.play(
            Create(plano),
            FadeOut(curva_x), FadeOut(curva_y),
            FadeOut(v_tan_x), FadeOut(v_tan_y),
            run_time=2,
        )
        self.wait(1)

        # 4. ZOOM O ACERCAMIENTO AL PUNTO DE TANGENCIA (Obligatorio en pauta)
        lbl_zoom = Text("Acercamiento: localmente la superficie y el plano coinciden", font_size=23, color=YELLOW)
        lbl_zoom.to_corner(UR, buff=0.4)
        self.add_fixed_in_frame_mobjects(lbl_zoom)

        self.play(Write(lbl_zoom), run_time=0.8)
        # Acercar cámara y enfocar cerca de P
        self.move_camera(
            phi=60 * DEGREES,
            theta=-35 * DEGREES,
            zoom=2.3,
            frame_center=pos_P,
            run_time=3.5,
        )
        self.wait(1.5)

        # 5. Punto a aproximar (1.98, 1.03) cerca de (2,1)
        pos_real = ejes.c2p(X0, Y0, f(X0, Y0))
        pos_aprox = ejes.c2p(X0, Y0, L(X0, Y0))

        punto_aprox = Dot3D(point=pos_aprox, radius=0.04, color=YELLOW)
        punto_real = Dot3D(point=pos_real, radius=0.04, color=GREEN)
        linea_error = Line(pos_aprox, pos_real, color=RED, stroke_width=6)

        lbl_eval = MathTex(r"(x_0,y_0) = (1.98,\, 1.03)", font_size=26, color=YELLOW)
        lbl_eval.next_to(lbl_zoom, DOWN, buff=0.2, aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(lbl_eval)

        self.play(Write(lbl_eval), FadeIn(punto_aprox), FadeIn(punto_real), Create(linea_error), run_time=1.5)
        self.wait(1)

        # Rotación sutil en zoom para notar cómo están prácticamente pegados
        self.move_camera(theta=-15 * DEGREES, phi=50 * DEGREES, run_time=2.5)
        self.wait(2)


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

        # ── Bloque 1: Aproximación lineal ────────────────────────────────
        aprox_label = Text("Aproximación lineal:", font_size=26, color=YELLOW)
        aprox_label.next_to(sep, DOWN, buff=0.45).to_edge(LEFT, buff=0.7)

        aprox = MathTex(
            r"L(1.98,\ 1.03) = 1.98 + 4(1.03) - 4 = ",
            r"2.10",
            font_size=32,
        )
        aprox[1].set_color(YELLOW)
        aprox.next_to(aprox_label, DOWN, buff=0.15).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(aprox_label))
        self.play(Write(aprox))
        self.wait(0.6)

        # ── Bloque 2: Valor real ──────────────────────────────────────────
        real_label = Text("Valor real:", font_size=26, color=GREEN_B)
        real_label.next_to(aprox, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)

        real = MathTex(
            r"f(1.98,\ 1.03) = 1.98 \cdot (1.03)^2 \approx ",
            r"2.100582",
            font_size=32,
        )
        real[1].set_color(GREEN_B)
        real.next_to(real_label, DOWN, buff=0.15).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(real_label))
        self.play(Write(real))
        self.wait(0.6)

        # ── Bloque 3: Error absoluto ──────────────────────────────────────
        error_label = Text("Error absoluto:", font_size=26, color=RED_B)
        error_label.next_to(real, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)

        error = MathTex(
            r"E = |f(1.98,1.03) - L(1.98,1.03)|",
            r"= |2.100582 - 2.10| \approx ",
            r"0.000582",
            font_size=30,
        )
        error[2].set_color(RED_B)
        error.next_to(error_label, DOWN, buff=0.15).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(error_label))
        self.play(Write(error))
        self.wait(0.5)

        # ── Interpretación ────────────────────────────────────────────────
        interp = Text(
            "Error relativo \u2248 0.028 %  \u2014  aproximación muy precisa\n"
            "porque (1.98, 1.03) está muy cerca de (2, 1).",
            font_size=24,
            color=GRAY_B,
            line_spacing=1.35,
        )
        interp.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(interp, shift=UP * 0.15))
        self.wait(3)

