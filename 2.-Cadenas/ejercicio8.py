#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 18:08:37 2021

@author: alberto

Escribir un programa que pregunte por consola el precio de un producto en pesos con dos decimales y
 muestre por pantalla el número de pesos y el número de centavos del precio introducido.
"""

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

