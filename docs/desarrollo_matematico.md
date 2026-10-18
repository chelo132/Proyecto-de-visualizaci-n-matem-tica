# 📐 Memoria de Desarrollo Matemático Riguroso
## Plano Tangente, Aproximación Lineal y Análisis del Error Local

> **Asignatura:** Cálculo Avanzado · Evaluación Individual de Desempeño (EID)  
> **Asignación Asignada:** Lista N.º 6  
> **Función:** $f(x, y) = xy^2$  
> **Punto base en el dominio:** $(a, b) = (2, 1)$  
> **Punto en la superficie 3D:** $P = (a, b, f(a, b)) = (2, 1, 2)$  
> **Punto cercano a evaluar:** $(x_0, y_0) = (1.98, 1.03)$  
> **Pregunta orientadora central:** *¿Cómo podemos utilizar el plano tangente para aproximar el valor de una función de dos variables cerca de un punto conocido?*  
> **Correspondencia con código:** Fundamenta las 11 escenas de [`src/main.py`](file:///src/main.py) y la clase `ProyectoCompleto`.

---

## 1. Identificación del Problema y Punto en la Superficie (Escenas 0 y 1)

Consideramos la función escalar de dos variables independientes $f: \mathbb{R}^2 \to \mathbb{R}$:
$$f(x, y) = xy^2$$

Dicha función describe una superficie suave en el espacio euclidiano tridimensional:
$$\mathcal{S} = \left\{ (x, y, z) \in \mathbb{R}^3 : z = f(x, y) = xy^2 \right\}$$

Evaluando en el punto base asignado $(a, b) = (2, 1)$:
$$f(2, 1) = 2 \cdot (1)^2 = 2$$

Por lo tanto, el punto tridimensional exacto sobre la superficie es:
$$P = (a, b, f(a, b)) = (2, 1, 2)$$

### Construcción progresiva hacia la pregunta central:
Evaluar $f(2, 1) = 2$ es una operación aritmética exacta y elemental. No obstante, al movernos a un punto decimal cercano como $(1.98, 1.03)$, calcular $1.98 \cdot (1.03)^2$ requiere multiplicaciones no lineales que resultan engorrosas sin calculadora.  
La aproximación lineal busca **sustituir localmente la superficie curva $z = xy^2$ por una variedad lineal plana afín** cuya evaluación dependa únicamente de sumas y productos ponderados por las pendientes directrices en dicho punto.

---

## 2. Derivadas Parciales y Geometría de las Secciones Transversales (Escenas 2 y 3)

Para determinar la orientación del plano tangente en $P(2, 1, 2)$, analizamos la razón de cambio instantánea de la cota $z$ en las dos direcciones ortogonales canónicas.

### 2.1. Derivada Parcial respecto a $x$ ($f_x$)
Para medir la variación en dirección del eje $x$, se interseca la superficie $z = xy^2$ con el plano vertical $y = 1$ (**se mantiene la variable $y$ estrictamente constante como el parámetro numérico 1**):
$$C_1: \begin{cases} z = f(x, 1) = x \cdot (1)^2 = x \\ y = 1 \end{cases}$$

Calculamos la derivada ordinaria de esta curva paramétrica:
$$f_x(x, y) = \frac{\partial}{\partial x}[xy^2] = y^2 \cdot \frac{d}{dx}[x] = y^2 \cdot 1 = y^2$$

Evaluando en $(a, b) = (2, 1)$:
$$f_x(2, 1) = (1)^2 = \mathbf{1}$$

**Significado Geométrico y Vector Tangente Director:**  
La curva de corte $C_1$ es una recta en el espacio cuya pendiente en dirección $x$ es $m_x = 1$. Su vector director tangente en $\mathbb{R}^3$ es:
$$\vec{u} = \left\langle 1, \, 0, \, f_x(2, 1) \right\rangle = \langle 1, 0, 1 \rangle$$
*Interpretación:* Por cada unidad que nos desplazamos en $+x$, la superficie se eleva instantáneamente $1$ unidad en $+z$.

---

### 2.2. Derivada Parcial respecto a $y$ ($f_y$)
Para medir la variación en dirección del eje $y$, intersecamos la superficie con el plano vertical $x = 2$ (**se mantiene la variable $x$ estrictamente constante como el parámetro numérico 2**):
$$C_2: \begin{cases} z = f(2, y) = 2 \cdot y^2 = 2y^2 \\ x = 2 \end{cases}$$

Derivamos respecto a $y$ tratando a $x$ como constante multiplicativa:
$$f_y(x, y) = \frac{\partial}{\partial y}[xy^2] = x \cdot \frac{d}{dy}[y^2] = x \cdot (2y) = 2xy$$

Evaluando en $(a, b) = (2, 1)$:
$$f_y(2, 1) = 2(2)(1) = \mathbf{4}$$

**Significado Geométrico y Vector Tangente Director:**  
La curva de corte $C_2$ es una parábola vertical con vértice en el origen. Su recta tangente en $y = 1$ tiene pendiente $m_y = 4$. Su vector director tangente en $\mathbb{R}^3$ es:
$$\vec{v} = \left\langle 0, \, 1, \, f_y(2, 1) \right\rangle = \langle 0, 1, 4 \rangle$$
*Interpretación:* Por cada unidad que nos desplazamos en $+y$, la altura se incrementa a razón de $4$ unidades en $+z$ (una inclinación cuatro veces mayor que en $x$).

---

## 3. Construcción Analítica y Espacial del Plano Tangente (Escenas 4 y 5)

Dos vectores directores no paralelos tangentes a la superficie en un punto común generan de manera única el plano tangente.

### 3.1. Obtención del Vector Normal $\vec{n}$
El vector ortogonal al plano se deduce mediante el producto vectorial de $\vec{u}$ y $\vec{v}$:
$$\vec{n} = \vec{u} \times \vec{v} = \det \begin{pmatrix} \hat{i} & \hat{j} & \hat{k} \\ 1 & 0 & 1 \\ 0 & 1 & 4 \end{pmatrix} = \hat{i}(0 - 1) - \hat{j}(4 - 0) + \hat{k}(1 - 0) = \langle -1, -4, 1 \rangle$$

En general: $\vec{n} = \langle -f_x(a,b), \, -f_y(a,b), \, 1 \rangle$.

### 3.2. Ecuación Cartesiana del Plano Tangente
Cualquier punto $(x, y, z)$ perteneciente al plano satisface la condición de ortogonalidad $\vec{n} \cdot \left( \langle x, y, z \rangle - P \right) = 0$:
$$-f_x(a, b)(x - a) - f_y(a, b)(y - b) + 1 \cdot (z - f(a, b)) = 0$$

Despejando explícitamente $z$:
$$z = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b)$$

