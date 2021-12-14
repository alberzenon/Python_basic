#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:46:01 2021

@author: alberto
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número introducido.
"""

nombre = input("Introduce tu Nombre: ")
n = input("Introduce un numero entero: ")

print((nombre+"\n")*int(n))