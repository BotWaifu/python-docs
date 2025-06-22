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
7. [Comparadores](#comparadores)
8. [Booleanos y operadores lógicos](#booleanos-y-operadores-lógicos)
9. [Evaluación de verdad (Truth Value Testing)](#evaluación-de-verdad-truth-value-testing)


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

Cuando se usa un metodo como .append() o .sort()
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
---

## Comparadores

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
