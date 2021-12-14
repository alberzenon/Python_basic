#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 22:20:16 2021

@author: alberto
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre 
por pantalla la misma frase pero con la vocal introducida en mayúscula.

"""

frase=input("Introdusca una frase: ")
vocal = input("Introduce una vocal: ")

print(frase.replace(vocal, vocal.upper()))