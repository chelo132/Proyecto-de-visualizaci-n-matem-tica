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


A, B   = 2.0, 1.0      # Punto de tangencia (a, b)
FAB    = f(A, B)       # f(2, 1) = 2
X0, Y0 = 1.98, 1.03   # Punto a aproximar
FX_AB  = 1.0           # fx(2, 1) = 1
FY_AB  = 4.0           # fy(2, 1) = 4


# ── Helpers reutilizables ────────────────────────────────────────────────────
def crear_encabezado(escena, texto, color=TEAL):
    """Dibuja título + línea separadora y los retorna como (titulo, sep)."""
    titulo = Text(texto, font_size=36, color=color)
    titulo.to_edge(UP, buff=0.3)
    sep = Line(LEFT * 6.3, RIGHT * 6.3, color=color, stroke_width=1)
    sep.next_to(titulo, DOWN, buff=0.12)
    escena.play(Write(titulo), run_time=0.8)
    escena.play(Create(sep), run_time=0.4)
    return titulo, sep


def crear_tarjeta_hud(mobject, color_borde=TEAL, buff=0.18, opacity=0.92):
    """Crea una tarjeta semitransparente con borde para alto contraste."""
    fondo = RoundedRectangle(
        corner_radius=0.12,
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
    def construct(self):
        titulo = Text("Plano Tangente", font_size=52, color=TEAL)
        subtitulo = Text("y Aproximación Lineal", font_size=38, color=TEAL_B)
        titulo.to_edge(UP, buff=0.45)
        subtitulo.next_to(titulo, DOWN, buff=0.2)

        self.play(Write(titulo), run_time=1.2)
        self.play(Write(subtitulo), run_time=0.8)
        self.wait(2)

        sep = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=1.5)
        sep.next_to(subtitulo, DOWN, buff=0.3)
        self.play(Create(sep))

        label_func = Text("Función asignada:", font_size=26, color=GRAY_B)
        func_tex   = MathTex(r"f(x,\,y) = xy^2", font_size=40, color=WHITE)
        fila1 = VGroup(label_func, func_tex).arrange(RIGHT, buff=0.35)
        fila1.next_to(sep, DOWN, buff=0.55)

        self.play(FadeIn(label_func), Write(func_tex))
        self.wait(2)

        label_pto = Text("Punto de tangencia:", font_size=26, color=GRAY_B)
        pto_tex   = MathTex(r"(a,\,b) = (2,\,1)", font_size=40, color=YELLOW)
        fila2 = VGroup(label_pto, pto_tex).arrange(RIGHT, buff=0.35)
        fila2.next_to(fila1, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_pto), Write(pto_tex))
        self.wait(2)

        label_apr = Text("Valor a aproximar:", font_size=26, color=GRAY_B)
        apr_tex   = MathTex(r"f(1.98,\;1.03) = \;?", font_size=40, color=GREEN_B)
        fila3 = VGroup(label_apr, apr_tex).arrange(RIGHT, buff=0.35)
        fila3.next_to(fila2, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_apr), Write(apr_tex))
        self.wait(2)

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
        self.wait(30)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 1 — Identificación del Punto y Construcción de Superficie 3D
