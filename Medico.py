class Medico:
    """
    Clase para representar a un médico con nombre y especialidad.
    """
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
