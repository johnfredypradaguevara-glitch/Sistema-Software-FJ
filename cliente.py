from entidad import Entidad

class Cliente(Entidad):

    def __init__(self, id, nombre, correo):
        super().__init__(id, nombre)
        self.set_correo(correo)

    def set_correo(self, correo):
        if "@" not in correo:
            raise ValueError("El correo electrónico es inválido.")
        self._correo = correo

    def get_correo(self):
        return self._correo

    def mostrar_informacion(self):
        return f"Cliente: {self._nombre} - Correo: {self._correo}"