# ════════════════════════════════════════════════════════════════════════════
class Escena01Superficie(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=-50 * DEGREES)

        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[-0.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=6,
            y_length=5,
            z_length=4.5,
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        etiqueta_func = MathTex(r"z = f(x,y) = xy^2", font_size=30, color=WHITE)
        etiqueta_calc = MathTex(r"f(2,1) = 2 \cdot (1)^2 = 2", font_size=28, color=YELLOW)
        etiqueta_p    = MathTex(r"P = (2,\, 1,\, 2)", font_size=30, color=RED_B)
        
        panel_contenido = VGroup(etiqueta_func, etiqueta_calc, etiqueta_p).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        panel_contenido.to_corner(UL, buff=0.35)
        tarjeta_panel = crear_tarjeta_hud(panel_contenido, color_borde=TEAL_C, buff=0.18)
        
        self.add_fixed_in_frame_mobjects(tarjeta_panel)
        self.remove(tarjeta_panel)

        self.play(Create(ejes), Write(labels), run_time=1.2)
        self.play(FadeIn(tarjeta_panel), run_time=0.8)
        self.wait(21)

        pos_base = ejes.c2p(A, B, 0)
        pos_P = ejes.c2p(A, B, FAB)

        punto_base = Dot3D(point=pos_base, radius=0.07, color=YELLOW)
        lbl_base = MathTex(r"(2,1,0)", font_size=20, color=YELLOW)
        lbl_base.next_to(punto_base, DOWN, buff=0.1)

        linea_elevacion = DashedLine(pos_base, pos_P, color=YELLOW_B, stroke_width=4, dash_length=0.1)
        punto_P = Dot3D(point=pos_P, radius=0.09, color=RED)

        self.play(FadeIn(punto_base), run_time=0.6)
        self.wait(2)

        self.play(Create(linea_elevacion), run_time=0.8)
        self.wait(2)

        self.play(FadeIn(punto_P), run_time=0.8)
        self.wait(5)

        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.5, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.72, stroke_opacity=0.15)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_B])

        self.play(Create(superficie), run_time=2.0)
        self.wait(0.5)

        self.move_camera(theta=-15 * DEGREES, phi=65 * DEGREES, run_time=3.0)
        self.wait(1.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 2 — Derivadas Parciales (Cálculo Algebraico)
# ════════════════════════════════════════════════════════════════════════════
class Escena02DerivadasParciales(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Derivadas Parciales en (2, 1)")

        fx_formula = MathTex(r"f_x(x,y) = \frac{\partial}{\partial x}(xy^2) = y^2", font_size=32)
        fx_eval    = MathTex(r"f_x(2,1) = (1)^2 = 1", font_size=34, color=YELLOW)
        fx_interp  = Text("• Pendiente en dirección x: sube 1 unidad vertical por cada 1 en x.", font_size=20, color=GRAY_B)
        
        bloque_x = VGroup(fx_formula, fx_eval, fx_interp).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bloque_x.next_to(sep, DOWN, buff=0.4).to_edge(LEFT, buff=0.8)

        fy_formula = MathTex(r"f_y(x,y) = \frac{\partial}{\partial y}(xy^2) = 2xy", font_size=32)
        fy_eval    = MathTex(r"f_y(2,1) = 2(2)(1) = 4", font_size=34, color=GREEN_B)
        fy_interp  = Text("• Pendiente en dirección y: sube 4 unidades verticales por cada 1 en y.", font_size=20, color=GRAY_B)

        bloque_y = VGroup(fy_formula, fy_eval, fy_interp).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        bloque_y.next_to(bloque_x, DOWN, buff=0.45).align_to(bloque_x, LEFT)
        self.wait(6)

        self.play(Write(fx_formula))
        self.wait(13)

        self.play(Write(fx_eval))
        self.wait(2)
        self.play(FadeIn(fx_interp))
        self.wait(6)

        self.play(Write(fy_formula))
        self.wait(10)
        self.play(Write(fy_eval))
        self.play(FadeIn(fy_interp))
        self.wait(1.5)

        resumen = Text(
            "Ambas pendientes f_x = 1 y f_y = 4 definen las direcciones tangentes\n"
            "que forman el plano tangente en el punto P(2, 1, 2).",
            font_size=22,
            color=TEAL_B,
            line_spacing=1.3
        ).to_edge(DOWN, buff=0.5)
        caja_res = SurroundingRectangle(resumen, color=TEAL, buff=0.15, corner_radius=0.1)

        self.play(Write(resumen), Create(caja_res))
        self.wait(3.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 3 — Visualización 3D de las Derivadas Parciales en P(2, 1, 2)
# ════════════════════════════════════════════════════════════════════════════
class Escena03GraficaDerivadas3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES)

        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[-0.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=6,
            y_length=5,
            z_length=4.5,
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.6, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.45, stroke_opacity=0.1)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_C])

        pos_P = ejes.c2p(A, B, FAB)
        punto_P = Dot3D(point=pos_P, radius=0.09, color=RED)

        curva_x = ParametricFunction(
            lambda t: ejes.c2p(t, 1.0, f(t, 1.0)),
            t_range=[1.0, 3.0],
            color=YELLOW,
            stroke_width=6,
        )
        v_tan_x = Line(ejes.c2p(1.2, 1.0, 1.2), ejes.c2p(2.8, 1.0, 2.8), color=YELLOW_A, stroke_width=6)

        curva_y = ParametricFunction(
            lambda t: ejes.c2p(2.0, t, f(2.0, t)),
            t_range=[0.3, 1.8],
            color=GREEN_B,
            stroke_width=6,
        )
        v_tan_y = Line(ejes.c2p(2.0, 0.4, -0.4), ejes.c2p(2.0, 1.6, 4.4), color=GREEN_A, stroke_width=6)

        lbl_info = Text("Significado Geométrico de f_x y f_y", font_size=20, color=TEAL_B)
        lbl_fx   = MathTex(r"f_x(2,1) = 1 \implies \text{Pendiente en } x \text{ con } y=1", font_size=18, color=YELLOW)
        lbl_fy   = MathTex(r"f_y(2,1) = 4 \implies \text{Pendiente en } y \text{ con } x=2", font_size=18, color=GREEN_B)

        panel = VGroup(lbl_info, lbl_fx, lbl_fy).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        panel.to_corner(UL, buff=0.35)
        tarjeta_panel = crear_tarjeta_hud(panel, color_borde=TEAL_C, buff=0.15)
        
        self.add_fixed_in_frame_mobjects(tarjeta_panel)
        self.remove(tarjeta_panel)

        self.play(Create(ejes), Write(labels), run_time=1)
        self.play(Create(superficie), FadeIn(punto_P), run_time=1.2)
        self.play(FadeIn(tarjeta_panel), run_time=0.8)

        self.move_camera(phi=85 * DEGREES, theta=-90 * DEGREES, run_time=2.0)
        self.play(Create(curva_x), Create(v_tan_x), run_time=1.5)
        self.wait(11)

        self.move_camera(phi=85 * DEGREES, theta=0 * DEGREES, run_time=2.0)
        self.play(Create(curva_y), Create(v_tan_y), run_time=1.5)
        self.wait(1.5)

        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=2.0)
        self.wait(12)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 4 — Construcción Explicativa de la Ecuación del Plano Tangente
