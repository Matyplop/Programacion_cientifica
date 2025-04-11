from abc import ABC, abstractmethod
from MetaIndicador import MetaIndicador


class IndicadorPaciente(ABC, metaclass=MetaIndicador):
    """
    Clase abstracta para definir indicadores a aplicar en los pacientes.
    Cada indicador debe implementar el método 'calcular'.
    """
    @abstractmethod
    def calcular(self, paciente):
        pass