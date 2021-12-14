#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:04:39 2021

@author: alberto

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
 muestre por pantalla el capital obtenido en la inversión.
"""

cantidad= float(input("Cantidad a inverir: "))
interes= float(input("Interes porcentual anual: "))
años = int(input("Años"))

capital= round(cantidad*(interes/100+1)**años,2)


print("Capital final: "+str(capital))