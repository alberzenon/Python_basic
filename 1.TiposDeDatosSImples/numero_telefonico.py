#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:03:38 2021

@author: alberto

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del 
país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla 
el número de teléfono sin el prefijo y la extensión.
"""


telefono = input("Digite el telefono con el formato +xx-xxxxxxxxxx-56")
print("EL numero telefonico es ", telefono[4:-3])