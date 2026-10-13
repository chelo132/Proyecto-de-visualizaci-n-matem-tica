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
        self.wait(0.4)

        sep = Line(LEFT * 6.2, RIGHT * 6.2, color=TEAL, stroke_width=1.5)
        sep.next_to(subtitulo, DOWN, buff=0.3)
        self.play(Create(sep))

        label_func = Text("Función asignada:", font_size=26, color=GRAY_B)
        func_tex   = MathTex(r"f(x,\,y) = xy^2", font_size=40, color=WHITE)
        fila1 = VGroup(label_func, func_tex).arrange(RIGHT, buff=0.35)
        fila1.next_to(sep, DOWN, buff=0.55)

        self.play(FadeIn(label_func), Write(func_tex))
        self.wait(0.4)

        label_pto = Text("Punto de tangencia:", font_size=26, color=GRAY_B)
        pto_tex   = MathTex(r"(a,\,b) = (2,\,1)", font_size=40, color=YELLOW)
        fila2 = VGroup(label_pto, pto_tex).arrange(RIGHT, buff=0.35)
        fila2.next_to(fila1, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_pto), Write(pto_tex))
        self.wait(0.4)

        label_apr = Text("Valor a aproximar:", font_size=26, color=GRAY_B)
        apr_tex   = MathTex(r"f(1.98,\;1.03) = \;?", font_size=40, color=GREEN_B)
        fila3 = VGroup(label_apr, apr_tex).arrange(RIGHT, buff=0.35)
        fila3.next_to(fila2, DOWN, buff=0.45).align_to(fila1, LEFT)

        self.play(FadeIn(label_apr), Write(apr_tex))
        self.wait(0.5)

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
# ESCENA 1 — Función, evaluación explícita y superficie 3D
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

        superficie = Surface(
            lambda u, v: ejes.c2p(u, v, f(u, v)),
            u_range=[0.5, 3.2],
            v_range=[0.0, 2.2],
            resolution=(28, 28),
        )
        superficie.set_style(fill_opacity=0.72, stroke_opacity=0.15)
        superficie.set_fill_by_value(axes=ejes, colorscale=[BLUE_E, TEAL_D, GREEN_B])

        pos_base = ejes.c2p(A, B, 0)
        pos_P = ejes.c2p(A, B, FAB)

        punto_base = Dot3D(point=pos_base, radius=0.07, color=YELLOW)
        linea_elevacion = DashedLine(pos_base, pos_P, color=YELLOW_B, stroke_width=4, dash_length=0.1)
        punto_P = Dot3D(point=pos_P, radius=0.09, color=RED)

        etiqueta_func = MathTex(r"z = f(x,y) = xy^2", font_size=30, color=WHITE)
        etiqueta_calc = MathTex(r"f(2,1) = 2 \cdot (1)^2 = 2", font_size=28, color=YELLOW)
        etiqueta_p    = MathTex(r"P = (2,\, 1,\, 2)", font_size=30, color=RED_B)
        
        panel_contenido = VGroup(etiqueta_func, etiqueta_calc, etiqueta_p).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        panel_contenido.to_corner(UL, buff=0.35)
        tarjeta_panel = crear_tarjeta_hud(panel_contenido, color_borde=TEAL_C, buff=0.18)
        self.add_fixed_in_frame_mobjects(tarjeta_panel)

        self.play(Create(ejes), Write(labels), run_time=1.2)
        self.play(FadeIn(tarjeta_panel), run_time=0.8)
        self.play(Create(superficie), run_time=2.0)
        self.wait(0.5)

        self.play(FadeIn(punto_base), run_time=0.8)
        self.play(Create(linea_elevacion), run_time=1)
        self.play(FadeIn(punto_P), run_time=1)
        self.wait(0.8)

        self.move_camera(theta=-15 * DEGREES, phi=65 * DEGREES, run_time=3.5)
        self.wait(1.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 2 — Derivadas Parciales e Interpretación de Pendientes
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

        self.play(Write(fx_formula))
        self.play(Write(fx_eval))
        self.play(FadeIn(fx_interp))
        self.wait(1)

        self.play(Write(fy_formula))
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
        self.wait(3)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 3 — Plano Tangente: Vistas 2D, Construcción 3D y Zoom Local
# ════════════════════════════════════════════════════════════════════════════
class Escena03PlanoTangente(ThreeDScene):
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
        punto_P = Dot3D(point=pos_P, radius=0.08, color=RED)

        curva_x = ParametricFunction(
            lambda t: ejes.c2p(t, 1.0, f(t, 1.0)),
            t_range=[1.0, 3.0],
            color=BLUE_A,
            stroke_width=5,
        )
        curva_y = ParametricFunction(
            lambda t: ejes.c2p(2.0, t, f(2.0, t)),
            t_range=[0.3, 1.8],
            color=GREEN_A,
            stroke_width=5,
        )

        v_tan_x = Line(ejes.c2p(1.2, 1.0, 1.2), ejes.c2p(2.8, 1.0, 2.8), color=YELLOW, stroke_width=6)
        v_tan_y = Line(ejes.c2p(2.0, 0.4, -0.4), ejes.c2p(2.0, 1.6, 4.4), color=YELLOW, stroke_width=6)

        plano = Surface(
            lambda u, v: ejes.c2p(u, v, L(u, v)),
            u_range=[1.0, 3.0],
            v_range=[0.2, 1.8],
            resolution=(14, 14),
        )
        plano.set_style(fill_opacity=0.45, stroke_opacity=0.2)
        plano.set_color(ORANGE)

        lbl_corte = Text("Visualización 2D: cortes planos alrededor de P", font_size=20, color=YELLOW)
        lbl_corte.to_corner(UL, buff=0.35)
        tarjeta_corte = crear_tarjeta_hud(lbl_corte, color_borde=YELLOW)
        self.add_fixed_in_frame_mobjects(tarjeta_corte)

        self.play(Create(ejes), Write(labels), run_time=1)
        self.play(Create(superficie), FadeIn(punto_P), run_time=1.5)
        self.wait(0.4)

        self.move_camera(phi=90 * DEGREES, theta=-90 * DEGREES, run_time=2.2)
        self.play(Create(curva_x), Create(v_tan_x), run_time=1.4)
        self.wait(1)

        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES, run_time=2.2)
        self.play(Create(curva_y), Create(v_tan_y), run_time=1.4)
        self.wait(1)

        self.play(FadeOut(tarjeta_corte))
        lbl_plano = MathTex(r"\text{Plano Tangente: } z = x + 4y - 4", font_size=26, color=ORANGE)
        lbl_plano.to_corner(UL, buff=0.35)
        tarjeta_plano = crear_tarjeta_hud(lbl_plano, color_borde=ORANGE)
        self.add_fixed_in_frame_mobjects(tarjeta_plano)

        self.move_camera(phi=68 * DEGREES, theta=-55 * DEGREES, run_time=2.5)
        self.play(
            Create(plano),
            FadeOut(curva_x), FadeOut(curva_y),
            FadeOut(v_tan_x), FadeOut(v_tan_y),
            run_time=2
        )
        self.wait(0.8)

        lbl_zoom = Text("A escala local: la superficie y el plano se funden", font_size=19, color=YELLOW)
        lbl_zoom.to_corner(UR, buff=0.35)
        tarjeta_zoom = crear_tarjeta_hud(lbl_zoom, color_borde=YELLOW)
        self.add_fixed_in_frame_mobjects(tarjeta_zoom)

        self.move_camera(
            phi=55 * DEGREES,
            theta=-45 * DEGREES,
            zoom=2.3,
            frame_center=pos_P,
            run_time=3.0,
        )
        self.wait(2.0)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 4 — Aproximación lineal
