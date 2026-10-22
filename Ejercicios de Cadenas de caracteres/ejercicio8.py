# Escribir un programa que pregunte por consola el precio de un producto en euros
# con dos decimales y muestre por pantalla el número de euros y el número de
# céntimos del precio introducido.
preprod = (input("Introduce un precio (en euros) con decimales: "))
preprodsplit = preprod.split(".")
print("el precio del producto es", preprodsplit[0] + "€")
print("el precio del producto es", preprodsplit[1] + "cts")
