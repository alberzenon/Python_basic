#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 00:16:02 2021

@author: alberto
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo
 y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos 
 y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
 Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
 y calcule el peso total del paquete que será enviado.
"""

payaso= int(input("Introduce el numero de payasos vendidos: "))
muniecas= int(input("Introduce el numero de muñecas vendidas: "))

peso_payaso = 112
peso_munieca= 75
peso_total= peso_payaso*payaso + peso_munieca *muniecas


print("El peso total de los payasos es: "+str(peso_total))