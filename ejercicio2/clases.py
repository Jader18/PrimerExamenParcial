

class Contacto:
    def __init__(self, nombre, apellido, telefono, email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email



    def __str__(self):
        return f"""Contacto: {self.nombre}, 
        Apellido: {self.apellido}, 
        Telefono: {self.telefono}, 
        Email: {self.email}"""

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_contacto(self):
        for contacto in self.contactos:
            print(contacto)