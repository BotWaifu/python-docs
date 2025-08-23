# Ejemplos y ejecicios de operaciones numéricas en Python

#División entera (//)
print(7 // 3)      # 2
print(-7 // 3)     # -3
print(7 // -3)     # -3
print(-7 // -3)    # 2

#Conversión de Float a Int
print(int(4.9))    # 4
print(int(-4.9))   # -4

#math.floor() y math.ceil()
import math

print(math.floor(3.7))   # 3
print(math.ceil(3.7))    # 4
print(math.floor(-3.7))  # -4
print(math.ceil(-3.7))   # -3

#math.trunc()
print(math.trunc(3.7))    # 3
print(math.trunc(-3.7))   # -3

print(round(2.5))        # 2 (redondea al par más cercano)
print(round(3.5))        # 4
print(round(3.14159, 2)) # 3.14

#float con valores especiales 
print(float("nan"))    # nan
print(float("inf"))    # inf
print(float("-inf"))   # -inf

#Potencia especial 0 ** 0
print(pow(0, 0))   # 1
print(0 ** 0)      # 1
