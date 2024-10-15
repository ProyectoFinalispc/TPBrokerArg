from repositorio.portafolioRepository import PortafolioRepository

class PortafolioService:
    portafolioRepository = PortafolioRepository()

    def consultar_portafolio (self, cuil):
        return self.portafolioRepository.obtener_portafolio(cuil)

    def crear_portafolio_serv (self, portafolio_nuevo):
        return self.portafolioRepository.crear_portafolio(portafolio_nuevo)
    