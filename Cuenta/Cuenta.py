class Cuenta():

    def __init__(self, numeroCuenta, tipoCuenta, saldo, divisa):
        self.__numeroCuenta = numeroCuenta
        self.__tipoCuenta = tipoCuenta
        self.__saldo = saldo
        self.__divisa = divisa

    def __str__(self):
        return ("Numero de Cuenta: " + str(self.__numeroCuenta) + " " + "Tipo de Cuenta: " + self.__tipoCuenta + "Saldo: " + str(self.__saldo) + "Moneda: " + self.__divisa)
