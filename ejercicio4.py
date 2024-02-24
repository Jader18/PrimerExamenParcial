#Leer la edad de una persona, decir si es mayor o menor de edad. 

import os
os.system("cls || clear")

#Funcion para determinar si es mayor o menor de edad
def calcularEdad(edad):
    
    try:
        if edad >= 18:
            print("Es mayor de edad")
            return 0
        else:
            print("Es menor de edad")
            return 0
    except:
        print("Error: Ingrese un número entero")
        return 0

edad = int(input("Ingresa la Edad: "))

calcularEdad(edad)


    