texto = "curso de python3"
resultado = texto.capitalize() #genera un nuevo String con letra mayuscula
print(resultado)

resultado2 = texto.swapcase() #Genera un nuevo string cambiando las letras mayusculas a minusculas y biceversa
print(resultado2)

resultado3 = texto.upper() #Genera un nuevo string cambiando las letras minusculas a mayusculas 
print(resultado3)

resultado4 = texto.lower() #Genera un nuevo string cambiando las letras mayusculas a minusculas 
print(resultado4)

#Saber si el string se encuentra con maysuculas o minusculas

texto2 = "curso de python3 , python3 basico"
resultado5 = texto2.upper() 
print(resultado5.isupper())
print(resultado5.islower())


resultado6 = texto2.title() 
print(resultado6)


resultado7 = texto2.replace("python3", "ruby",1) 
print(resultado7)

texto4 = "        curso de python3 , python3 basico con strip"
resultado8 = texto4.strip() 
print(resultado8)

