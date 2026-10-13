# Desarrollo Matemático — Lista N.º 6

## Datos de la asignación

| Campo | Valor |
|-------|-------|
| Función | f(x, y) = xy² |
| Punto | (a, b) = (2, 1) |
| Valor a aproximar | f(1.98, 1.03) |

---

## 1. Función y punto de tangencia

f(x, y) = xy²

Punto asignado: (a, b) = (2, 1)

Evaluamos:
  f(2, 1) = 2 · 1² = 2

Punto en la superficie:
  P = (2, 1, 2)

---

## 2. Derivadas parciales

### Respecto a x
  fx(x, y) = ∂/∂x [xy²] = y²

Evaluando en (2, 1):
  fx(2, 1) = 1² = 1

**Interpretación geométrica:**
  La superficie sube 1 unidad en z por cada unidad que avancemos en la dirección x,
  al pasar por el punto P = (2, 1, 2).

### Respecto a y
  fy(x, y) = ∂/∂y [xy²] = 2xy

Evaluando en (2, 1):
  fy(2, 1) = 2 · 2 · 1 = 4

**Interpretación geométrica:**
  La superficie sube 4 unidades en z por cada unidad que avancemos en la dirección y,
  al pasar por el punto P = (2, 1, 2).
  La pendiente en dirección y es 4 veces mayor que en x.

---

## 3. Plano tangente en P = (2, 1, 2)

Fórmula general:
  z = f(a, b) + fx(a, b)·(x - a) + fy(a, b)·(y - b)

Sustituyendo:
  z = 2 + 1·(x - 2) + 4·(y - 1)
  z = 2 + x - 2 + 4y - 4
  z = x + 4y - 4

**Ecuación del plano tangente:**
  z = x + 4y - 4

---

## 4. Aproximación lineal L(x, y)

La función de aproximación lineal es la misma expresión del plano tangente,
entendida ahora como función de dos variables:

  L(x, y) = x + 4y - 4

Esta función nos permite aproximar:
  f(x, y) ≈ L(x, y)   para (x, y) cerca de (2, 1)

---

## 5. Estimación del valor asignado

Punto a aproximar: (x₀, y₀) = (1.98, 1.03)

Usamos la aproximación lineal:
  L(1.98, 1.03) = 1.98 + 4·(1.03) - 4
               = 1.98 + 4.12 - 4
               = 2.10

**Valor aproximado: f(1.98, 1.03) ≈ 2.10**

---

## 6. Valor real y análisis del error

Valor real (calculado directamente):
  f(1.98, 1.03) = 1.98 · (1.03)²
               = 1.98 · 1.0609
               ≈ 2.100582

Error absoluto:
  E = |f(1.98, 1.03) - L(1.98, 1.03)|
    = |2.100582 - 2.10|
    ≈ 0.000582

Error relativo:
  E_rel = 0.000582 / 2.100582 ≈ 0.0277 %

**Interpretación del error:**
  El error absoluto es de apenas 0.000582 unidades, lo que representa un error
  relativo de solo 0.0277%. Esta precisión tan alta se explica porque el punto
  (1.98, 1.03) está muy próximo al punto de tangencia (2, 1): la distancia
  entre ellos es solo √(0.02² + 0.03²) ≈ 0.036 unidades.

  Esto ilustra el carácter **local** de la aproximación lineal: funciona
  excelentemente cerca del punto de tangencia, pero la calidad de la aproximación
  se deteriora a medida que nos alejamos de él.

---

## Código LaTeX para el video (Overleaf)

### Fórmula del plano tangente

```latex
z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)
```

### Derivadas parciales

```latex
f_x(x,y) = y^2 \implies f_x(2,1) = 1
```

```latex
f_y(x,y) = 2xy \implies f_y(2,1) = 4
```

### Plano tangente del ejercicio

```latex
z = 2 + 1\cdot(x-2) + 4\cdot(y-1) = x + 4y - 4
```

### Aproximación lineal

```latex
L(x,y) = x + 4y - 4
```

### Estimación

```latex
L(1{,}98,\; 1{,}03) = 1{,}98 + 4(1{,}03) - 4 = \mathbf{2{,}10}
```

### Error

```latex
E = \left| f(1{,}98,\; 1{,}03) - L(1{,}98,\; 1{,}03) \right| \approx 0{,}000582
```

