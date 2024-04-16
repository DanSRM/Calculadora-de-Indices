# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:49:55 2024

@author: daniel
"""

import calculadora_indices as calc

def ejecutar_consola_calorias_adelgazar()->None:
    peso = float(input("Ingresa tu peso: "))
    altura = float(input("Ingresa tu altura en centímetros: "))
    edad = int(input("Ingresa tu edad: "))
    print("(Masculino: 5, Femenino: -161")
    valor_genero = float(input("Ingresa tu valor de genero: "))
    
    CPAd = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
    
    print(CPAd)
    
ejecutar_consola_calorias_adelgazar()