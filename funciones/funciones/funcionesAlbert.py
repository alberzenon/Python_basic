#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 11:44:33 2021

@author: alberto
"""

#Definicion de una funcion
"""
def nombreFucion(parametro1,parametro2,...):
    linea1
    linea2
    linea3
    return var1
"""

def mensaje():
    print("Bienvenido Alberto")
    
def mensaje2(nombre): #nombre=cad
    print("Bienvenido", nombre)


def mensaje3(nombre): #nombre=nom
    cadena="Bienvenido "+nombre
    return cadena



def lenN(cadena):
    cont=0
    for caract in cadena:
        cont+=1
    return cont


def validar_numero(cadena):
    while not cadena.isdigit():
        cadena=input("ERROR, ingrese un numero: ")
    return int(cadena)