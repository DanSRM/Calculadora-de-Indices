# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:49:28 2024

@author: daniel
"""

import calculadora_indices as calc

def ejecutar_consola_calorias_reposo()->None:
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura en centímetros: "))
    edad = int(input("Ingrese su edad: "))
    valor_genero = int(input("Ingrese su valor de genero (Masculino: 5 y Femenino: -161): "))
    
    TMB = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    print("La cantidad total de sus calorias en reposo es " + str(round(TMB,2)) + " kcal")
    
ejecutar_consola_calorias_reposo()
