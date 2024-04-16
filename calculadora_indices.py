# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:43:16 2024

@author: daniel
"""

def calcular_IMC(peso: float, altura: float)->float:
    """

    Calcula el índice de masa corporal de una persona a partir de la ecuación
    definida anteriormente.
    
    Parameters
    ----------
    peso : float
        DESCRIPTION. Peso de la persona en kilogramos.
    altura : float
        DESCRIPTION. Altura de la persona en metros.

    Returns
    -------
    float
        DESCRIPTION. Índice de masa corporal de la persona.

    """
    # Calcular el índice de masa corporal
    IMC = peso/(altura**2)
    
    # Enviar el IMC como resultado
    return IMC

def calcular_porcentaje_grasa(peso: float, altura: float, edad: int, valor_genero: float)-> float:
    """
    Calcula el porcentaje de grasa de una persona a partir de la ecuación 
    definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION. Peso de la persona en kilogramos.
    altura : float
        DESCRIPTION. Altura de la persona en metros.
    edad : int
        DESCRIPTION. Edad de la persona en años.
    valor_genero : float
        DESCRIPTION. Valor que varía según el género de la persona: en caso de ser masculino debe 
        ser 10.8 y en caso de ser femenino debe ser 0.

    Returns
    -------
    float
        DESCRIPTION.  El porcentaje de grasa que tiene el cuerpo de la persona.

    """
    # calcular el IMC
    IMC = calcular_IMC(peso, altura)
    
    # Calcular el porcentaje de grasa corporal
    GC = 1.2*IMC+0.23*edad-5.4-valor_genero
    
    return GC

def calcular_calorias_en_reposo(peso: float, altura: float, edad: int, valor_genero: int)->float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal), a partir de la ecuación definida 
    anteriormente

    Parameters
    ----------
    peso : float
        DESCRIPTION. Peso de la persona en kilogramos.
    altura : float
        DESCRIPTION. Altura de la persona en centímetros.
    edad : int
        DESCRIPTION. Edad de la persona en años.
    valor_genero : float
        DESCRIPTION. Valor que varía según el género de la persona: en caso de ser masculino 
        debe ser 5 y en caso de ser femenino debe ser -161

    Returns
    -------
    float
        DESCRIPTION. La cantidad de calorías que la persona quema en reposo

    """
    
    # Calcular tasa metobólica basal
    
    TMB = (10*peso)+(6.25*altura)-(5*edad)+ valor_genero
    
    # Retonar el valor de la tasa metabólica basal
    return TMB

def calcular_calorias_en_activivdad(peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)->float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo
    (esto es, su tasa metabólica basal), a partir de la ecuación definida 
    anteriormente

    Parameters
    ----------
    peso : float
        DESCRIPTION. Peso de la persona en kilogramos.
    altura : float
        DESCRIPTION. Altura de la persona en metros.
    edad : int
        DESCRIPTION. Edad de la persona en años.
    valor_genero : float
        DESCRIPTION. Valor que varía según el género de la persona: en caso de ser masculino 
        debe ser 5 y en caso de ser femenino debe ser -161
    valor_actividad: float
        DESCRIPTION: Valor que depende de la actividad física semanal:
        • 1.2: poco o ningún ejercicio
        • 1.375: ejercicio ligero (1 a 3 días a la semana)
        • 1.55: ejercicio moderado (3 a 5 días a la semana)
        • 1.725: deportista (6 -7 días a la semana)
        • 1.9: atleta (entrenamientos mañana y tarde)

    Returns
    -------
    float
        DESCRIPTION. La cantidad de calorías que una persona quema, al realizar algún tipo de 
        actividad física semanalmente.

    """
    
    # Calcular tasa metobólica basal
    
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    # Calcular TMB según actividad física
    
    TMB_AF = TMB * valor_actividad
    
    # Retonar el valor de la tasa metabólica basal según actividad física
    return TMB_AF

def consumo_calorias_recomendado_para_adelgazar(peso: float, altura: float, edad: int, valor_genero: float)->str:
    """
    

    Parameters
    ----------
    peso : float
        DESCRIPTION. Peso de la persona en kilogramos.
    altura : float
        DESCRIPTION. Altura de la persona en metros.
    edad : int
        DESCRIPTION. Edad de la persona en años.
    valor_genero : float
        DESCRIPTION. Valor que varía según el género de la persona: en caso de ser masculino 
        debe ser 5 y en caso de ser femenino debe ser -161

    Returns
    -------
    str
        DESCRIPTION. Una cadena indicando el rango de calorías que una persona debe consumir 
        si desea adelgazar. El formato de la cadena debe ser: "Para adelgazar es 
        recomendado que consumas entre: XXX y ZZZ calorías al día.". Siendo XXX 
        el rango inferior y ZZZ el rango superior

    """
    TMB = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    
    Cal_Min = (80 * TMB) / 100
    Cal_Max = (85 * TMB) / 100
    
    CPAd =  str (str("Para adelgazar es recomendable que consumas entre ")+ str(round(Cal_Min, 2))+ str(" y ")+ str(round(Cal_Max, 2))+ str(" calorias al día."))
    
    return CPAd


    