# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:48:30 2024

@author: daniel
"""

import calculadora_indices as calc

def ejecutar_consola_IMC()->None:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura "))
    IMC = calc.calcular_IMC(peso, altura)
    print("Su IMC es: ", str(round(IMC,2)))
    
ejecutar_consola_IMC()
    