class Cliente:
    def __init__(self, nombre, apellido, dni, codCliente):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__codCliente = codCliente

    def calcularMontoTotal(precioDolar, cantidad):
        impuestoPais = 0.3
        impuestoGanancias = 0.35

        montoOperacion = cantidad * precioDolar
        pais = montoOperacion * impuestoPais
        ganancias = montoOperacion * impuestoGanancias

        total = montoOperacion + pais + ganancias

        return total

    def descontarComision(monto, porcentajeComision):
        comision = (porcentajeComision / 100) * monto
        montoConDescuento = monto - comision
        return montoConDescuento

    def CalcularPlazoFijo(monto, interes):
        montoConIntereses = monto * (interes + 1)
        return montoConIntereses
