#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:00:00 2021

@author: alberto

Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca 
y el coste final total.

"""

barras  = int(input("Introduca numero de barras  vendidas que no son del dia:  "))

precio= 3.49
descuento=0.6

coste =barras * precio *(1-descuento)

print("El costo del pan fresco es: "+str(precio))
print("el descuento sobre una barra no fresca es: "+str(descuento*100))
print("El cosoto final a pagar es: " + str(round(coste,2)))
      