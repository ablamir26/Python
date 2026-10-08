# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
# interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
# año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
# comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
# introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
# la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
# cantidad a dos decimales
dinero_depositado = float(input("Introduce la cantidad depositada "))
interes = 0.04
cantidad_ahorros_año1 = dinero_depositado * (1 + interes)
cantidad_ahorros_año2 = cantidad_ahorros_año1 * (1 + interes)
cantidad_ahorros_año3 = cantidad_ahorros_año2 * (1 + interes)
print(f"Ahorros tras el primer año: {round(cantidad_ahorros_año1, 2)} €")
print(f"Ahorros tras el segundo año: {round(cantidad_ahorros_año2, 2)} €")
print(f"Ahorros tras el tercer año: {round(cantidad_ahorros_año3, 2)} €")