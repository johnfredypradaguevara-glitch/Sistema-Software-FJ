from servicio import Servicio

class ServicioSala(Servicio):

    def calcular_costo(self, horas):
        return self._precio_base * horas

    def describir_servicio(self):
        return f"Sala reservada por ${self._precio_base} por hora"


class ServicioEquipo(Servicio):

    def calcular_costo(self, dias):
        return self._precio_base * dias

    def describir_servicio(self):
        return f"Equipo alquilado por ${self._precio_base} por día"


class ServicioAsesoria(Servicio):

    def calcular_costo(self, horas, descuento=0):
        total = self._precio_base * horas
        return total - (total * descuento)

    def describir_servicio(self):
        return f"Asesoría especializada ${self._precio_base} por hora"