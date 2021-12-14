#Diciconario
diccionario ={"a":1, "b":2, "c":3,"a":4}
print(diccionario)
#imprimiendo el valor de una llave 
resultado = diccionario["a"]
print(resultado)

#usando el metodo in para buscar el valor de una llave
resultado2 = "a" in diccionario
print(resultado2)

#usando el metodo get

resultado3 = diccionario.get("a")
print(resultado3)
#usuando get con doble valor para retornar mensaje cuando la llave no exista 


resultado4 = diccionario.get("z","ERROR la llave no existe")
print(resultado4)

#metodo setdefault
resultado5 = diccionario.setdefault("z",{})
print(resultado5)
print(diccionario)
