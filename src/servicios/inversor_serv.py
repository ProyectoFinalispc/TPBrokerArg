from repositorio.inversorRepository import InversorRepository

class InversorService:
    inversorRepository = InversorRepository()

    def consultar_inversor (self, cuil):
        return self.inversorRepository.obtener_inversor(cuil)

    def crear_inversor_serv (self, inversor_nuevo):
        return self.inversorRepository.crear_inversor(inversor_nuevo)