from excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ReservaError("Duración inválida.")

            costo = self.servicio.calcular_costo(self.duracion)
            self.estado = "Confirmada"
            return costo

        except Exception as e:
            raise ReservaError("Error al confirmar la reserva.") from e

        finally:
            print("Proceso de confirmación finalizado.")

    def cancelar(self):
        self.estado = "Cancelada"