from IndicadorPaciente import IndicadorPaciente



class MargenGasto(IndicadorPaciente):
    """
    Indicador que calcula el gasto promedio por consulta de un paciente.
    """
    def calcular(self, paciente):
        if paciente.cantidad_consultas() == 0:
            return 0
        return paciente.total_gastado() / paciente.cantidad_consultas()
