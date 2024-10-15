
class Inversor:
    def __init__(self, dni = None, nombre = None, apellido = None, email = None, telefono = None, direccion = None, contraseña = None):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.contraseña = contraseña

    def __str__(self):
        return (f"Inversor: {self.nombre} {self.apellido}\n"
                f"DNI: {self.dni}\n"
                f"Email: {self.email}\n"
                f"Teléfono: {self.telefono}\n"
                f"Dirección: {self.direccion}")
        