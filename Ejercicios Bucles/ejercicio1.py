# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces
palabra= input("Escribe una palabra")

for i in range(10):
    print (palabra)

# NOTA: Si usas input como el nombre de la variable del bucle, vas a sobrescribir la función interna input() 
# de Python (aunque en este programa corto no la vuelvas a usar después, es una muy mala práctica porque 
# rompe esa función para el resto del archivo).

# En Python, la variable que va justo después de for es un contador temporal que inventas tú 
# solo para llevar la cuenta de las vueltas. Por convención, los programadores suelen 
# llamarla i (de índice o iterador), x, o incluso _ (guion bajo) cuando no van a usar 
# ese número para nada.