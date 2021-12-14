#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:37:55 2021

@author: alberto
"""

import funciones.funcionesAlbert as fa

producto ="capuchino"
cuantos=fa.lenN(producto)
print("El tamaño de  la cadena es: ",cuantos)


cadena=input("Ingrese un numero: ")
numero=fa.validar_numero(cadena)
print("esto es un numero: ",numero)