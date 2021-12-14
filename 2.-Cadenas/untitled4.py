#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 14:03:49 2021

@author: alberto
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del 
país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por 
pantalla el número de teléfono sin el prefijo y la extensión.
"""

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print(" EL NUMERO TELEFONICO ES: "+ tel[4:-3])+52-722130