# Apuntes Python - Su 🐍

# TODO: Cosas por hacer
# NOTE: Anotaciones
# FIXME: Lanza error
# BUG: Errores confirmados
# HACK: Soluciones rapidas
# XXX: Revisar esta parte

--------------------------------------------------------------------
## Indice
1. [Tipos de datos built-in](#tipos-de-datos-built-in)
2. [Mutabilidad de colecciones](#mutabilidad-de-colecciones)
3. [Operaciones comunes y conversiones](#operaciones-comunes-y-conversiones)
4. [`str()` vs `repr()`](#str-vs-repr)
5. [Tipos numéricos](#tipos-numéricos)
6. [Operaciones básicas](#operaciones-básicas)
7. [Funciones útiles para `int` y `float`](#funciones-útiles-para-int-y-float)
8. [Comparadores](#comparadores)
9. [Booleanos y operadores lógicos](#booleanos-y-operadores-lógicos)
10. [Evaluación de verdad (Truth Value Testing)](#evaluación-de-verdad-truth-value-testing)
11. [Métodos Adicionales del Tipo `int` en Python](#métodos-adicionales-del-tipo-int-en-Python)


## Tipos de datos built-in

- `'int', 'float', 'complex'`: Números  
- `'str', 'list', 'tuple', 'range'`: Secuencias ordenadas  
- `'dict'`: Diccionarios (clave-valor)  
- `'bool'`: Verdadero / falso  
- `'None'`: Ausencia de valor  
- `'exception'`: Tipos de error (ValueError, IndexError...)  
- `'class'`, `'instance'`: Tipos definidos por el usuario  

------------------------------------------------------------------------
## Mutabilidad de colecciones

Algunas estructuras como listas o diccionarios **se pueden modificar directamente** (son mutables). 

Cuando se usa un método como .append() o .sort()
- Modifican la colección
- No devuelven nada (retornan None)

### Ejemplo:

lista = [3, 1, 2]
resultado = lista.sort()

print(lista)      # [1, 2, 3]
print(resultado)  # None

## Operaciones comunes y conversiones

- Comparar: `==`, `!=`  
- Convertir: `str()`, `repr()`  
- Mostrar: `print()`  

### Ejemplo:
nombre = "Zulhei"
print(nombre == "Zulhei")  # True
print(str(25))             # "25"
print(repr(3.14))          # '3.14'

--------------------------------------------------
## `str()` vs `repr()`

| Función  | Propósito                          | Ejemplo                  |
|----------|------------------------------------|--------------------------|
| `str()`  | Legible para humanos               | `str("hola") → "hola"`   |
| `repr()` | Representación exacta para código  | `repr("hola") → "'hola'"`|

texto = "Hola Zulhei"

print(str(texto))   # Hola Zulhei
print(repr(texto))  # 'Hola Zulhei'

- repr() muestra las comillas para dejar claro que es un string. str() no-
----------------------------------------------------------------------------
## Tipos numéricos

- `int`: Números enteros (`1`, `0`, `-7`)  
- `float`: Números con decimales (`3.14`, `-1.0`)  
- `complex`: Números con parte real e imaginaria (`2 + 3j`)

### `int` (Enteros)
- Son números **sin punto decimal**.
- Se usan para contar: 1, 2, 3...
- También pueden ser negativos o cero.

### `float` (Punto Flotante)
- Son números reales con parte decimal.

### `complex` (Complejos)
- Son números con parte real e imaginaria.

- Lo que me explico uwu
x = 5 
y = 3.14 
z = 2 + 3j 

print(type(x))
print(type(y).__name__)
print(type(z))

def f(n):
    return 2 * n

class Persona:
    def __init__(self):
        self.nombre = "Zulhei"
        self.edad = 27

print(Persona.__name__)

x = 5        # int
y = 3.14     # float
z = 2 + 3j   # complex

print(type(x))  # 'int'
print(type(y))  # 'float'
print(type(z))  # 'complex'

--------------------------------------------

## Operaciones básicas

| Operación         | Resultado                          | Ejemplo                       |
|------------------|-------------------------------------|-------------------------------|
| `x + y`          | Suma                                | `3 + 2 → 5`                   |
| `x - y`          | Resta                               | `5 - 1 → 4`                   |
| `x * y`          | Multiplicación                      | `4 * 2 → 8`                   |
| `x / y`          | División decimal                    | `7 / 2 → 3.5`                 |
| `x // y`         | División entera                     | `7 // 2 → 3`                  |
| `x % y`          | Módulo (residuo)                    | `7 % 2 → 1`                   |
| `-x`             | Número negado                       | `-5 → -5`                     |
| `+x`             | Igual que x                         | `+3 → 3`                      |
| `abs(x)`         | Valor absoluto                      | `abs(-4) → 4`                 |
| `int(x)`         | Convertir a entero                  | `int(3.9) → 3`                |
| `float(x)`       | Convertir a decimal                 | `float(5) → 5.0`              |
| `complex(x, y)`  | Crear número complejo               | `complex(2, 3) → 2+3j`        |
| `x.conjugate()`  | Conjugado complejo                  | `(2+3j).conjugate() → 2-3j`   |
| `divmod(x, y)`   | Retorna `(x // y, x % y)`           | `divmod(9, 4) → (2, 1)`       |
| `pow(x, y)`      | Potencia (función)                  | `pow(2, 3) → 8`               |
| `x ** y`         | Potencia (operador)                 | `2 ** 3 → 8`                  |


### División entera (`//`)
- Si ambos operandos son `int`, el resultado es `int`.
- Si alguno es `float`, el resultado es `float`.
- **Siempre redondea hacia abajo (hacia el menos infinito)**.

### Suma, Resta, Multiplicación y División
 - La división con / siempre da un número tipo float, incluso si es exacta.

### `x % y` → Módulo o residuo
- Devuelve **lo que sobra** al dividir `x` entre `y`.
- Sirve para saber si un número es par, impar, múltiplo, etc.

### -x → Número negado
- Cambia el signo de un número. Si era positivo, se vuelve negativo (y viceversa).

### +x → Número sin cambios
- No cambia el valor. Es como decir “déjalo tal como está”.

### abs(x) → Valor absoluto
- Devuelve el número sin signo. 
- Siempre positivo.

### int(x) → Convierte a entero
- Trunca los decimales. No redondea, solo corta lo decimal.

### float(x) → Convierte a decimal
- Convierte un entero a número con punto decimal.

### complex(re, im) → Número complejo
- Crea un número con parte real (re) y parte imaginaria (im).

### c.conjugate() → Conjugado complejo
- Cambia el signo de la parte imaginaria del número complejo.

### divmod(x, y) → División con cociente y resto
- Devuelve una tupla: (x // y, x % y)

### pow(x, y) → Potencia (función)
- Eleva x a la y (como x ** y, pero en forma de función).

### x ** y → Potencia (operador)
- Forma más común de hacer potencias.


## Funciones útiles para `int` y `float`

| Función              | Descripción                                                        |
|----------------------|--------------------------------------------------------------------|
| `math.trunc(x)`      | Trunca (corta) los decimales. No redondea.                         |
| `round(x[, n])`      | Redondea a `n` dígitos. Si no se indica `n`, redondea a entero.    |
| `math.floor(x)`      | Redondea hacia abajo (el entero menor o igual a `x`).              |
| `math.ceil(x)`       | Redondea hacia arriba (el entero mayor o igual a `x`).             |

### División entera (`//`)
- Si ambos operandos son `int`, el resultado es `int`.
- Si alguno es `float`, el resultado es `float`.
- **Siempre redondea hacia abajo (hacia el menos infinito)**.

### Números complejos
- Estas operaciones **no funcionan** con números complejos.
- Puedes usar `abs()` si necesita el valor absoluto.

### Conversión `float` → `int`
- Trunca (corta) los decimales, **no redondea**.

- Para redondear correctamente:
- `math.floor(x)` → redondea hacia abajo.
- `math.ceil(x)` → redondea hacia arriba.

- Para redondear correctamente:
- `math.floor(x)` → redondea hacia abajo.
- `math.ceil(x)` → redondea hacia arriba.

### Valores especiales en `float`
- `float()` acepta:
- `"nan"`  → Not a Number
- `"inf"`  → Infinito positivo
- `"-inf"` → Infinito negativo

### Literales numéricos
- Puedes usar los dígitos `0` a `9`, o caracteres Unicode equivalentes con propiedad `Nd`.

## Comparadores
Lexicographic order

| Operador | Significado                  | Ejemplo             |
|----------|------------------------------|---------------------|
| `<`      | menor que                    | `3 < 5 → True`      |
| `<=`     | menor o igual que            | `5 <= 5 → True`     |
| `>`      | mayor que                    | `8 > 2 → True`      |
| `>=`     | mayor o igual que            | `5 >= 6 → False`    |
| `==`     | igual                        | `"a" == "a" → True` |
| `!=`     | distinto                     | `7 != 3 → True`     |
| `is`     | misma identidad de objeto    | `a is b`            |
| `is not` | distinta identidad           | `a is not b`        |

## <, <=, >, >=
Se usan con numeros, letras o cualquier valor ordenable.

print(3 < 5)      # True
print("a" < "z")  # True

## ==, !=
Comparan si los valores son iguales o distintos.

print(3 == 3)        # True
print("hola" != "")  # True

True → 1
False → 0
---
## Booleanos y operadores lógicos

- `True` se comporta como `1`, y `False` como `0`.

### Operadores:

- `x or y`: Devuelve `x` si es verdadero, si no, devuelve `y`.
- `x and y`: Devuelve `x` si es falso, si no, devuelve `y`.
- `not x`: Invierte el valor lógico (`not True → False`)

### 'or' : x or y
- Si 'x' es verdadero, devuelve 'x'
- Si 'x' es falso, devuelve 'y'

---Solo evalúa 'y' si 'x' es falso.

### 'and' : x and y
- Si `x` es falso, devuelve `x`
- Si `x` es verdadero, devuelve `y`

---Solo evalúa `y` si `x` es verdadero.

### 'not': not x

- Si `x` es falso, devuelve `True`
- Si `x` es verdadero, devuelve `False`

## Evaluación de verdad (Truth Value Testing)

Python considera **falso** lo siguiente:

### Constantes:
- `None`, `False`

### Números:
- `0`, `0.0`, `0j`
- `Decimal(0)`, `Fraction(0, 1)`

### Colecciones vacías:
- `""`, `[]`, `()`, `{}`, `set()`, `range(0)`

Todo lo demás se evalúa como **True**.

--
# Métodos Adicionales del Tipo `int` en Python

## 1. `int.bit_length()`
Devuelve la cantidad de bits necesarios para representar el valor absoluto de un entero en binario (sin signo ni ceros iniciales).

## 2. `int.bit_count()`
Cuenta los bits `1` en la representación binaria del valor absoluto del número.

## 3. `int.to_bytes(length, byteorder, signed=False)`
Convierte un entero en una secuencia de bytes.

## 4. `int.from_bytes(bytes, byteorder, signed=False)`
Convierte una secuencia de bytes a un número entero.

## 5. `int.as_integer_ratio()`
Devuelve una tupla `(numerador, denominador)` equivalente a la fracción del entero.

## 6. `int.is_integer()`
Devuelve `True`. Añadido por compatibilidad con `float.is_integer()`.
-----

sea L = min(|s|, |t|) 
si existe 1 <= i <= L tal que
s[j] = t[j] para todo j < i
s[i] < t[i] alfab'eticamente
si s[j] = t[j] para todo 1 <= j  <= L, pero |s| < |t|
amor vs a
amor mide 4
a mide 1
hasta la posici'on 1
a < amor
bebe vs zu 
L = min(4, 2) = 2
b vs z (alfabéticamente)
bebe < zu 
meme vs meter
L = min(4, 5) = 4
para i = 1
m = m
para i = 2, e = e
para i = 3, m < t
meme < meter
---

En Python, las cadenas de texto se pueden comparar usando los comparadores <, >, ==, etc.
Estas comparaciones se hacen de forma lexicográfica, es decir, comparando caracter por caracter.

Por ejemplo,
"ana" < "carlos" da True porque 'a' < 'c'.
"ana" < "andres" da True porque 'a' == 'a', 'n' == 'n', pero 'a' < 'd'

Implementa una función llamada es_menor_lex(s: str, t: str) -> bool que retorna True si s es menor que t 
según el orden lexicográfico, y False en caso contrario.

Una cadena s es menor lexicográficamente que otra cadena t si ocurre alguna de las siguientes condiciones:
1. Existe un índice i tal que s[i] < t[i] y s[j] == t[j] para todo j < i.
2. O bien, s es un prefijo propio de t (es decir, todos los caracteres de s coinciden con los de t, pero s es más corta que t).

Ejemplos:
es_menor_lex("ana", "andres") retorna True
es_menor_lex("casa", "casamiento") retorna True
es_menor_lex("zorro", "abeja") retorna False
es_menor_lex("hola", "hola") retorna False