# ════════════════════════════════════════════════════════════════════════════
class Escena04ConstruccionEcuacionPlano(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Construcción del Plano Tangente")

        formula_gen = MathTex(
            r"z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)",
            font_size=34,
            color=WHITE,
        ).next_to(sep, DOWN, buff=0.35)

        self.play(Write(formula_gen))
        self.wait(7)

        p1 = MathTex(r"\bullet \text{ Altura base: } f(2,1) = 2", font_size=26, color=YELLOW)
        p2 = MathTex(r"\bullet \text{ Cambio en } x: f_x(2,1)(x-2) = 1\cdot(x-2)", font_size=26, color=YELLOW)
        p3 = MathTex(r"\bullet \text{ Cambio en } y: f_y(2,1)(y-1) = 4\cdot(y-1)", font_size=26, color=GREEN_B)

        desglose = VGroup(p1, p2, p3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        desglose.next_to(formula_gen, DOWN, buff=0.35).to_edge(LEFT, buff=1.0)

        for el in desglose:
            self.play(FadeIn(el, shift=RIGHT * 0.2))
            self.wait(0.4)

        sustitucion = MathTex(
            r"z = 2 + 1\cdot(x - 2) + 4\cdot(y - 1)",
            font_size=34,
            color=TEAL_B,
        ).next_to(desglose, DOWN, buff=0.35)

        simplificacion = MathTex(
            r"z = x + 4y - 4",
            font_size=42,
            color=ORANGE,
        ).next_to(sustitucion, DOWN, buff=0.3)

        caja_plano = SurroundingRectangle(simplificacion, color=ORANGE, buff=0.18, corner_radius=0.12)

        self.play(Write(sustitucion))
        self.wait(10)
        self.play(Write(simplificacion), Create(caja_plano))
        self.wait(2)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 5 — Graficación 3D del Plano Tangente y Zoom Local
# ════════════════════════════════════════════════════════════════════════════
class Escena05GraficaPlanoTangente3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-55 * DEGREES)

        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[-0.5, 2.5, 1],
            z_range=[0, 6, 2],
            x_length=6,
            y_length=5,
            z_length=4.5,
        )
        labels = ejes.get_axis_labels(x_label="x", y_label="y", z_label="z")

        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.6, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.55, stroke_opacity=0.1)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_C])

        pos_P = ejes.c2p(A, B, FAB)
        punto_P = Dot3D(point=pos_P, radius=0.09, color=RED)

        plano = Surface(
            lambda u, v: ejes.c2p(u, v, L(u, v)),
            u_range=[1.0, 3.0],
            v_range=[0.2, 1.8],
            resolution=(14, 14),
        )
        plano.set_style(fill_opacity=0.5, stroke_opacity=0.2)
        plano.set_color(ORANGE)

        lbl_plano = MathTex(r"\text{Plano Tangente: } z = x + 4y - 4", font_size=26, color=ORANGE)
        lbl_plano.to_corner(UL, buff=0.35)
        tarjeta_plano = crear_tarjeta_hud(lbl_plano, color_borde=ORANGE)
        
        self.add_fixed_in_frame_mobjects(tarjeta_plano)
        self.remove(tarjeta_plano)

        self.play(Create(ejes), Write(labels), run_time=1)
        self.play(Create(superficie), FadeIn(punto_P), run_time=1.2)
        self.play(FadeIn(tarjeta_plano), run_time=0.6)
        
        self.play(Create(plano), run_time=2.0)
        self.wait(1.0)

        lbl_zoom = Text("Acercamiento Local: Superficie y Plano se confunden", font_size=19, color=YELLOW)
        lbl_zoom.to_corner(UR, buff=0.35)
        tarjeta_zoom = crear_tarjeta_hud(lbl_zoom, color_borde=YELLOW)

        self.wait(10)
        self.add_fixed_in_frame_mobjects(tarjeta_zoom)
        self.remove(tarjeta_zoom)
        self.play(FadeIn(tarjeta_zoom), run_time=0.6)

        self.move_camera(
            phi=55 * DEGREES,
            theta=-45 * DEGREES,
            zoom=2.3,
            frame_center=pos_P,
            run_time=3.0,
        )
        self.wait(10)

        self.move_camera(
            phi=68 * DEGREES,
            theta=-55 * DEGREES,
            zoom=1.0,
            frame_center=ORIGIN,
            run_time=2.5,
        )

        self.wait(10)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 6 — Aproximación Lineal L(x, y)