Sustituyendo los valores numéricos correspondientes al punto $(2, 1)$:
$$z = 2 + 1 \cdot (x - 2) + 4 \cdot (y - 1)$$
$$z = 2 + x - 2 + 4y - 4$$
$$\mathbf{z = x + 4y - 4}$$

### 3.3. Principio de Aplanamiento Local (*Local Flatness*)
Al realizar un acercamiento profundo (*zoom in*) con la cámara hacia el punto $P(2, 1, 2)$, la curvatura de la superficie $z = xy^2$ se atenúa progresivamente hasta volverse imperceptible. A escala infinitesimal, **la superficie y el plano tangente coinciden espacialmente**.

---

## 4. La Aproximación Lineal $L(x, y)$ y Diferenciabilidad (Escena 6)

Definimos la función de aproximación lineal (o linearización) de $f$ en $(a, b)$ como la función escalar cuya gráfica coincide con el plano tangente:
$$L(x, y) = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b)$$
$$\mathbf{L(x, y) = x + 4y - 4}$$

### ¿Por qué $L(x, y)$ aproxima a $f(x, y)$ cerca de $(a, b)$?
Por la definición formal de **diferenciabilidad**: una función $f$ es diferenciable en $(a, b)$ si y solo si el incremento real $\Delta z = f(a + \Delta x, b + \Delta y) - f(a, b)$ admite la descomposición:
$$\Delta z = f_x(a, b)\Delta x + f_y(a, b)\Delta y + \varepsilon_1 \Delta x + \varepsilon_2 \Delta y$$
donde los residuos satisfacen $\varepsilon_1, \varepsilon_2 \to 0$ cuando $(\Delta x, \Delta y) \to (0, 0)$.

