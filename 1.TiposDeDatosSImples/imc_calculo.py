#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:48:57 2021

@author: alberto

Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y
 lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> 
 es el índice de masa corporal calculado redondeado con dos decimales.
"""


peso = input("¿Cuál es tu peso en KG?:  ")
estatura=input("¿Cuál es tu estatura en metros?: ")
imc = round(float(peso)/float(estatura)**2,2)

print("Tu indice de masa corporal es "+ str(imc))