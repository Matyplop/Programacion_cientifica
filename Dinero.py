class Dinero:
    """
    Clase para representar operaciones financieras.
    Permite la sobrecarga de operadores para facilitar cálculos monetarios.
    """
    def __init__(self, monto):
        self.monto = monto

    def __add__(self, otro):
        return Dinero(self.monto + otro.monto)

    def __sub__(self, otro):
        return Dinero(self.monto - otro.monto)

    def __mul__(self, factor):
        return Dinero(self.monto * factor)

    def __str__(self):
        return f"${self.monto:,.2f}"

    def valor(self):
        return self.monto