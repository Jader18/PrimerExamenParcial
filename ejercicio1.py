#Crear una calculadora que pueda realizar operaciones basicas como suma, resta, multiplicacion, division. 
#Utiliza funciones para cada operacion y permite al usuario elegir la operacion deseada 
#mediante una sentencia de control. 
import os 

def suma(num1, num2): 
    answer = num1 + num2
    print("La suma es: ", answer)
    return 0

def resta(num1, num2): 
    answer = num1 - num2
    print("La resta es: ", answer)

    return 0

def multiplicacion(num1, num2): 
    answer = num1 * num2
    print("La multiplicacion es: ", answer)

    return 0

def division(num1, num2): 
    answer = num1 / num2
    print("La division es: ", answer)

    return 0


def menu():
    while True:
        print("*** Menu de opciones ***")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                suma(num1, num2)
                os.system("pause")
                 
                        
            elif opcion == 2:
                resta(num1, num2)
                os.system("pause")

                
            elif opcion == 3:
                multiplicacion(num1, num2)
                os.system("pause")

                
            elif opcion == 4:
                division(num1, num2)
                os.system("pause")

            
            elif opcion == 5:

                break

            else:
                print("Opción no válida")

        except:
            print("Error: Ingrese un número entero")


num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

menu()


