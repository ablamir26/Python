#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.
correo = input("introduce tu correo electrónico")
correosplit = correo.split("@")
print("Tu nuevo correo es ", correosplit[0] + "@ceu.es")