Reordenando términos:
$$f(a + \Delta x, b + \Delta y) = \underbrace{f(a, b) + f_x(a, b)\Delta x + f_y(a, b)\Delta y}_{L(x, y)} + \mathcal{R}(\Delta x, \Delta y)$$

Por consiguiente:
$$f(x, y) \approx L(x, y) \quad \text{cuando } (x, y) \to (a, b)$$

---

## 5. Estimación Numérica del Valor Asignado (Escenas 7 y 8)

Se nos solicita aproximar el valor de la función en $(x_0, y_0) = (1.98, 1.03)$.

### 5.1. Desglose de Incrementos y Distancia en el Dominio
Definimos las desviaciones respecto al punto de tangencia $(a, b) = (2, 1)$:
$$\Delta x = x_0 - a = 1.98 - 2.00 = \mathbf{-0.02}$$
$$\Delta y = y_0 - b = 1.03 - 1.00 = \mathbf{+0.03}$$

La distancia euclidiana en el plano coordenado es:
$$\Delta r = \sqrt{(\Delta x)^2 + (\Delta y)^2} = \sqrt{(-0.02)^2 + (0.03)^2} = \sqrt{0.0004 + 0.0009} = \sqrt{0.0013} \approx \mathbf{0.0360555\text{ unidades}}$$

### 5.2. Evaluación en la Aproximación Lineal
Calculamos el diferencial total:
$$dz = f_x(2, 1)\Delta x + f_y(2, 1)\Delta y = 1 \cdot (-0.02) + 4 \cdot (+0.03) = -0.02 + 0.12 = \mathbf{+0.10}$$

Por tanto:
$$L(1.98, 1.03) = f(2, 1) + dz = 2.00 + 0.10 = \mathbf{2.100000}$$

Verificación mediante la expresión simplificada:
$$L(1.98, 1.03) = 1.98 + 4(1.03) - 4 = 1.98 + 4.12 - 4 = \mathbf{2.100000}$$

### 5.3. Valor Real Exacto
Evaluando directamente en la función no lineal:
$$f(1.98, 1.03) = 1.98 \cdot (1.03)^2$$
$$(1.03)^2 = (1 + 0.03)^2 = 1 + 2(0.03) + (0.03)^2 = 1.0609$$
$$f(1.98, 1.03) = 1.98 \cdot 1.0609 = (2 - 0.02) \cdot 1.0609 = 2.1218 - 0.021218 = \mathbf{2.100582}$$

### 5.4. Error Absoluto y Relativo
$$E = |f(1.98, 1.03) - L(1.98, 1.03)| = |2.100582 - 2.100000| = \mathbf{0.000582}$$

Error porcentual relativo:
$$E_{\text{rel}} = \frac{E}{f(1.98, 1.03)} \times 100\% = \frac{0.000582}{2.100582} \times 100\% \approx \mathbf{0.027706\%}$$

---

## 6. Sustento Teórico del Error Mediante la Serie de Taylor Bivariada (Escena 9)

En la `Escena09CurvaturaError` se analiza la sección transversal bidimensional en el plano $x=2$:
$$f(2, y) = 2y^2, \qquad L(2, y) = 2 + 4(y - 1) = 4y - 2$$
La brecha vertical de error unidimensional es:
$$E(y) = |f(2, y) - L(2, y)| = |2y^2 - (4y - 2)| = 2|y^2 - 2y + 1| = \mathbf{2(y - 1)^2}$$

Generalizando a dos variables mediante la **Serie de Taylor de segundo orden** alrededor de $(a, b) = (2, 1)$:
$$f(a + \Delta x, b + \Delta y) = f(a, b) + \left( f_x \Delta x + f_y \Delta y \right) + \frac{1}{2!} \left( f_{xx}(\Delta x)^2 + 2f_{xy}\Delta x \Delta y + f_{yy}(\Delta y)^2 \right) + \mathcal{R}_2$$

