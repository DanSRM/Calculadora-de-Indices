# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 14:49:35 2024

@author: daniel
"""
import calculadora_indices as calc

def ejecutar_consola_calorias_actividad()->None:
    
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura en centímetros: "))
    edad = int(input("Ingrese su edad: "))
    print("Masculino: 5 y Femenino: -161")
    valor_genero = float(input("Ingrese su valor de genero: "))
    print("1.2: poco o ningún ejercicio") 
    print("1.375: ejercicio ligero (1 a 3 días a la semana))")
    print("1.55: ejercicio moderado (3 a 5 días a la semana))")
    print("1.725: deportista (6 -7 días a la semana)")
    print("1.9: atleta (entrenamientos mañana y tarde)")
    valor_actividad = float(input("Valor de actividad física: "))
    
                                  
    TMB_AF = calc.calcular_calorias_en_activivdad(peso, altura, edad, valor_genero, valor_actividad)

    print("Su ingesta de calorías debe de ser: " + str(round(TMB_AF,2)) + " kcal")
    

ejecutar_consola_calorias_actividad()