#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:03:15 2021

@author: alberto

Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla 
la misma frase pero con la vocal introducida en mayúscula.

"""

frase=input("Introduce una face: ")
vocal=input("Introduce una voical en minusculas: ")

print(frase.replace(vocal, vocal.upper()))