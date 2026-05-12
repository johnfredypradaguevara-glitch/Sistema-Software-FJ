from cliente import Cliente
from servicios_especializados import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reserva
import logging
import sistema

# 1 Cliente válido
try:
    cliente1 = Cliente(1, "Ana", "ana@gmail.com")
except Exception as e:
    logging.error(e)

# 2 Cliente inválido
try:
    cliente2 = Cliente(2, "Luis", "correo_invalido")
except Exception as e:
    logging.error(e)

# 3 Servicio válido
servicio1 = ServicioSala("Sala VIP", 50)

# 4 Reserva válida
try:
    reserva1 = Reserva(cliente1, servicio1, 2)
    print("Costo:", reserva1.confirmar())
except Exception as e:
    logging.error(e)

# 5 Reserva inválida (duración negativa)
try:
    reserva2 = Reserva(cliente1, servicio1, -3)
    reserva2.confirmar()
except Exception as e:
    logging.error(e)

# 6 Servicio equipo
servicio2 = ServicioEquipo("Proyector", 30)

# 7 Reserva válida
try:
    reserva3 = Reserva(cliente1, servicio2, 3)
    print("Costo:", reserva3.confirmar())
except Exception as e:
    logging.error(e)

# 8 Asesoría con descuento
servicio3 = ServicioAsesoria("Consultoría", 100)
print("Costo asesoría:", servicio3.calcular_costo(2, 0.1))

# 9 Cancelación
reserva1.cancelar()

# 10 Intento incorrecto
try:
    reserva4 = Reserva(cliente1, servicio3, 0)
    reserva4.confirmar()
except Exception as e:
    logging.error(e)