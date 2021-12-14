#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:18:42 2021

@author: alberto

Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
segundo y tercer años. Redondear cada cantidad a dos decimales.
"""

inversion=float(input("Introduce la cantidad a invertir en cuentra de Ahorro:  "))

interes = 0.04
balance1= inversion * (interes+1)
balance2= balance1 * (interes+1)
balance3= balance2 * (interes+1)
print("Balance del primer año: "+str(round(balance1,2)))
print("Balance del segundo año:"+str(round(balance2,2)))
print("Balance del Tercer año:"+str(round(balance3,2)))