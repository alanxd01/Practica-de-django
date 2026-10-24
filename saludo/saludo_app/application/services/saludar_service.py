from saludo_app.application.ports.saludar_use_case import SaludarUseCase
from saludo_app.domain.persona import generar_saludo

class SaludarService(SaludarUseCase):
    def ejecutar(self, nombre: str) -> str:
        return generar_saludo(nombre)