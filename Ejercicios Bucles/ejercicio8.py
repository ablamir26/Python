# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero= int(input ("Introduce un número"))
for fila in range (1, numero +1, 2):
    print ()

    for columna in range (fila, 0, -2):
        print (columna, end=" ")
