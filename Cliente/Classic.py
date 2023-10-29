from Cliente.Cliente import Cliente


class Classic(Cliente):

    def __init__(self, nombre, apellido, dni, codCliente):
        super().__init__(nombre, apellido, dni, codCliente)
        self.tipo_cliente = "Classic"
        self.limiteCajero = 10000
        self.retirosDisponibles = 5
        self.cajaDeAhorroDisponiblePesos = 1
        self.cajaDeAhorroDisponibleDolares = 1
        self.tarjetasDeDebitoDisponibles = 1
