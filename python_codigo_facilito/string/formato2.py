curso="python"
version="3"

#resultado="Curso de %s %s" %(curso,version)
resultado = "curso de {a} {b}".format(a=curso,b=version)
print(resultado)



curso2="Curso de Python"
print("original--> ", curso2)
#curso2= "c"+curso2[1:]
curso2= "c"+curso2[1:] +str(2.7)+ " " + "en Codigo facilito"
print(curso2)