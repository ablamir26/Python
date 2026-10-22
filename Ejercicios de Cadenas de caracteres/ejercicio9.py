#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.
fecnac= input("Introduce tu fecha de nacimiento con formato dd/mm/aaaa ")
fecnacsplit= fecnac.split("/")
print("Tu fecha de nacimiento es ")
print("Día:", fecnacsplit[0])
print("Mes:", fecnacsplit[1])
print("Año:", fecnacsplit[2])
