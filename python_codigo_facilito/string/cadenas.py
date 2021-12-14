curso="Curso de Python3"

resultado =len(curso)
resultado2=curso[1:16:2]
print(resultado)
print(resultado2)


lenguajes="python; Java; Ruby; PHP; Swift; JavaScrypt; C#; c; C++"

separador ="; "
new_result= lenguajes.split(separador) #El nuevo resultado es una lista 
print(lenguajes)
print(new_result)

new_string = separador.join(new_result)
print(new_string)


#texto con saltos de linea


texto= """Esto es un texto 
con 
saltos 
de

linea"""

nuevo_txt= texto.splitlines()
print(nuevo_txt)