Calculamos las derivadas parciales de segundo orden para $f(x, y) = xy^2$:
- $f_{xx}(x, y) = \frac{\partial}{\partial x}[y^2] = 0 \implies f_{xx}(2, 1) = 0$
- $f_{xy}(x, y) = \frac{\partial}{\partial y}[y^2] = 2y \implies f_{xy}(2, 1) = 2(1) = 2$
- $f_{yy}(x, y) = \frac{\partial}{\partial y}[2xy] = 2x \implies f_{yy}(2, 1) = 2(2) = 4$

Dado que las derivadas de tercer orden con respecto a $x$ son nulas y solo $f_{xyy} = 2$ subsiste, la expansión exacta del error es:
$$f(x_0, y_0) - L(x_0, y_0) = \frac{1}{2}\left[ 0 \cdot (\Delta x)^2 + 2(2)\Delta x \Delta y + 4(\Delta y)^2 \right] + \frac{1}{6}\left[ 3 \cdot 2 \Delta x (\Delta y)^2 \right]$$

$$f(x_0, y_0) - L(x_0, y_0) = 2\Delta x \Delta y + 2(\Delta y)^2 + \Delta x (\Delta y)^2$$

Evaluando término a término con $\Delta x = -0.02$ y $\Delta y = +0.03$:
1. $2\Delta x \Delta y = 2(-0.02)(+0.03) = -0.0012$
2. $2(\Delta y)^2 = 2(0.03)^2 = 2(0.0009) = +0.0018$
3. Término de segundo orden neto: $-0.0012 + 0.0018 = \mathbf{+0.000600}$
4. Término cúbico de orden superior: $\Delta x (\Delta y)^2 = (-0.02)(0.0009) = \mathbf{-0.000018}$

Sumando con total precisión analítica:
$$\text{Diferencia teórica exacta} = +0.000600 - 0.000018 = \mathbf{0.000582}$$

$$\mathbf{E = |f(1.98, 1.03) - L(1.98, 1.03)| = 0.000582}$$

### Justificación del comportamiento $\mathcal{O}((\Delta r)^2)$:
- El error está dominado por la forma cuadrática del Hessiano:
  $$E \le \frac{1}{2} M (\Delta r)^2 = \mathcal{O}((\Delta r)^2)$$
- Debido a que $\Delta r \approx 0.036$, su cuadrado es $(\Delta r)^2 \approx 0.0013$. Al elevar centésimas al cuadrado, **el término cuadrático amortigua el residuo a magnitudes de diezmilésimas**.
- Esto demuestra formalmente por qué la aproximación lineal es extraordinariamente precisa en una vecindad infinitesimal del punto de tangencia, pero pierde fiabilidad rápidamente si nos alejamos hacia zonas donde $(\Delta r)^2$ se vuelve significativo.

---

## 7. Síntesis y Respuesta Definitiva a la Pregunta Central (Escena 10)

> **Pregunta:** *¿Cómo podemos utilizar el plano tangente para aproximar el valor de una función de dos variables cerca de un punto conocido?*

1. **Principio Geométrico de Aplanamiento Local:**  
   Toda superficie diferenciable en $\mathbb{R}^3$ es suave y carece de vértices angulosos; en una vecindad microscópica alrededor de cualquier punto $P(a, b, f(a,b))$, la curvatura se extingue visualmente y la superficie es indistinguible de su plano tangente afín generado por las direcciones tangentes $\vec{u}$ y $\vec{v}$.
2. **Linearización Operativa:**  
   Sustituimos el modelo no lineal cuadrático $z = xy^2$ por una variedad lineal de primer grado $L(x, y) = x + 4y - 4$. Esto permite evaluar alturas y hacer estimaciones inmediatas mediante operaciones aritméticas elementales.
3. **Control del Error y Carácter Local:**  
   El plano tangente es confiable **únicamente de forma local**. Gracias a que el error cometido es de orden cuadrático $\mathcal{O}((\Delta r)^2)$, al mantener $(\Delta x, \Delta y)$ en magnitudes centesimales garantizamos precisiones extremas (como el margen de error comprobado del $0.0277\%$).
