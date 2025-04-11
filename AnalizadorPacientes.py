from collections import Counter
from functools import reduce

class AnalizadorPacientes:
    """
    Clase que contiene métodos estáticos para procesar y analizar datos
    relacionados a los pacientes.
    """
    @staticmethod
    def pacientes_con_gastos_altos(pacientes, umbral):
        return list(filter(lambda p: p.total_gastado() > umbral, pacientes))

    @staticmethod
    def top_enfermedades(pacientes):
        todas = [enf for p in pacientes for enf in p.enfermedades()]
        return Counter(todas).most_common(5)

    @staticmethod
    def gasto_total_del_sistema(pacientes):
        return reduce(lambda acc, p: acc + p.total_gastado(), pacientes, 0)
