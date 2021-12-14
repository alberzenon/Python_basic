#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 18:30:36 2021

@author: alberto

Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""

hrst=float(input("Introduce tus horas trabajadas: "))
costo=float(input("Introduce el costo por hora: "))


total= hrst*costo

print("Tu pago total es: ",total)