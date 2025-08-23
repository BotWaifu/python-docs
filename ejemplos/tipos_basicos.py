# Tipos básicos: int, float, complex

x = 5
y = 3.14
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

print(type(y).__name__)  # Solo el nombre como texto

# Función y clase
def f(n):
    return 2 * n

print(f)
print(f.__name__)

class Persona:
    def __init__(self):
        self.nombre = "Zulhei"
        self.edad = 27

print(Persona.__name__)

persona = Persona()
print(persona.nombre)
