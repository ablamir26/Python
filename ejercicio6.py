# Escribir un programa que pida al usuario un número entero y muestre por pantalla
# un triángulo rectángulo como el de más abajo, de altura el número introducido.
# Para ayudarte a ver la lógica, imagina que el usuario introduce el número 5. El resultado en pantalla debería verse así:

# *
# **
# ***
# ****
# *****
num = int(input("introduce un numero entero"))
# i es el numero de veces que el asterisco se imprime dentro del for hasta llegar al numero del imput
for i in range (1, num + 1):
    print ("*" * i)


 