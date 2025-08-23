# Operadores de comparación

print(3 < 5)             # True
print("a" < "z")         # True
print(3 == 3)            # True
print("hola" != "")      # True
print(4 is 4.0)          # False (diferente tipo)
print([1, 2] == [1, 2])  # True (contenido igual)
x = [1, 2, 3]
y = x
print(x is y)            # True (misma referencia)
