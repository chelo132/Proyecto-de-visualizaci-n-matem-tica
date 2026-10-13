# 📐 Proyecto de Visualización Matemática — Plano Tangente y Aproximación Lineal

> **Cálculo Avanzado · Proyecto Individual · EID**  
> Video matemático animado con [Manim Community](https://www.manim.community/)

---

## 🎯 Asignación (N.º de lista: 6)

| Campo | Valor |
|-------|-------|
| **Función** | $f(x, y) = xy^2$ |
| **Punto de tangencia** | $(a, b) = (2,\ 1)$ |
| **Valor a aproximar** | $f(1.98,\ 1.03)$ |

---

## 📋 Descripción general

Este proyecto consiste en la creación de un video matemático animado que explora el concepto de **plano tangente** y su uso como **aproximación lineal** de una función de dos variables cerca de un punto dado.

La pregunta central que guía el desarrollo es:

> *¿Cómo podemos utilizar el plano tangente para aproximar el valor de una función de dos variables cerca de un punto conocido?*

---

## 🧮 Idea matemática principal

Dada una función de dos variables $z = f(x, y)$ y un punto $(a, b)$ en su dominio, si la función se comporta adecuadamente cerca de dicho punto, es posible aproximar sus valores mediante la **linearización**:

$$L(x, y) = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b)$$

Esta expresión corresponde al **plano tangente** a la superficie $z = f(x, y)$ en el punto $P = (a, b, f(a, b))$, y nos dice que:

$$f(x, y) \approx L(x, y) \quad \text{cuando } (x, y) \text{ está cerca de } (a, b)$$

---

## 🔢 Desarrollo matemático (Lista 6)

### 1. Función y punto

$$f(x, y) = xy^2 \qquad (a, b) = (2,\ 1)$$

$$f(2, 1) = 2 \cdot 1^2 = 2 \implies P = (2,\ 1,\ 2)$$

### 2. Derivadas parciales

$$f_x(x, y) = y^2 \implies f_x(2, 1) = 1^2 = 1$$

$$f_y(x, y) = 2xy \implies f_y(2, 1) = 2 \cdot 2 \cdot 1 = 4$$

> $f_x(2,1) = 1$ — La superficie sube 1 unidad por unidad avanzada en $x$ (pendiente en dirección $x$).  
> $f_y(2,1) = 4$ — La superficie sube 4 unidades por unidad avanzada en $y$ (pendiente en dirección $y$).

### 3. Plano tangente

$$z = f(2,1) + f_x(2,1)(x - 2) + f_y(2,1)(y - 1)$$

$$z = 2 + 1 \cdot (x - 2) + 4 \cdot (y - 1) = x + 4y - 4$$

### 4. Aproximación lineal

$$L(x, y) = x + 4y - 4$$

### 5. Estimación del valor asignado

$$L(1.98,\ 1.03) = 1.98 + 4(1.03) - 4 = \mathbf{2.10}$$

### 6. Valor real y error

$$f(1.98,\ 1.03) = 1.98 \cdot (1.03)^2 \approx 2.100582$$

$$E = |f(1.98,\ 1.03) - L(1.98,\ 1.03)| \approx \mathbf{0.000582}$$

> Error relativo ≈ 0.0277%. La aproximación es **muy precisa** porque $(1.98, 1.03)$ está muy cerca de $(2, 1)$, ilustrando el carácter **local** de la aproximación lineal.

---

## 📁 Estructura del proyecto

```
Proyecto-de-visualizacion-matematica/
│
├── EID_Calculo_Avanzado.pdf    # Enunciado oficial del proyecto
├── README.md                   # Este archivo
│
├── src/                        # Código fuente de las animaciones (Manim)
│   ├── main.py                 # Escena principal del video
│   ├── scene_01_intro.py       # Presentación de la función y el punto
│   ├── scene_02_derivadas.py   # Derivadas parciales
│   ├── scene_03_plano.py       # Construcción del plano tangente
│   ├── scene_04_aprox.py       # Aproximación lineal L(x, y)
│   ├── scene_05_estimacion.py  # Estimación del valor asignado
│   └── scene_06_error.py       # Análisis del error
│
├── media/                      # Archivos generados por Manim (auto)
│   └── videos/
│
├── assets/                     # Recursos adicionales (si aplica)
│
└── docs/                       # Notas y desarrollo matemático previo
    └── desarrollo_matematico.md
```

