# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
# un descuento del 60%. Escribir un programa que comience leyendo el número de
# barras vendidas que no son del día. Después el programa debe mostrar el precio
# habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
# coste final total.
precio_pan_normal = 3.49
descuento = 0.6
barras_nodia = float(input("Introduce el numero de barras vendidas que no son del dia: "))
precio_descuento = round(3.49 * 0.4, 2)

print(f"El precio habitual de una barra de pan fresca es {precio_pan_normal}, el descuento es de un {descuento}% por no ser una barra fresca y el coste final de la barra, con descuento es {precio_descuento} € por barra")
print(f"Como el número de barras es {barras_nodia:2.0f} el precio total es de {precio_descuento * barras_nodia}€")