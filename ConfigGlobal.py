from datetime import datetime



class ConfigGlobal:

    """
    Clase Singleton para administrar la configuración global
    y el registro de eventos (logs) en el sistema.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigGlobal, cls).__new__(cls)
            cls._instance._log_nivel = "INFO"
            cls._instance._eventos = []
        return cls._instance

    def log(self, mensaje, nivel="INFO"):
        """
        Registra un evento en el sistema con la fecha actual y un nivel específico.
        """
        self._eventos = []  # Limpiar el historial de eventos
        evento = f"{datetime.now()} [{nivel}] {mensaje}"
        self._eventos.append(evento)
        print(evento)

    def eventos(self):
        """
        Retorna la lista de eventos registrados.
        """
        return self._eventos

    def set_log_nivel(self, nivel):
        """
        Permite actualizar el nivel de log a utilizar en la aplicación.
        """
        
        self._log_nivel = nivel

    @property
    def log_nivel(self):
        """
        Propiedad para obtener el nivel de log actual.
        """
        return self._log_nivel
