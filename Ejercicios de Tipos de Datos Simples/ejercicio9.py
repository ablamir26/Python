# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
# y el número de años, y muestre por pantalla el capital obtenido en la inversión.
# Solicitar los datos al usuario
capital = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))
capital_final = capital * (1 + (interes / 100) * años)
print("El capital obtenido en la inversión es: " + str(capital_final))
