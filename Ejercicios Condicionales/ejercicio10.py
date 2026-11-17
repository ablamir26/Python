# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
    # ● Ingredientes vegetarianos: Pimiento y tofu.
    # ● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
# en función de su respuesta le muestre un menú con los ingredientes disponibles
# para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
# tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
# pizza elegida es vegetariana o no y todos los ingredientes que lleva.
print("Bienvenido a la pizzería Bella Napoli.")
print("Tipos de pizza:")
print("1. Vegetariana")
print("2. No vegetariana")

tipo = input("Introduce el número correspondiente al tipo de pizza que quieres: ")

# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas:")
    print("1. Pimiento")
    print("2. Tofu")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    
    if ingrediente == "1":
        print("Pizza vegetariana con mozzarella, tomate y pimiento.")
    else:
        print("Pizza vegetariana con mozzarella, tomate y tofu.")

elif tipo == "2":
    print("Ingredientes de pizzas no vegetarianas:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    
    if ingrediente == "1":
        print("Pizza no vegetariana con mozzarella, tomate y peperoni.")
    elif ingrediente == "2":
        print("Pizza no vegetariana con mozzarella, tomate y jamón.")
    else:
        print("Pizza no vegetariana con mozzarella, tomate y salmón.")

else:
    print("Opción no válida. Por favor, reinicia el programa y elige 1 o 2.")