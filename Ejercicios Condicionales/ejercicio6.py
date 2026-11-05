# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
# el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
# los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
# programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
# que le corresponde.
nombre = input("Introduce tu nombre").upper()
sexo = input("Introduce tu sexo H/M").upper()

if nombre[0] < "M" and sexo =="M" or nombre[0] > "N" and sexo== "H":
    print("Estás en el grupo A")
else: 
    print("Estás en el grupo B")

