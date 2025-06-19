#Apuntes Python - Su 🐍

# TODO: Cosas por hacer
# NOTE: Anotaciones
# FIXME: Lanza error
# BUG: Errores confirmados
# HACK: Soluciones rapidas
# XXX: Revisar esta parte
--------------------------------------------------------------------
# Tipos built-in
-'int', 'float', 'complex': Numero y texto
-'str', 'list', 'tuple', 'range': Secuencias (ordenadas)
-'dict': Mappings (clave-valor)
-'class' y 'instance': Tipos definidos por el usuario
-'exception': Errores (como ValueError, IndexError, etc.)
-'bool': verdadero/falso
-'None': ausencia de valor

------------------------------------------------------------------------
## Algunas colecciones (como listas y diccionarios) se puede*n modificar directamente (son mutables)
Cuando se usa un metodo como .append() o .sort()
- Modifican la colección
- No devuelven nada (retornan None)

### Ejemplo:

lista = [3, 1, 2]
resultado = lista.sort()

print(lista)      # [1, 2, 3]
print(resultado)  # None

## Hay operaciones que se pueden usar con casi cualquier tipo de objeto, como:

- Compararlos con == o !=
- Convertirlos a texto con str() o repr()
- Imprimirlos con print ()

### Ejemplo:
nombre = "Zulhei"
print(nombre == "Zulhei")  # True
print(str(25))             # "25"
print(repr(3.14))          # '3.14'

--------------------------------------------------
### str () vs repr()

- str(): Convierte en texto legible
Ej: str(25) -> "25", str ("hola") -> "hola"

- repr(): Muesta de manera técnica y exacta (con comillas, etc)
Ej: repr(3.14) → '3.14', repr("hola") → "'hola'"

- print() usa str() por defecto

## Comparacion str() vs repr() con distintos tipos

------------------------------------------------------------------------
# Strings

texto = "Hola Zulhei"

print(str(texto))   # Hola Zulhei
print(repr(texto))  # 'Hola Zulhei'

- repr() muestra las comillas para dejar claro que es un string. str() no-

### Lo que me explico uwu

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

## Tipos Numéricos (Numeric Types)

Hay tipos númericos principales:

- int : Numeros enteros (1, 0, -7)
- float : Numeros decimales (3.14, -1.0)
- complex : Numeros complejos (2+3j)

### Ejemplo :

x = 5        # int
y = 3.14     # float
z = 2 + 3j   # complex

print(type(x))  # 'int'
print(type(y))  # 'float'
print(type(z))  # 'complex'

--------------------------------------------

# Truth Value Testing
Cualquier objeto puede ser evaluado como verdadero o falso, por ejemplo en un:

- if
- while
- Operacion logica como and, or

Un objeto es considerado verdadero (True), a menos que:
- Tenga un método _bool_() que devuelva False, o
- Tenga un método _len_() que devuelva 0

Python considera como False:

1. Constantes:
- 'None' --> nada
- 'False' --> boleano falso

2. Ceros numericos: 
- 0, 0.0 ,0j --> enteros, flotantes, complejos
- Decimal (0), Fraction(0,1) --> librerias espaciales

3. Colecciones Vacías:
- '' --> string vacío
- [] --> lista vacía
- () --> tupla vacía
- {} o set() --> conjunto vacío
- range(0) --> rango sin números

### Todo lo demás es True

# Bolean Operations - ('and', 'or','not')

### 'or' : x or y
- Si 'x' es verdadero, devuelve 'x'
- Si 'x' es falso, devuelve 'y'

---Solo evalúa 'y' si 'x' es falso

### 'and' : x and y
- Si `x` es falso, devuelve `x`
- Si `x` es verdadero, devuelve `y`

---Solo evalúa `y` si `x` es verdadero

### 'not': not x

- Si `x` es falso, devuelve `True`
- Si `x` es verdadero, devuelve `False`

# Operadores de comparación en Python

|Operador |  Resultado                | Ejemplo               |
|-------------------------------------------------------------|
|<        | menor que                 | 3 < 5 --> True        |
|<=       | menor o igual que         | 5 <= 5 --> True       |
|>        | mayor que                 | 8 > 2--> True         |
|>=       | mayor o igual que         | 5 >= 6 --> False      |
|==       | igual                     | "a" == "a" --> True   |
|!=       | distinto                  | 7! = 3 --> True       |
|is       | misma identidad de objeto | a is b                |
|is not   | diferente identidad       | a is not b            |

## <, <=, >, >=
Se usan con numeros, letras o cualquier valor ordenable

print(3 < 5)      # True
print("a" < "z")  # True

## ==, !=
Comparan si los valores son iguales o distintos

print(3 == 3)        # True
print("hola" != "")  # True
