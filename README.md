# 📐 Proyecto de Visualización Matemática — Plano Tangente y Aproximación Lineal

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Manim-Community%20v0.18%2B-red?logo=manim" alt="Manim Community">
  <img src="https://img.shields.io/badge/C%C3%A1lculo-Avanzado-teal" alt="Cálculo Avanzado">
  <img src="https://img.shields.io/badge/Licencia-Educativa-green" alt="Licencia">
</p>

> **Cálculo Avanzado · Evaluación Individual de Desempeño (EID)**  
> Animación matemática formal desarrollada con **[Manim Community](https://www.manim.community/)**.

---

## 🎯 Asignación (Lista N.º 6)

| Parámetro | Notación | Valor Asignado |
| :--- | :---: | :--- |
| **Función escalar de dos variables** | $z = f(x, y)$ | $f(x, y) = xy^2$ |
| **Punto base en el dominio** | $(a, b)$ | $(2,\ 1)$ |
| **Punto de anclaje en el espacio 3D** | $P = (a, b, f(a,b))$ | $P = (2,\ 1,\ 2)$ |
| **Punto cercano a evaluar** | $(x_0, y_0)$ | $(1.98,\ 1.03)$ |
| **Incrementos respecto a $(a, b)$** | $(\Delta x, \Delta y)$ | $\Delta x = -0.02, \quad \Delta y = +0.03$ |
| **Distancia euclidiana local** | $\Delta r = \sqrt{(\Delta x)^2 + (\Delta y)^2}$ | $\Delta r \approx 0.03606\text{ unidades}$ |

---

## 📋 Pregunta Central del Proyecto

> *¿Cómo podemos utilizar el plano tangente para aproximar el valor de una función de dos variables cerca de un punto conocido?*

Este proyecto responde dicha pregunta integrando tres dimensiones de análisis:
1. **Geométrica (Aplanamiento local):** En un entorno infinitesimal alrededor de $P$, una superficie suave carece de aristas y se confunde visualmente con su plano tangente afín (*local flatness*).
2. **Algebraica (Linearización operativa):** Sustituye el cálculo no lineal de potencias $z = xy^2$ por una combinación lineal inmediata de evaluar $L(x, y) = x + 4y - 4$.
3. **Analítica (Control del residuo):** Mediante la Serie de Taylor multivariable, se comprueba que el error absoluto $E = |f - L|$ es de orden cuadrático $\mathcal{O}((\Delta r)^2)$, garantizando precisión submilenaria en las cercanías del punto de tangencia.

---

## 🔢 Resumen del Desarrollo Analítico

### 1. Punto de tangencia y evaluación de altura
$$f(2, 1) = 2 \cdot (1)^2 = 2 \implies P(2, 1, 2)$$

### 2. Derivadas parciales y vectores directores
* **Dirección $x$ ($y=1$ constante):**
  $$f_x(x, y) = \frac{\partial}{\partial x}(xy^2) = y^2 \implies f_x(2, 1) = 1$$
  Vector director tangente: $\vec{u} = \langle 1, 0, f_x(2,1) \rangle = \langle 1, 0, 1 \rangle$.
* **Dirección $y$ ($x=2$ constante):**
  $$f_y(x, y) = \frac{\partial}{\partial y}(xy^2) = 2xy \implies f_y(2, 1) = 2(2)(1) = 4$$
  Vector director tangente: $\vec{v} = \langle 0, 1, f_y(2,1) \rangle = \langle 0, 1, 4 \rangle$.

### 3. Ecuación del plano tangente
Vector normal mediante producto vectorial:
$$\vec{n} = \vec{u} \times \vec{v} = \det \begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 0 & 1 \\ 0 & 1 & 4 \end{pmatrix} = \langle -1, -4, 1 \rangle$$

$$z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b) = 2 + 1(x - 2) + 4(y - 1) \implies \mathbf{z = x + 4y - 4}$$

