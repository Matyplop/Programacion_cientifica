from abc import ABCMeta, abstractmethod



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