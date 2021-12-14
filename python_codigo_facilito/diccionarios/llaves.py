diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
resultado=diccionario.keys() #inrpimiendo los valores de las llaves  dict_key
print(resultado)
resultado =tuple(resultado) #convirtiendola a una tupla
print(resultado)

resultado= diccionario.values()
print(resultado)

#metodo items

resultado2=diccionario.items()
print(resultado2)  #dict_items

#tambien se pude transformar en una lista o una tupla

resultado2=list(resultado2)
print(resultado2)