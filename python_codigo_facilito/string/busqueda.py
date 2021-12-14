mensaje="Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"
resultado=mensaje.count("texto")
resultado2=mensaje.count("e")
print(resultado)
print(resultado2)

resultado3 = "texto" not in mensaje
print(resultado3)


resultado4 = mensaje.find("texto")
print(resultado4)

resultado4 =mensaje[resultado4: resultado4+len("texto")]
print(resultado4)


#saber si inicia con ese texto o caracter
resultado5 = mensaje.startswith("Este")
print(resultado5)

#Saber si termina con ese texto o caracter

resultado6 = mensaje.endswith("refiere")
print(resultado6)
