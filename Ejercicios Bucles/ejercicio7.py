# Escribir un programa que muestre por pantalla la tabla 
# de multiplicar del 1 al 10
for num in range(1, 11):
    print(f"--- Tabla del {num} ---")
    for multiplicador in range(1, 11):
        print(f"{num} x {multiplicador} = {num * multiplicador}")
    print()  # Línea en blanco para separar cada tabla