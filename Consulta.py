from Dinero import Dinero
from datetime import datetime


class Consulta:
    """
    Clase para modelar una consulta médica. Se utiliza __slots__ para optimizar el uso de memoria.
    """
    __slots__ = ('fecha', 'medico', 'costo', 'diagnostico')

    def __init__(self, medico, costo, diagnostico=""):
        self.fecha = datetime.now()
        self.medico = medico
        self.costo = costo if isinstance(costo, Dinero) else Dinero(costo)
        self.diagnostico = diagnostico

    def __str__(self):
        return f"{self.fecha.date()} - {self.medico.nombre} - {self.costo} - {self.diagnostico}"