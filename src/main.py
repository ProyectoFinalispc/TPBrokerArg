from servicios.inversor_serv import InversorService
from servicios.portafolio_serv import PortafolioService
from modelos.inversor import Inversor
from modelos.portafolio import Portafolio

def menu():
    print("1. Mostrar inversor")
    print("2. Crear inversor")
    print("3. Salir")

def main():
    inversor_service = InversorService()
    portafolio_service = PortafolioService()

    inversorAux = Inversor()

    while True:
        menu()
        choice = input("Selecciona una opción: ")

        if choice == "1":
            inversorAux.dni = input("Ingrese el dni a consultar: ")
            inversorAux = inversor_service.consultar_inversor(inversorAux.dni)

            if inversorAux:
                print(inversorAux)
            else:
                print("Inversor no encontrado.")

        elif choice == "2":
            inversor_nuevo = Inversor()

            inversor_nuevo.dni = input("Ingrese su dni: ")
            inversor_nuevo.nombre = input("Ingrese su nombre: ")
            inversor_nuevo.apellido = input("Ingrese su apellido: ")
            inversor_nuevo.email = input("Ingrese su email: ")
            inversor_nuevo.telefono = input("Ingrese su telefono: ")
            inversor_nuevo.direccion = input("Ingrese su direccion: ")
            inversor_nuevo.contraseña = input("Ingrese su contraseña: ")

            creado = inversor_service.crear_inversor_serv(inversor_nuevo)

            if creado:
                print("Se creo al nuevo inversor")

                portafolio_nuevo = Portafolio()
                portafolio_nuevo.descripcion = input("Ingrese una descripcion para su portafolio: ")
                portafolio_nuevo.dni = inversor_nuevo.dni

                portafolio_creado = portafolio_service.crear_portafolio_serv(portafolio_nuevo)

                if portafolio_creado:
                    print("Se creo su portafolio")
                else:
                    print("Error al crear el portafolio")

            else:
                print("no se pudo crearlo")

        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
