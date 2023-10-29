from Cuenta.Cuenta import Cuenta


class CuentaInversion(Cuenta):
    def __init__(self, numeroCuenta, tipoCuenta, saldo, divisa):
        super().__init__(tipoCuenta, saldo, divisa, numeroCuenta)

    def __str__(self):
        return "Cuenta: "+self.__tipoCuenta+". Saldo: "+str(self.__saldo) + " "+self.__divisa+" con id : "+str(self.__numeroCuenta)
