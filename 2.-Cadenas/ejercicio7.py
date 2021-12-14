#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 17:48:06 2021

@author: alberto
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

"""

correo=input("Introduce tu correo electronico: ")


print(correo[:correo.find('@')]+"@ceu.es")