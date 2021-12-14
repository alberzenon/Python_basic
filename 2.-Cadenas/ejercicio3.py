#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 13:55:51 2021

@author: alberto
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> 
es el número de letras que tienen el nombre.
"""

nombre = input("Digita tu nombre: ")

print(nombre.upper()+"  Tiene "+str(len(nombre))+ " Letras ")