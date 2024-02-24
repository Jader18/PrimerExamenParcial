import clases as c
import os 

agendas = c.Agenda()

def ingresarContacto():
    try:
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        telefono = input("Telefono: ")
        email = input("Email: ")

        contacto = c.Contacto(nombre, apellido, telefono, email)
        agendas.agregar_contacto(contacto)
    except:
        print("Error inesperado")

def menu():
    while True:
        os.system("cls || clear")
        print("Cantidad de contactos: " , str(len(agendas.contactos)))
        print("1. Ingresar contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        try:
            opcion = int(input("Opción: "))
            if opcion == 1:
                ingresarContacto()
            elif opcion == 2:
                print("ver productos")
                agendas.mostrar_contacto()
                os.system("pause")
            elif opcion == 3:
                break
            else:
                print("Opción no válida")
        except:
            print("Error: Ingrese un número entero")

def main():
    menu()

if __name__ == "__main__":
    main()