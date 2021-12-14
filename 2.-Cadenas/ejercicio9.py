#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:21:21 2021

@author: alberto

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
el día, el mes y el año.

"""

fecha= input("Digita la fecha de tu nacimiento en el formato dd/mm/aaaa: ")

print("DIA: "+fecha[:2])
print("MES: "+fecha[3:5])
print("AÑO: "+fecha[6:10])