#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:46:57 2021

@author: alberto

Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente 
y el resto de la división entera respectivamente.

"""

n1 = input("Introduce el primer numero: ")
n2 = input("Introduce el segundo numero: ")


c=int(n1) // int(n2)
r=int(n1) %  int(n2)


print("*******   "  +n1 + " entre " +n2 +" da un cociente de "+str(c)+" y un resto de: "+str(r)+"  ********")


