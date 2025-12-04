from abc import ABC, abstractmethod

class Socio(ABC):
    def __init__(self, tipo, numero_socio, nombre_titular, integrantes_adicionales, activo):
        self.tipo = tipo
        self.numero_socio = numero_socio
        self.nombre_titular = nombre_titular
        self.integrantes_adicionales = integrantes_adicionales
        self.activo = activo
    
    @abstractmethod
    def calcular_cuota_mensual(self):
        pass
    
    @property
    @abstractmethod
    def nombre_tipo(self):
        pass
    
    def __str__(self):
        return f"{self.nombre_tipo} - {self.numero_socio}: {self.nombre_titular}"