### 4. Aproximación lineal y comparación numérica
* **Función lineal:** $\mathbf{L(x, y) = x + 4y - 4}$
* **Estimación lineal:** $L(1.98, 1.03) = 1.98 + 4(1.03) - 4 = \mathbf{2.100000}$
* **Valor real exacto:** $f(1.98, 1.03) = 1.98 \cdot (1.03)^2 = \mathbf{2.100582}$
* **Error absoluto:** $E = |2.100582 - 2.100000| = \mathbf{0.000582}$
* **Error relativo porcentual:** $E_{\text{rel}} \approx \mathbf{0.0277\%}$ (precisión del $99.9723\%$)

---

## 📁 Estructura del Repositorio

El repositorio mantiene una estructura limpia, separando el código fuente de los documentos académicos y los archivos binarios autogenerados:

```
Proyecto-de-visualizacion-matematica/
│
├── .gitignore                  # Reglas de exclusión para Git (media, venv, caches)
├── README.md                   # Documentación principal del repositorio en GitHub
├── EID_Calculo_Avanzado.pdf    # Pauta oficial de la Evaluación Individual de Desempeño
│
├── src/                        # Código fuente de Manim Community
│   └── main.py                 # Script modular con 11 escenas y la clase ProyectoCompleto
│
├── docs/                       # Documentación complementaria y guiones
│   ├── desarrollo_matematico.md # Memoria de cálculo formal (Taylor, derivadas, error)
│   └── guion_narracion.md      # Guion de narración oral sincronizado a 6 minutos
│
└── media/                      # [IGNORADO EN GIT] Renders de video generados localmente
    └── videos/                 # Salida generada por los comandos de Manim
```

> [!NOTE]
> La carpeta `media/` y los entornos virtuales (`venv/`) están excluidos en `.gitignore` para mantener el repositorio ligero y libre de binarios temporales o videos pesados de renderizado.

---

## 🎬 Arquitectura de Escenas en `src/main.py`

El video completo dura **~6 minutos** con narración oral continua y está estructurado en 11 escenas modulares, más una clase unificada:

| # | Clase en Manim | Vista | Concepto Matemático y Visual | Duración Guion |
| :---: | :--- | :---: | :--- | :---: |
| **0** | `Escena00Introduccion` | 2D | Título, datos de la función $f(x,y)=xy^2$ y pregunta central | ~35 s |
| **1** | `Escena01Superficie` | 3D | Proyección basal $(2,1,0) \to P(2,1,2)$ y superficie $z=xy^2$ | ~35 s |
| **2** | `Escena02DerivadasParciales` | 2D | Cálculo de $f_x=1$ e $f_y=4$ tratando variables como constantes | ~35 s |
| **3** | `Escena03GraficaDerivadas3D` | 3D | Cortes ortogonales $x=2, y=1$ y vectores tangentes $\vec{u}, \vec{v}$ | ~35 s |
| **4** | `Escena04ConstruccionEcuacionPlano` | 2D | Deducción cartesiana paso a paso: $z = x + 4y - 4$ | ~35 s |
| **5** | `Escena05GraficaPlanoTangente3D` | 3D | Plano tangente 3D y zoom de aplanamiento local (*local flatness*) | ~40 s |
| **6** | `Escena06Aproximacion` | 2D | Formalización de $L(x,y)$ y justificación por diferenciabilidad | ~30 s |
| **7** | `Escena07EstimacionComparacion` | 2D | Estimación $L=2.10$, valor real $f=2.100582$ y cálculo del error | ~35 s |
| **8** | `Escena08VisualizacionAproximacion3D` | 3D | Punto real vs aproximado en la superficie y plano 3D | ~30 s |
| **9** | `Escena09CurvaturaError` | 2D/3D | Corte transversal 2D, parábola, recta tangente y área de error | ~35 s |
| **10** | `Escena10Conclusion` | 2D | Respuesta integral y fundamentada a la pregunta central | ~35 s |
| **—** | `ProyectoCompleto` | Master | **Ensamble continuo y secuencial de las 11 escenas en un solo video** | **~6:00 min** |

