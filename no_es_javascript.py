#EJEMPLO 1 

lista = [3,1,2]
resultado = lista.sort()

print("Lista ordenada:",lista)
print("Resultado de sort():",resultado)

#Ejemplo 2

nombre = "Zulhei"
print(nombre == "Zulhei")  
print(str(25))             
print(repr(3.14))          

#Ejemplo 3

texto = "Hola Zulhei"
print(str(texto))  
print(repr(texto))  

x = 5       
y = 3.14     
z = 2 + 3j   

print(type(x))  
print(type(y))  
print(type(z))  

#Lo que me explico mi amorcito uwu

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

w = Persona()
print(w.nombre)

print(f)
print(f.__name__)

#EJEMPLO DE OR

print("" or "Zulhei")     
print("Hola" or "Mundo")  
print(False or 5)         

#EJEMPLO DE AND

print(1 and 2)            
print(0 and "Zulhei")     
print(True and "Python")  

#EJEMPLO DE NOT

print(not True)           
print(not "")             
print(not [1, 2])         

#EJEMPLO DE <, <=, >, >=

print(3 < 5)      
print("a" < "z")  

#EJEMPLO DE ==, !=

print(3 == 3)        
print("hola" != "")  

#uwu


