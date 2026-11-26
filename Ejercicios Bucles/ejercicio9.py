# Escribir un programa que almacene la cadena de caracteres contraseña en una
# variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
# correcta.
contraseña = "contraseña"
pregunta = ""

while pregunta != contraseña:
    pregunta = input("Dime tu contraseña: ")
    if pregunta != contraseña:
        print("Esa no es tu contraseña")

print("Esa es tu contraseña")