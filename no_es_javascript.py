# #EJEMPLO 1 

# lista = [3,1,2]
# resultado = lista.sort()

# print("Lista ordenada:",lista)
# print("Resultado de sort():",resultado)

# #Ejemplo 2

# nombre = "Zulhei"
# print(nombre == "Zulhei")  
# print(str(25))             
# print(repr(3.14))          

# #Ejemplo 3

# texto = "Hola Zulhei"
# print(str(texto))  
# print(repr(texto))  

# x = 5       
# y = 3.14     
# z = 2 + 3j   

# print(type(x))  
# print(type(y))  
# print(type(z))  

# #Lo que me explico mi amorcito uwu

# x = 5
# y = 3.14
# z = 2 + 3j

# print(type(x))
# print(type(y).__name__)
# print(type(z))

# def f(n):
#     return 2 * n

# class Persona:
#     def __init__(self):
#         self.nombre = "Zulhei"
#         self.edad = 27

# print(Persona.__name__)

# w = Persona()
# print(w.nombre)

# print(f)
# print(f.__name__)

# #EJEMPLO DE OR

# print("" or "Zulhei")     
# print("Hola" or "Mundo")  
# print(False or 5)         

# #EJEMPLO DE AND

# print(1 and 2)            
# print(0 and "Zulhei")     
# print(True and "Python")  

# #EJEMPLO DE NOT

# print(not True)           
# print(not "")             
# print(not [1, 2])         

# #EJEMPLO DE <, <=, >, >=

# print(3 < 5)      
# print("a" < "z")  

# #EJEMPLO DE ==, !=

# print(3 == 3)        
# print("hola" != "")  

# #uwu
# # Ejercicio 1
# print(10 > 5 and 3 <= 3)

# # Ejercicio 2
# print("perro" != "gato")

# # Ejercicio 3
# print(4 is 4.0)

# # Ejercicio 4
# print([1, 2] == [1, 2])

# # Ejercicio 5
# x = [1, 2, 3]
# y = x
# print(x is y)

# # Ejercicio 6
# print("x" in "texto")

# # Ejercicio 7
# print("z" not in "zapato")

# # Ejercicio 8
# print(2.0 == 2)

# # Ejercicio 9
# print(None is not False)

# # Ejercicio 10
# print((1 < 2) < 3)  # Comparación encadenada

#Tipos numericos
##int
x = 10
type (x) # <class 'int'>

edad = 25
print (type(edad)) # <class 'int'>

#float
y = 3.14
type(y)  # <class 'float'>

#complex
z = 2 + 3j
z.real        # 2.0
z.imag        # 3.0
z.conjugate() # 2 - 3j
type(z)       # <class 'complex'>

#Operaciones básicas
a = 10
b = 3

print(a + b)   # 13 (suma)
print(a - b)   # 7  (resta)
print(a * b)   # 30 (multiplicación)
print(a / b)   # 3.333... (división decimal)

### `x % y` → Módulo o residuo
7 % 2  # → 1 (porque 2 cabe 3 veces en 7, y sobra 1)
10 % 5 # → 0 (no sobra nada)

### -x → Número negado
x = 5
print(-x)     # → -5
print(-(-5))  # → 5

### +x → Número sin cambios
x = 3
print(+x)  # → 3

### abs(x) → Valor absoluto
abs(-4)  # → 4
abs(4)   # → 4

### int(x) → Convierte a entero
int(3.9)  # → 3

### float(x) → Convierte a decimal
float(5)  # → 5.0

### complex(re, im) → Número complejo
z = complex(2, 3)  # → 2 + 3j

### c.conjugate() → Conjugado complejo
(2 + 3j).conjugate()  # → 2 - 3j

### divmod(x, y) → División con cociente y resto
divmod(9, 4)  # → (2, 1)

### pow(x, y) → Potencia (función)
pow(2, 3)  # → 8

### x ** y → Potencia (operador)
2 ** 3   # → 8
9 ** 0.5 # → 3.0 (raíz cuadrada de 9)


