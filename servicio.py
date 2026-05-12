from abc import ABC, abstractmethod

class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass