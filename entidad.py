from abc import ABC, abstractmethod

class Entidad(ABC):
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre

    @abstractmethod
    def mostrar_informacion(self):
        pass