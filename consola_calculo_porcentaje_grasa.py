# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:49:20 2024

@author: daniel
"""
import calculadora_indices as calc

def ejecutar_consola_porcentaje_grasa()->None:
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    edad = int(input("Ingrese su edad: "))
    valor_genero = float(input("Ingrese su valor de genero (Masculino: 10.8 y Femenino: 0) : "))
    GC = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
    print("Su porcentaje de grasa actual es el siguiente: " , round(GC,2) , "%")
    
ejecutar_consola_porcentaje_grasa()
    