

# Esto es un comentario de linea

"""

Esto es un comentario de bloque

"""

print("Hello Python. This is my first line of code in Python");

variableNum = 10
variableTexto = "--Variable de texto--"
print(variableNum, " espacio " , variableTexto)

arrayPython = {1,2,3,4,5}

# For en Python
for i in arrayPython:
    print("number: ",i)

# While en Python
i = 0
while i < 5:
    print(i)
    i+=1
    print("Estoy dentro del 'while'")
        #print("¿?") # Esto provoca IndentatioError: unexpected indent

# En Python la tabulación marca cuando se esta dentro de un bloque.
print("Estoy fuera del 'while'")