# ════════════════════════════════════════════════════════════════════════════
class Escena06Aproximacion(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Aproximación Lineal L(x, y)")

        general = MathTex(
            r"L(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)",
            font_size=32,
        ).next_to(sep, DOWN, buff=0.4)

        sustit = MathTex(
            r"L(x,y) = 2 + 1\cdot(x-2) + 4\cdot(y-1)",
            font_size=34,
        ).next_to(general, DOWN, buff=0.35)

        simple = MathTex(
            r"L(x,y) = x + 4y - 4",
            font_size=44,
            color=YELLOW,
        ).next_to(sustit, DOWN, buff=0.45)
        caja = SurroundingRectangle(simple, color=YELLOW, buff=0.18, corner_radius=0.1)

        self.wait(3)
        self.play(Write(general))
        self.play(Write(sustit))
        self.play(Write(simple), Create(caja))
        self.wait(1)

        just_tit = Text("¿Por qué aproxima a f(x, y)?", font_size=25, color=TEAL_C)
        just_tit.next_to(caja, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)

        just_desc = Text(
            "• Geométricamente: z_plano ≈ z_superficie cerca del punto de tangencia.\n"
            "• Operativamente: reemplaza una función no lineal por una expresión\n"
            "  lineal muy fácil de calcular: f(x, y) ≈ L(x, y) para (x, y) → (2, 1).",
            font_size=22,
            color=WHITE,
            line_spacing=1.3,
        ).next_to(just_tit, DOWN, buff=0.15).align_to(just_tit, LEFT)

        self.play(FadeIn(just_tit), FadeIn(just_desc, shift=UP * 0.15))
        self.wait(17)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 7 — Estimación y Comparación Directa con Valor Real
# ════════════════════════════════════════════════════════════════════════════
class Escena07EstimacionComparacion(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Estimación, Valor Real y Comparación")

        aprox_label = Text("1. Aproximación Lineal L(1.98, 1.03):", font_size=22, color=YELLOW)
        aprox_label.next_to(sep, DOWN, buff=0.3).to_edge(LEFT, buff=0.6)

        aprox = MathTex(
            r"L(1.98,\ 1.03) = 1.98 + 4(1.03) - 4 = ",
            r"2.100000",
            font_size=30,
        )
        aprox[1].set_color(YELLOW)
        aprox.next_to(aprox_label, DOWN, buff=0.1).to_edge(LEFT, buff=0.9)

        self.play(FadeIn(aprox_label), Write(aprox))
        self.wait(22)

        real_label = Text("2. Valor Real (Cálculo exacto / Herramienta computacional):", font_size=22, color=GREEN_B)
        real_label.next_to(aprox, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)

        real = MathTex(
            r"f(1.98,\ 1.03) = 1.98 \cdot (1.03)^2 = ",
            r"2.100582",
            font_size=30,
        )
        real[1].set_color(GREEN_B)
        real.next_to(real_label, DOWN, buff=0.1).to_edge(LEFT, buff=0.9)

        self.play(FadeIn(real_label), Write(real))
        self.wait(5)

        comp_label = Text("3. Comparación y Error Absoluto:", font_size=22, color=RED_B)
        comp_label.next_to(real, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)

        error = MathTex(
            r"E = |f(1.98, 1.03) - L(1.98, 1.03)| = |2.100582 - 2.100000| = ",
            r"0.000582",
            r"\quad (\approx 0.0277\%)",
            font_size=28,
        )
        error[1].set_color(RED_B)
        error.next_to(comp_label, DOWN, buff=0.1).to_edge(LEFT, buff=0.9)

        self.play(FadeIn(comp_label), Write(error))
        self.wait(0.6)

        concl_text = Text(
            "¡Ambos resultados son prácticamente idénticos!\n"
            "La diferencia es de sólo 0.000582 (un error relativo de apenas 0.0277%).\n"
            "Esto demuestra la altísima precisión del plano tangente muy cerca de (2, 1).",
            font_size=20,
            color=WHITE,
            line_spacing=1.35,
        ).to_edge(DOWN, buff=0.3)
        caja_concl = SurroundingRectangle(concl_text, color=TEAL_C, buff=0.15, corner_radius=0.1)

        self.play(Create(caja_concl), FadeIn(concl_text))
        self.wait(6.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 8 — Visualización 3D: Cercanía del Punto Asignado en la Superficie
# ════════════════════════════════════════════════════════════════════════════
class Escena08VisualizacionAproximacion3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=68 * DEGREES, theta=-45 * DEGREES, zoom=1.1)

        ejes = ThreeDAxes(
            x_range=[0, 3.5, 1],
            y_range=[0, 2.2, 1],
            z_range=[0, 8, 2],
            x_length=6.0,
            y_length=5.0,
            z_length=4.5,
        )

        pos_P = ejes.c2p(A, B, FAB)

        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.6, 3.3],
            v_range=[0.1, 1.8],
            resolution=(24, 24),
        )
        superficie.set_style(fill_opacity=0.6, stroke_opacity=0.1)
        superficie.set_color(BLUE_C)

        plano = Surface(
            lambda u, v: ejes.c2p(u, v, L(u, v)),
            u_range=[0.6, 3.3],
            v_range=[0.1, 1.8],
            resolution=(16, 16),
        )
        plano.set_style(fill_opacity=0.45, stroke_opacity=0.15)
        plano.set_color(ORANGE)

        pt_P = Dot3D(point=pos_P, radius=0.08, color=RED)

        pos_eval = ejes.c2p(X0, Y0, f(X0, Y0))
        pt_eval = Dot3D(point=pos_eval, radius=0.08, color=YELLOW)

        escena_3d = VGroup(ejes, superficie, plano, pt_P, pt_eval)
        escena_3d.shift(-pos_P)

        lbl_p_asig = Text("Aproximación en (1.98, 1.03)", font_size=18, color=YELLOW)
        lbl_val_r  = MathTex(r"\text{Superficie: } f(1.98, 1.03) = 2.100582", font_size=16, color=GREEN_B)
        lbl_val_a  = MathTex(r"\text{Plano Tangente: } L(1.98, 1.03) = 2.100000", font_size=16, color=ORANGE)
        lbl_diff   = MathTex(r"\text{Diferencia: } E = 0.000582 \implies \text{Casi indistinguibles}", font_size=16, color=WHITE)

        panel = VGroup(lbl_p_asig, lbl_val_r, lbl_val_a, lbl_diff).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        panel.to_corner(UL, buff=0.35)
        tarjeta = crear_tarjeta_hud(panel, color_borde=YELLOW, buff=0.14)

        self.add_fixed_in_frame_mobjects(tarjeta)
        self.remove(tarjeta)

        self.play(Create(ejes), run_time=1.0)
        self.play(Create(superficie), Create(plano), FadeIn(pt_P), run_time=1.5)
        self.play(FadeIn(tarjeta), run_time=0.6)
        self.wait(2.0)
        self.play(FadeIn(pt_eval), run_time=1.0)
        self.wait(16.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 9 — Geometría del Error y Curvatura (Compatible con ThreeDScene)
# ════════════════════════════════════════════════════════════════════════════
class Escena09CurvaturaError(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.0)

        titulo = Text("Geometría y Curvatura del Error", font_size=34, color=TEAL)
        titulo.to_edge(UP, buff=0.25)
        sep = Line(LEFT * 6.3, RIGHT * 6.3, color=TEAL, stroke_width=1)
        sep.next_to(titulo, DOWN, buff=0.1)
        self.add(titulo, sep)

        ejes_2d = Axes(
            x_range=[0.4, 1.6, 0.2],
            y_range=[0, 4.5, 1],
            x_length=7.4,
            y_length=3.2,
            axis_config={"color": GRAY_C, "include_tip": True},
        ).move_to(DOWN * 0.8 + RIGHT * 0.4)

        x_label = MathTex("y", font_size=24, color=WHITE).next_to(ejes_2d.x_axis.get_end(), RIGHT, buff=0.25)
        z_label = MathTex("z", font_size=24, color=WHITE).next_to(ejes_2d.y_axis.get_end(), UP, buff=0.25)
        labels_2d = VGroup(x_label, z_label)

        curva_f = ejes_2d.plot(lambda y: 2 * y**2, x_range=[0.45, 1.55], color=GREEN_B, stroke_width=4)
        recta_L = ejes_2d.plot(lambda y: 4 * y - 2, x_range=[0.45, 1.55], color=YELLOW, stroke_width=4)

        pos_P_2d = ejes_2d.c2p(1.0, 2.0)
        
        halo_P = Dot(pos_P_2d, radius=0.14, color=WHITE, fill_opacity=0.4)
        pt_tangencia = Dot(pos_P_2d, radius=0.08, color=RED)
        
        lbl_p = MathTex(r"P(2,1,2)", font_size=22, color=WHITE)
        lbl_p.next_to(halo_P, UP + LEFT, buff=0.12)
        
        grupo_P = VGroup(halo_P, pt_tangencia, lbl_p)
        grupo_P.set_z_index(20)

        lbl_curva  = MathTex(r"\text{Superficie: } f(2,y) = 2y^2", font_size=18, color=GREEN_B)
        lbl_recta  = MathTex(r"\text{Plano: } L(2,y) = 4y - 2", font_size=18, color=YELLOW)
        lbl_brecha = MathTex(r"\text{Error: } E(y) = |f - L| = 2(y-1)^2", font_size=18, color=RED_B)

        panel_leyenda = VGroup(lbl_curva, lbl_recta, lbl_brecha).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tarjeta_leyenda = crear_tarjeta_hud(panel_leyenda, color_borde=TEAL_C, buff=0.12, opacity=0.92)
        tarjeta_leyenda.next_to(sep, DOWN, buff=0.15).to_edge(LEFT, buff=0.5)

        self.play(Create(ejes_2d), Write(labels_2d), run_time=1.0)
        self.play(Create(curva_f), Create(recta_L), run_time=1.2)
        self.play(FadeIn(grupo_P), run_time=0.8)
        self.play(FadeIn(tarjeta_leyenda), run_time=0.8)
        self.wait(0.4)

        area_error = ejes_2d.get_area(
            curva_f,
            x_range=[0.45, 1.55],
            bounded_graph=recta_L,
            color=RED,
            opacity=0.3,
        )
        area_error.set_z_index(1)
        self.play(FadeIn(area_error), run_time=1.0)
        self.wait(22)

        self.play(FadeOut(tarjeta_leyenda), run_time=0.5)

        # Transición de zoom compatible con ThreeDScene
        self.move_camera(
            frame_center=pos_P_2d,
            zoom=2.5,
            run_time=2.2,
        )
        self.wait(0.4)

        pt_eval = Dot(ejes_2d.c2p(1.03, 2 * (1.03)**2), radius=0.03, color=YELLOW)
        pt_eval.set_z_index(20)
        
        linea_error_local = Line(
            ejes_2d.c2p(1.03, 4 * 1.03 - 2),
            ejes_2d.c2p(1.03, 2 * (1.03)**2),
            color=RED_A,
            stroke_width=3.5,
        )
        linea_error_local.set_z_index(15)

        lbl_eval_cercana = MathTex(
            r"y_0 = 1.03 \implies E \approx 0.000582", font_size=15, color=WHITE
        )
        tarjeta_local = crear_tarjeta_hud(lbl_eval_cercana, color_borde=YELLOW, buff=0.08, opacity=0.95)
        tarjeta_local.next_to(pt_eval, UR, buff=0.1)

        self.play(FadeIn(pt_eval), Create(linea_error_local), FadeIn(tarjeta_local), run_time=1.2)
        self.wait(1.8)

        self.play(FadeOut(tarjeta_local), run_time=0.4)
        self.move_camera(
            frame_center=ORIGIN,
            zoom=1.0,
            run_time=2.0,
        )
        self.play(FadeIn(tarjeta_leyenda), run_time=0.6)
        self.wait(15.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 10 — Conclusión
# ════════════════════════════════════════════════════════════════════════════
class Escena10Conclusion(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Conclusiones")

        pregunta = Text(
            "¿Cómo utilizamos el plano tangente para aproximar?",
            font_size=27,
            color=BLUE_B,
        ).next_to(sep, DOWN, buff=0.35)
        caja_p = SurroundingRectangle(pregunta, color=BLUE_B, buff=0.15, corner_radius=0.1)

        self.play(Write(pregunta), Create(caja_p), run_time=1.2)
        self.wait(0.5)

        p1_tit = Text("1. Principio de Linealidad Local:", font_size=24, color=YELLOW)
        p1_desc = Text(
            "Cerca del punto de tangencia (a, b), la superficie curva se comporta\n"
            "casi exactamente igual que su plano tangente.",
            font_size=21,
            color=WHITE,
            line_spacing=1.25,
        )
        b1 = VGroup(p1_tit, p1_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        p2_tit = Text("2. Simplificación del Cálculo:", font_size=24, color=GREEN_B)
        p2_desc = Text(
            "Sustituimos una función no lineal f(x, y) por una combinación lineal L(x, y)\n"
            "mucho más fácil de evaluar.",
            font_size=21,
            color=WHITE,
            line_spacing=1.25,
        )
        b2 = VGroup(p2_tit, p2_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        p3_tit = Text("3. Validez Local y Control del Error:", font_size=24, color=RED_B)
        p3_desc = Text(
            "La aproximación es altamente precisa sólo cerca del punto (E ≈ 0.028%).\n"
            "A mayor distancia, el error crece y el plano pierde representatividad.",
            font_size=21,
            color=WHITE,
            line_spacing=1.25,
        )
        b3 = VGroup(p3_tit, p3_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        conclusiones = VGroup(b1, b2, b3).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
        conclusiones.next_to(caja_p, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)

        for bloque in conclusiones:
            self.play(FadeIn(bloque, shift=RIGHT * 0.2), run_time=1.1)
            self.wait(8)

        self.wait(8)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA MASTER — Une todas las escenas en 1 solo video continuo
# ════════════════════════════════════════════════════════════════════════════
class ProyectoCompleto(ThreeDScene):
    def reset_2d(self):
        """Restablece la perspectiva de la cámara 3D al plano 2D frontal."""
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1.0)
        self.move_camera(frame_center=ORIGIN, run_time=0.1)

    def construct(self):
        # Escena 0
        self.reset_2d()
        Escena00Introduccion.construct(self)
        self.clear()

        # Escena 1
        Escena01Superficie.construct(self)
        self.clear()

        # Escena 2
        self.reset_2d()
        Escena02DerivadasParciales.construct(self)
        self.clear()

        # Escena 3
        Escena03GraficaDerivadas3D.construct(self)
        self.clear()

        # Escena 4
        self.reset_2d()
        Escena04ConstruccionEcuacionPlano.construct(self)
        self.clear()

        # Escena 5
        Escena05GraficaPlanoTangente3D.construct(self)
        self.clear()

        # Escena 6
        self.reset_2d()
        Escena06Aproximacion.construct(self)
        self.clear()

        # Escena 7
        self.reset_2d()
        Escena07EstimacionComparacion.construct(self)
        self.clear()

        # Escena 8
        Escena08VisualizacionAproximacion3D.construct(self)
        self.clear()

        # Escena 9
        self.reset_2d()
        Escena09CurvaturaError.construct(self)
        self.clear()

        # Escena 10
        self.reset_2d()
        Escena10Conclusion.construct(self)
        self.clear()