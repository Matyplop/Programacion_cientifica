from IndicadorPaciente import IndicadorPaciente



class FrecuenciaConsultas(IndicadorPaciente):
    """
    Indicador que mide la frecuencia total de consultas de un paciente.
    """
    def calcular(self, paciente):
        return paciente.cantidad_consultas()