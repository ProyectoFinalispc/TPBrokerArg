from src.repositorio.database import DatabaseConnection
from src.modelos.inversor import Inversor

class InversorRepository:
    def obtener_inversor(self, id_inversor):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = "SELECT * FROM inversores WHERE dni = %s"
        
        try:
            cursor.execute(query, (id_inversor,))
            resultado = cursor.fetchone()

            if resultado:
                return Inversor(
                    dni=resultado[0],
                    nombre=resultado[1],
                    apellido=resultado[2],
                    email=resultado[3],
                    telefono=resultado[4],
                    direccion=resultado[5],
                    contraseña=resultado[6]
                )
            return None

        except Exception as e:
            print(f"Error al obtener el inversor: {e}")
            return None

        finally:
            cursor.close()
            connection.close()

    def crear_inversor(self, nuevo_inversor):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
            INSERT INTO inversores (dni, nombre, apellido, email, telefono, direccion, contraseña) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        try:
            cursor.execute(query, (
                nuevo_inversor.dni, nuevo_inversor.nombre, nuevo_inversor.apellido,
                nuevo_inversor.email, nuevo_inversor.telefono, nuevo_inversor.direccion, nuevo_inversor.contraseña
            ))
            connection.commit()
            return True

        except Exception as e:
            print(f"Error al crear el inversor: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()