---


## 🚀 Instalación y Reproducción Local

### 1. Requisitos previos
- **Python 3.10 o superior**
- **FFmpeg** instalado en el sistema (`sudo apt install ffmpeg` en Ubuntu/Debian)
- Compilador LaTeX (opcional si usas Manim sin textos complejos de LaTeX, o `texlive-latex-extra`)

### 2. Clonar y preparar el entorno
```bash
# Clonar el repositorio
git clone https://github.com/Chelo-prog/Proyecto-de-visualizaci-n-matem-tica.git
cd Proyecto-de-visualizaci-n-matem-tica

# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate       # Linux / macOS
# venv\Scripts\activate        # Windows

# Instalar dependencias
pip install manim
```

### 3. Renderizar escenas individuales (Previsualización rápida)
```bash
# Modo rápido a 480p y 15 fps (-ql)
manim -pql src/main.py Escena00Introduccion
manim -pql src/main.py Escena03GraficaDerivadas3D
manim -pql src/main.py Escena05GraficaPlanoTangente3D
manim -pql src/main.py Escena09CurvaturaError
```

### 4. Renderizar el video continuo completo
```bash
# Calidad baja para revisión de tiempos y audio (480p 15fps)
manim -pql src/main.py ProyectoCompleto

# Calidad de entrega final en alta definición (1080p 60fps)
manim -pqh src/main.py ProyectoCompleto
```

---

## 📊 Rúbrica de Evaluación

| Criterio | Ponderación | Aspectos Evaluados |
| :--- | :---: | :--- |
| **Corrección matemática** | 25 % | Rigor en derivadas parciales, plano tangente, linealización y error. |
| **Comprensión de la aproximación lineal** | 25 % | Fundamentación teórica de $L(x,y)$, aplanamiento local y Taylor. |
| **Uso matemático de Manim** | 20 % | Animaciones 3D, cortes ortogonales, vectores y zoom explicativo. |
| **Interpretación y análisis del error** | 15 % | Análisis de la vecindad local $\Delta r$, error absoluto y relativo. |
| **Comunicación y organización** | 15 % | Sincronización con el guion de narración oral y coherencia visual. |
| **Total** | **100 %** | **Ponderación: 8% de la calificación final** |

---

## 📌 Estado de Avance

- [x] Memoria analítica rigurosa finalizada ([`docs/desarrollo_matematico.md`](file:///docs/desarrollo_matematico.md))
- [x] Configuración de entorno y depuración de sintaxis en Manim Community
- [x] 11 escenas modulares implementadas y probadas en [`src/main.py`](file:///src/main.py)
- [x] Clase unificada `ProyectoCompleto` para renderizado continuo
- [x] Guion sincronizado de 6 minutos completado ([`docs/guion_narracion.md`](file:///docs/guion_narracion.md))
- [x] Configuración de [`.gitignore`](file:///.gitignore) para exclusión de artefactos pesados (`media/`)
- [ ] Grabación final de locución oral y entrega

---

## 📌 Estado de Avance

- [x] Memoria analítica rigurosa finalizada ([`docs/desarrollo_matematico.md`](file:///docs/desarrollo_matematico.md))
- [x] Configuración de entorno y depuración de sintaxis en Manim Community
- [x] 11 escenas modulares implementadas y probadas en [`src/main.py`](file:///src/main.py)
- [x] Clase unificada `ProyectoCompleto` para renderizado continuo
- [x] Guion sincronizado de 6 minutos completado ([`docs/guion_narracion.md`](file:///docs/guion_narracion.md))
- [x] Configuración de [`.gitignore`](file:///.gitignore) para exclusión de artefactos pesados (`media/`)
- [ ] Grabación final de locución oral y entrega

