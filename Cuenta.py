class Cuenta():

    def __init__(self, numeroCuenta, tipoCuenta):
        self.__numeroCuenta = numeroCuenta
        self.__tipoCuenta = tipoCuenta

    def __str__(self):
        return ("Numero de Cuenta: " + str(self.__numeroCuenta) + " " + "Tipo de Cuenta: " + self.__tipoCuenta)