> ⚠️ La carpeta `media/` es generada automáticamente por Manim y **no se sube al repositorio**.

---

## 🎬 Estructura del video

El video tiene una duración de **4 a 6 minutos** con narración obligatoria, y sigue esta secuencia:

| # | Sección | Descripción |
|---|---------|-------------|
| 1 | **Presentación del problema** | Mostrar la función asignada, el punto $(a, b)$ y el valor a aproximar |
| 2 | **Derivadas parciales** | Calcular $f_x$ y $f_y$, evaluarlas en $(a, b)$ y explicar su significado geométrico |
| 3 | **Plano tangente** | Construir la ecuación del plano y mostrarlo junto a la superficie 3D |
| 4 | **Aproximación lineal** | Presentar $L(x, y)$ y su relación con el plano tangente |
| 5 | **Estimación** | Usar $L(x, y)$ para aproximar el valor asignado $(x_0, y_0)$ |
| 6 | **Comparación y error** | Calcular $f(x_0, y_0)$ real y el error absoluto $E = |f(x_0, y_0) - L(x_0, y_0)|$ |
| 7 | **Conclusión** | Responder la pregunta central del proyecto |

---

## 📊 Criterios de evaluación

| Criterio | Ponderación |
|----------|-------------|
| Corrección matemática | 25 % |
| Comprensión de la aproximación lineal | 25 % |
| Uso matemático de Manim | 20 % |
| Interpretación y análisis del error | 15 % |
| Comunicación y organización | 15 % |

---

## ⚙️ Tecnologías utilizadas

- **Python 3.x**
- **[Manim Community](https://www.manim.community/)** — Motor de animación matemática

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/<tu-usuario>/Proyecto-de-visualizacion-matematica.git
cd Proyecto-de-visualizacion-matematica
```

### 2. Instalar dependencias

Se recomienda usar un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
# venv\Scripts\activate        # Windows

pip install manim
```

### 3. Renderizar una escena

```bash
# Calidad baja (para desarrollo rápido)
manim -pql src/main.py NombreDeLaEscena

# Calidad alta (para entrega final)
manim -pqh src/main.py NombreDeLaEscena
```

---

## 📝 Información del proyecto

| Campo | Valor |
|-------|-------|
| Asignatura | Cálculo Avanzado |
| Modalidad | Individual |
| Ponderación | 8% de la nota final |
| Producto | Video matemático (Manim Community) |
| Duración | 4 a 6 minutos |
| Narración | Obligatoria |
| Tema | Plano tangente y aproximación lineal |

---

## 📌 Estado del proyecto

- [x] Desarrollo matemático previo (notas, cálculos y LaTeX en `docs/desarrollo_matematico.md`)
- [x] Setup del entorno Manim (entorno virtual + dependencias + LaTeX)
- [x] Escena 0: Introducción al problema y pregunta central
- [x] Escena 1: Presentación de la superficie 3D y punto $P=(2,1,2)$ con proyección
- [x] Escena 2: Derivadas parciales paso a paso e interpretación geométrica
- [x] Escena 3: Plano tangente 3D, curvas directrices, **zoom local obligatorio** y visualización de error
- [x] Escena 4: Deducción y construcción formal de la aproximación lineal $L(x,y)$
- [x] Escena 5: Estimación numérica $L(1.98, 1.03)$ y cálculo del error absoluto $E$
- [x] Escena 6: Conclusiones respondiendo a la pregunta central
- [x] Guion de narración escena por escena sincronizado (`docs/guion_narracion.md`)
- [ ] Grabación de la voz y ensamble del video final (4 a 6 min)
- [ ] Entrega final

