# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
# aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
# conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
# intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
# los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
# en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

# Nivel           Puntuación
# Inaceptable     0.0
# Aceptable       0.4
# Meritorio       0.6 o más

# Escribir un programa que lea la puntuación del usuario e indique su nivel de
# rendimiento, así como la cantidad de dinero que recibirá el usuario.

# Solicitamos la puntuación al usuario (convertida a número decimal)
puntuacion = float(input("Introduce la puntuación obtenida (ej. 0.0, 0.4, 0.6): "))

# Definimos la cantidad fija por punto
BASE_DINERO = 2400.0

# Evaluamos los niveles mediante condicionales
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = puntuacion * BASE_DINERO
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Cantidad de dinero que recibirá: {dinero:.2f}€")

elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = puntuacion * BASE_DINERO
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Cantidad de dinero que recibirá: {dinero:.2f}€")

elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = puntuacion * BASE_DINERO
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Cantidad de dinero que recibirá: {dinero:.2f}€")

else:
    print("Puntuación no válida. Los valores permitidos son 0.0, 0.4, o 0.6 o más.")