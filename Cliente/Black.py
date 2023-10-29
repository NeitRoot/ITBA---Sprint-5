from Cliente.Cliente import Cliente

from Tarjeta.Debito import Debito
from Tarjeta.Credito import Credito
from Cuenta.CAPesos import CAPesos
from Cuenta.CADolares import CADolares
from Cuenta.CCPesos import CCPesos
from Cuenta.CCDolares import CCDolares
from Cuenta.CuentaInversion import CuentaInversion
from Cuenta.Chequera import Chequera
from Transaccion.Transaccion import Transaccion
from datetime import datetime


class Black(Cliente):

    def __init__(self, nombre, apellido, dni, codCliente):
        super().__init__(nombre, apellido, dni, codCliente)
        self.tipo_cliente = "Black"
        self.limiteCajero = 100000
        self.cuentasCorrientesDisponibles = 3
        self.cuentaInversionesDisponibles = 2
        self.chequerasDisponibles = 2
        self.tarjetasCredito = []
        self.tarjetasDebito = []
        # Tarjetas de crédito y débito separadas
        # Tiene la posibilidad de hasta 5 cajas de ahorro, usamos una lista para almacenarlas
        self.cajasAhorro = []
        self.tarjetas = []
        self.productos = []
        self.transacciones = []
