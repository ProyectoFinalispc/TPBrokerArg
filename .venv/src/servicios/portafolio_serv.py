from src.repositorio.portafolioRepository import PortafolioRepository

class PortafolioService:
    portafolioRepository = PortafolioRepository()

    def consultar_portafolio (self, dni):
        return self.portafolioRepository.obtener_portafolio(dni)

    def crear_portafolio_serv (self, portafolio_nuevo):
        return self.portafolioRepository.crear_portafolio(portafolio_nuevo)
    