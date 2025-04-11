from functools import reduce


class Paciente:
    """
    Clase para representar a un paciente, utilizando encapsulamiento para sus atributos.
    Contiene métodos para agregar consultas, enfermedades y calcular gastos.
    """
    def __init__(self, nombre, rut):
        self._nombre = nombre
        self._rut = rut
        self._enfermedades = set()
        self._consultas = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def rut(self):
        return self._rut

    def agregar_enfermedad(self, enfermedad):
        
        self._enfermedades.add(enfermedad)

    def agregar_consulta(self, consulta):
        self._consultas.append(consulta)
        if consulta.diagnostico:
            self._enfermedades.add(consulta.diagnostico)

    def total_gastado(self):
        return reduce(lambda acc, c: acc + c.costo.valor(), self._consultas, 0)

    def enfermedades(self):
        return list(self._enfermedades)

    def consultas(self):
        return self._consultas

    def cantidad_consultas(self):
        return len(self._consultas)

    def medicos_que_lo_atendieron(self):
        return set(c.medico.nombre for c in self._consultas)

    def __str__(self):
        return f"{self._nombre} - RUT: {self._rut} - Enfermedades: {', '.join(self._enfermedades)}"