# ════════════════════════════════════════════════════════════════════════════
class Escena04Aproximacion(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Aproximación lineal")

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

        self.play(Write(general))
        self.wait(0.7)
        self.play(Write(sustit))
        self.wait(0.7)
        self.play(Write(simple), Create(caja))
        self.wait(0.8)

        just_tit = Text("¿Por qué aproxima a f(x, y)?", font_size=25, color=TEAL_C)
        just_tit.next_to(caja, DOWN, buff=0.45).to_edge(LEFT, buff=0.8)

        just_desc = Text(
            "• Geométricamente: z_plano ≈ z_superficie cerca del punto de tangencia.\n"
            "• Operativamente: reemplaza una superficie no lineal por un cálculo\n"
            "  lineal inmediato: f(x, y) ≈ L(x, y) cuando (x, y) → (2, 1).",
            font_size=22,
            color=WHITE,
            line_spacing=1.3,
        ).next_to(just_tit, DOWN, buff=0.15).align_to(just_tit, LEFT)

        self.play(FadeIn(just_tit), FadeIn(just_desc, shift=UP * 0.15))
        self.wait(3.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 5 — Estimación y Análisis del Error Local
# ════════════════════════════════════════════════════════════════════════════
class Escena05EstimacionError(Scene):
    def construct(self):
        titulo, sep = crear_encabezado(self, "Estimación y análisis del error")

        aprox_label = Text("Aproximación lineal en (1.98, 1.03):", font_size=24, color=YELLOW)
        aprox_label.next_to(sep, DOWN, buff=0.35).to_edge(LEFT, buff=0.7)

        aprox = MathTex(
            r"L(1.98,\ 1.03) = 1.98 + 4(1.03) - 4 = ",
            r"2.10",
            font_size=31,
        )
        aprox[1].set_color(YELLOW)
        aprox.next_to(aprox_label, DOWN, buff=0.12).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(aprox_label))
        self.play(Write(aprox))
        self.wait(0.5)

        real_label = Text("Valor real (evaluación exacta):", font_size=24, color=GREEN_B)
        real_label.next_to(aprox, DOWN, buff=0.3).to_edge(LEFT, buff=0.7)

        real = MathTex(
            r"f(1.98,\ 1.03) = 1.98 \cdot (1.03)^2 = ",
            r"2.100582",
            font_size=31,
        )
        real[1].set_color(GREEN_B)
        real.next_to(real_label, DOWN, buff=0.12).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(real_label))
        self.play(Write(real))
        self.wait(0.5)

        error_label = Text("Error absoluto y relativo:", font_size=24, color=RED_B)
        error_label.next_to(real, DOWN, buff=0.3).to_edge(LEFT, buff=0.7)

        error = MathTex(
            r"E = |2.100582 - 2.10| = ",
            r"0.000582",
            r"\quad (\approx 0.0277\%)",
            font_size=30,
        )
        error[1].set_color(RED_B)
        error.next_to(error_label, DOWN, buff=0.12).to_edge(LEFT, buff=1.0)

        self.play(FadeIn(error_label))
        self.play(Write(error))
        self.wait(0.6)

        analisis_caja = Text(
            "Análisis de calidad:\n"
            "• Distancia en el dominio: Δr = √[(-0.02)² + (0.03)²] ≈ 0.036 unidades.\n"
            "• Al estar a centésimas del punto (2,1), los términos cuadráticos son minúsculos.\n"
            "• Conclusión: La aproximación es excelente localmente, pero degradará si Δr crece.",
            font_size=20,
            color=WHITE,
            line_spacing=1.3,
        ).to_edge(DOWN, buff=0.35)
        caja_borde = SurroundingRectangle(analisis_caja, color=TEAL_C, buff=0.15, corner_radius=0.1)

        self.play(Create(caja_borde), FadeIn(analisis_caja, shift=UP * 0.1))
        self.wait(3.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 6 — Demostración de la Curvatura del Error (Diagramación Limpia)
# ════════════════════════════════════════════════════════════════════════════
class Escena06CurvaturaError(MovingCameraScene):
    """
    Muestra en un plano 2D la brecha entre f(2,y)=2y² y L(2,y)=4y-2.
    Ejes desplazados hacia abajo para dar 1.5 unidades de margen superior libre.
    """
    def construct(self):
        # ── 1. Encabezado limpio ──────────────────────────────────────────
        titulo = Text("Geometría y Curvatura del Error", font_size=34, color=TEAL)
        titulo.to_edge(UP, buff=0.25)
        sep = Line(LEFT * 6.3, RIGHT * 6.3, color=TEAL, stroke_width=1)
        sep.next_to(titulo, DOWN, buff=0.1)
        self.add(titulo, sep)

        # ── 2. Ejes 2D desplazados hacia abajo (evita chocar arriba) ──────
        ejes_2d = Axes(
            x_range=[0.4, 1.6, 0.2],
            y_range=[0, 4.5, 1],
            x_length=7.4,
            y_length=3.2,
            axis_config={"color": GRAY_C, "include_tip": True},
        ).move_to(DOWN * 0.8 + RIGHT * 0.4)

        # Etiquetas de ejes con buff holgado fuera de las flechas
        x_label = MathTex("y", font_size=24, color=WHITE).next_to(ejes_2d.x_axis.get_end(), RIGHT, buff=0.25)
        z_label = MathTex("z", font_size=24, color=WHITE).next_to(ejes_2d.y_axis.get_end(), UP, buff=0.25)
        labels_2d = VGroup(x_label, z_label)

        # ── 3. Curva f(2,y) y Recta L(2,y) ─────────────────────────────────
        curva_f = ejes_2d.plot(lambda y: 2 * y**2, x_range=[0.45, 1.55], color=GREEN_B, stroke_width=4)
        recta_L = ejes_2d.plot(lambda y: 4 * y - 2, x_range=[0.45, 1.55], color=YELLOW, stroke_width=4)

        # Punto P(2,1,2)
        pt_tangencia = Dot(ejes_2d.c2p(1.0, 2.0), radius=0.075, color=RED)
        lbl_p = MathTex(r"P(2,1,2)", font_size=20, color=RED)
        lbl_p.next_to(pt_tangencia, DOWN + LEFT, buff=0.1)

        # ── 4. Tarjeta HUD de Leyenda (Ubicada en la franja superior izquierda)
        lbl_curva  = MathTex(r"\text{Superficie: } f(2,y) = 2y^2", font_size=18, color=GREEN_B)
        lbl_recta  = MathTex(r"\text{Plano: } L(2,y) = 4y - 2", font_size=18, color=YELLOW)
        lbl_brecha = MathTex(r"\text{Error: } E(y) = |f - L| = 2(y-1)^2", font_size=18, color=RED_B)

        panel_leyenda = VGroup(lbl_curva, lbl_recta, lbl_brecha).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        tarjeta_leyenda = crear_tarjeta_hud(panel_leyenda, color_borde=TEAL_C, buff=0.12, opacity=0.92)
        
        # Posicionada en la franja libre de arriba a la izquierda
        tarjeta_leyenda.next_to(sep, DOWN, buff=0.15).to_edge(LEFT, buff=0.5)

        # ── 5. Construcción animada ───────────────────────────────────────
        self.play(Create(ejes_2d), Write(labels_2d), run_time=1.0)
        self.play(Create(curva_f), Create(recta_L), FadeIn(pt_tangencia), Write(lbl_p), run_time=1.2)
        self.play(FadeIn(tarjeta_leyenda), run_time=0.8)
        self.wait(0.4)

        # ── 6. Área sombreada del error ───────────────────────────────────
        area_error = ejes_2d.get_area(
            curva_f,
            x_range=[0.45, 1.55],
            bounded_graph=recta_L,
            color=RED,
            opacity=0.3,
        )
        self.play(FadeIn(area_error), run_time=1.0)
        self.wait(0.6)

        # ── 7. Zoom Local Dinámico hacia P(2,1,2) ─────────────────────────
        # Ocultamos temporalmente la tarjeta principal para no estorbar el zoom
        self.play(FadeOut(tarjeta_leyenda), FadeOut(lbl_p), run_time=0.5)

        self.play(
            self.camera.frame.animate.scale(0.4).move_to(ejes_2d.c2p(1.0, 2.0)),
            run_time=2.2,
        )
        self.wait(0.4)

        # Elementos en primer plano durante el Zoom
        pt_eval = Dot(ejes_2d.c2p(1.03, 2 * (1.03)**2), radius=0.03, color=YELLOW)
        linea_error_local = Line(
            ejes_2d.c2p(1.03, 4 * 1.03 - 2),
            ejes_2d.c2p(1.03, 2 * (1.03)**2),
            color=RED_A,
            stroke_width=3.5,
        )

        lbl_eval_cercana = MathTex(
            r"y_0 = 1.03 \implies E \approx 0.000582", font_size=15, color=WHITE
        )
        tarjeta_local = crear_tarjeta_hud(lbl_eval_cercana, color_borde=YELLOW, buff=0.08, opacity=0.95)
        tarjeta_local.next_to(pt_eval, UR, buff=0.1)

        self.play(FadeIn(pt_eval), Create(linea_error_local), FadeIn(tarjeta_local), run_time=1.2)
        self.wait(1.8)

        # ── 8. Retorno a la vista general ─────────────────────────────────
        self.play(FadeOut(tarjeta_local), run_time=0.4)
        self.play(
            self.camera.frame.animate.scale(1 / 0.4).move_to(ORIGIN),
            run_time=2.0,
        )
        self.play(FadeIn(tarjeta_leyenda), FadeIn(lbl_p), run_time=0.6)
        self.wait(1.5)


# ════════════════════════════════════════════════════════════════════════════
# ESCENA 7 — Conclusión (Respuesta a la pregunta central)
# ════════════════════════════════════════════════════════════════════════════
class Escena07Conclusion(Scene):
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
            self.wait(1.2)

        self.wait(3)