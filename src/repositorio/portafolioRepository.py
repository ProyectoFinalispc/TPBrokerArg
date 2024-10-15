from repositorio.database import DatabaseConnection
from modelos.portafolio import Portafolio

class PortafolioRepository:
    def crear_portafolio(self, nuevo_portafolio):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        query = """
            INSERT INTO portafolio (dni, descripcion, saldo_actual) 
            VALUES (%s, %s, 1000000)
        """

        try:
            cursor.execute(query, (
                nuevo_portafolio.dni, nuevo_portafolio.descripcion
            ))
            connection.commit()
            return True

        except Exception as e:
            print(f"Error al crear el portafolio: {e}")
            connection.rollback()
            return False

        finally:
            cursor.close()
            connection.close()