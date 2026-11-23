# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
# año que dura la inversión.
inversion = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años de inversión? "))

for i in range(1, años + 1):
    inversion *= 1 + interes / 100
    print(f"Capital tras {i} año(s): {inversion:.2f}")