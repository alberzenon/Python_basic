#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 21:19:53 2021

@author: alberto

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
líneas distintas el nombre del usuario tantas veces como el número introducido.
"""


nombre= input("¿Como te llamas? ")
n= input("Introduce un numero entero ")
print((nombre + "\n")*int(n))