from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod


class MetaIndicador(ABCMeta):
    """
    Metaclase que registra automáticamente cada subclase de IndicadorPaciente,
    lo que facilita la extensión y el mantenimiento del sistema.
    """
    indicadores_registrados = []

    def __new__(cls, nombre, bases, dct):
        clase = super().__new__(cls, nombre, bases, dct)
        if nombre != "IndicadorPaciente":
            cls.indicadores_registrados.append(clase)
        return clase
    

class IndicadorPaciente(ABC, metaclass=MetaIndicador):
    """
    Clase abstracta para definir indicadores a aplicar en los pacientes.
    Cada indicador debe implementar el método 'calcular'.
    """
    @abstractmethod
    def calcular(self, paciente):
        pass




class FrecuenciaConsultas(IndicadorPaciente):
    """
    Indicador que mide la frecuencia total de consultas de un paciente.
    """
    def calcular(self, paciente):
        return paciente.cantidad_consultas()
    

class MargenGasto(IndicadorPaciente):
    """
    Indicador que calcula el gasto promedio por consulta de un paciente.
    """
    def calcular(self, paciente):
        if paciente.cantidad_consultas() == 0:
            return 0
        return paciente.total_gastado() / paciente.cantidad_consultas()
