# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.ç
num = int(input("Escribe un número entero positivo: "))
for i in range(num, -1, -1):
    print(i, end=", ")