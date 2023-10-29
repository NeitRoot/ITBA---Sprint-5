from Cliente.Cliente import Cliente

from Tarjeta.Debito import Debito
from Cuenta.CAPesos import CAPesos
from Cuenta.CADolares import CADolares
from Transaccion.Transaccion import Transaccion
from datetime import datetime


class Classic(Cliente):

    def __init__(self, nombre, apellido, dni, codCliente):
        super().__init__(nombre, apellido, dni, codCliente)
        self.tipo_cliente = "Classic"
        self.limiteCajero = 10000
        self.retirosDisponibles = 5
        self.cajaDeAhorroDisponiblePesos = 1
        self.cajaDeAhorroDisponibleDolares = 1
        self.tarjetasDeDebitoDisponibles = 1

    def getInfo(self):
        print("Nombre: "+self.nombre+" "+self.apellido+"\n"
              "DNI: "+str(self.dni)+"\n"
              "Tipo de cliente: "+self.tipo_cliente)

    def altaCAPesos(self):
        if self.cajaDeAhorroDisponiblePesos > 0:
            self.CAPesos = CAPesos(
                "caja de ahorro en pesos", 0, "pesos", (100 + len(self.productos) + 1))
            self.cajaDeAhorroDisponiblePesos -= 1
            self.transaccion.append(Transaccion("aprobada", "Alta_Caja_Ahorro_Pesos", len(
                self.transaccion)+1, self.CAPesos.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            self.productos += [self.CAPesos.tipo]
        else:
            print("Máximo número de cajas de ahorro alcanzado")
            self.transaccion.append(Transaccion("rechazada", "Alta_Caja_Ahorro_Pesos", len(
                self.transaccion)+1, self.CAPesos.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaCADolares(self):
        if self.cajaDeAhorroDisponibleDolares > 0:
            self.CADolares = CADolares(
                "caja de ahorro en dolares", 0, "dolares", (100 + len(self.productos) + 1))
            self.cajaDeAhorroDisponibleDolares -= 1
            self.transaccion.append(Transaccion("aprobada", "Alta_Caja_Ahorro_Dolares", len(
                self.transaccion)+1, self.CADolares.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            self.productos += [self.CADolares.tipo]
        else:
            print("Máximo número de cajas de ahorro alcanzado")
            self.transaccion.append(Transaccion("rechazada", "Alta_Caja_Ahorro_Dolares", len(
                self.transaccion)+1, self.CADolares.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaCuentaCorrientePesos(self):
        print("El cliente no tiene acceso a cuenta corriente")
        self.transaccion.append(Transaccion("rechazada", "Alta_Cuenta_Corriente_Pesos", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaCuentaCorrienteDolares(self):
        print("El cliente no tiene acceso a cuenta corriente")
        self.transaccion.append(Transaccion("rechazada", "Alta_Cuenta_Corriente_Dolares", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaCuentaDeInversion(self):
        print("El cliente no tiene acceso a cuenta de inversión")
        self.transaccion.append(Transaccion("rechazada", "Alta_Cuenta_Inversion", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaTarjetaCredito(self, marcaTarjeta):
        print("El cliente no tiene acceso a tarjeta de crédito")
        self.transaccion.append(Transaccion("rechazada", "Alta_Tarjeta_Credito", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def altaChequera(self):
        print("El cliente no tiene acceso a chequera")
        self.transaccion.append(Transaccion("rechazada", "Alta_Chequera", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def compraTarjetaCredito(self):
        print("Error: El cliente no posee tarjeta de crédito")
        self.transaccion.append(Transaccion("rechazada", "Compra_Tarjeta_Credito", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def compraTarjetaCreditoCuotas(self):
        print("Error: El cliente no posee tarjeta de crédito")
        self.transaccion.append(Transaccion("rechazada", "Compra_Tarjeta_Credito_Cuotas", len(
            self.transaccion)+1, "N/A", "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def getSaldoCAPesos(self):
        if self.cajaDeAhorroDisponiblePesos == 0:
            print(self.CAPesos)
        else:
            return "No se ha dado de alta una caja de ahorro en pesos"

    def getSaldoCADolares(self):
        if self.cajaDeAhorroDisponibleDolares == 0:
            print(str(self.CADolares) + ". Costo mensual de mantenimiento: U$D 4")
        else:
            return "No se ha dado de alta una caja de ahorro en dolares"

    def altaTarjetaDebito(self, marcaTarjeta):
        if self.tarjetasDeDebitoDisponibles > 0:
            if (marcaTarjeta == "Visa" or marcaTarjeta == "Mastercard"):
                self.tarjetaDebito = Debito(
                    marcaTarjeta, (1000 + len(self.tarjeta)+1))
                self.tarjeta += ["Debito"]
                self.tarjetasDeDebitoDisponibles -= 1
                self.transaccion.append(Transaccion("aprobada", "Alta_Tarjeta_Debito", len(
                    self.transaccion)+1, self.CAPesos.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                print("El cliente solo tiene acceso a tarjetas Mastercard o Visa")
                self.transaccion.append(Transaccion("rechazada", "Alta_Tarjeta_Debito", len(
                    self.transaccion)+1, self.CAPesos.tipo, "N/A", datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        else:
            print("Máximo número de tarjetas de débito alcanzado")

    def getTarjetaDebito(self):
        if self.tarjetasDeDebitoDisponibles > 0:
            print(self.tarjetaDebito)
        else:
            print("No se ha dado de alta una tarjeta de débito")

    def enviarTransferencia(self, montoTransfer, monedaTransfer):
        if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
            if self.CAPesos.saldo >= montoTransfer * 1.01:
                self.CAPesos.saldo = self.CAPesos.saldo - montoTransfer * 1.01
                self.transaccion.append(Transaccion("aprobada", "Envio_Transeferencia_Pesos", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoTransfer, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                      + "Saldo actual: "+str(self.CAPesos.saldo) + " "+monedaTransfer)
            else:
                self.transaccion.append(Transaccion("rechazada", "Envio_Transeferencia_Pesos", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoTransfer, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Error: verifique la moneda y el monto a transferir ingresados")

        elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares":
            if self.CADolares.saldo >= montoTransfer * 1.01:
                self.CADolares.saldo = self.CADolares.saldo - montoTransfer * 1.01
                self.transaccion.append(Transaccion("aprobada", "Envio_Transeferencia_Dolares", len(
                    self.transaccion)+1, self.CADolares.tipo, montoTransfer, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Transferencia realizada, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.01)+" "+monedaTransfer+"\n"
                      + "Saldo actual: "+str(self.CADolares.saldo) + " "+monedaTransfer)
            else:
                self.transaccion.append(Transaccion("rechazada", "Envio_Transeferencia_Dolares", len(
                    self.transaccion)+1, self.CADolares.tipo, montoTransfer, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Error: Verifique la moneda y el monto a transferir ingresados")
        else:
            print(
                "Error: Debe dar de alta una caja de ahorro en la moneda en la que quiere enviar transferencias")

    def recibirTransferencia(self, montoTransfer, monedaTransfer):
        if self.cajaDeAhorroDisponiblePesos == 0 and monedaTransfer == "pesos":
            self.CAPesos.saldo = self.CAPesos.saldo + \
                (montoTransfer * 0.995)
            print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                  + "Saldo actual: "+str(self.CAPesos.saldo) + " "+monedaTransfer)

        elif self.cajaDeAhorroDisponibleDolares == 0 and monedaTransfer == "dolares":
            self.CADolares.saldo = self.CADolares.saldo + \
                (montoTransfer * 0.995)
            print("Transferencia recibida, monto: "+str(montoTransfer)+" "+monedaTransfer+", comision: "+str(montoTransfer * 0.005)+" "+monedaTransfer+"\n"
                  + "Saldo actual: "+str(self.CADolares.saldo) + " "+monedaTransfer)
        else:
            print(
                "Error: debe dar de alta una caja de ahorro en la moneda que quiere recibir la transferencia")

    def retiroPorCaja(self, montoRetiro, monedaRetiro):
        if self.cajaDeAhorroDisponiblePesos == 0 and monedaRetiro == "pesos":
            if montoRetiro <= self.CAPesos.saldo:
                self.CAPesos.saldo = self.CAPesos.saldo - montoRetiro
                self.transaccion.append(Transaccion("aprobada", "Retiro_Por_Caja_Pesos", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoRetiro, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Retiro por caja realizado, monto: "+str(montoRetiro) +
                      ". Saldo actual: "+str(self.CAPesos.saldo)+" "+monedaRetiro)
            else:
                self.transaccion.append(Transaccion("rechazada", "Retiro_Por_Caja_Pesos", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoRetiro, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Error: verifique la moneda y el monto a retirar ingresados")

        elif self.cajaDeAhorroDisponibleDolares == 0 and monedaRetiro == "dolares":
            if montoRetiro <= self.CADolares.saldo:
                self.CADolares.saldo = self.CADolares.saldo - montoRetiro
                self.transaccion.append(Transaccion("aprobada", "Retiro_Por_Caja_Dolares", len(
                    self.transaccion)+1, self.CADolares.tipo, montoRetiro, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Retiro por caja realizado, monto: "+str(montoRetiro) +
                      ". Saldo actual: "+str(self.CADolares.saldo)+" "+monedaRetiro)
            else:
                self.transaccion.append(Transaccion("rechazada", "Retiro_Por_Caja_Dolares", len(
                    self.transaccion)+1, self.CADolares.tipo, montoRetiro, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Error: verifique la moneda y el monto a retirar ingresados")
        else:
            print(
                "Debe dar de alta una caja de ahorro en la moneda deseada para hacer retiros por caja")

    def retiroCajero(self, montoCajero):
        if self.cajaDeAhorroDisponiblePesos == 0:
            if montoCajero <= self.limiteCajero and montoCajero <= self.CAPesos.saldo and self.retirosDisponibles > 0:
                self.CAPesos.saldo -= montoCajero
                self.limiteCajero -= montoCajero
                self.retirosDisponibles -= 1
                self.transaccion.append(Transaccion("aprobada", "Retiro_Cajero_Automatico", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoCajero, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Retiro por cajero, monto retirado: "+str(montoCajero)+"\n" +
                      "Saldo disponible: "+str(self.CAPesos.saldo)+"\n" +
                      "Limite de retiro por cajero disponible: "+str(self.limiteCajero)+"\n" +
                      "Retiros diarios disponibles: "+str(self.retirosDisponibles))
            elif montoCajero <= self.limiteCajero and montoCajero > self.CAPesos.saldo and self.retirosDisponibles > 0:
                print("Error: Saldo insuficiente")
                self.transaccion.append(Transaccion("rechazada", "Retiro_Cajero_Automatico", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoCajero, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            else:
                print(
                    "Error: Límite diario de retiro de cajero alcanzado, regrese mañana")
                self.transaccion.append(Transaccion("rechazada", "Retiro_Cajero_Automatico", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoCajero, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
        else:
            print("Debe dar de alta una caja de ahorro en pesos para retirar por cajero")

    def compraDolar(self, cantidadDolares):
        if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
            montoPesos = Cliente.calcularMontoTotal(350, cantidadDolares)
            if self.CAPesos.saldo >= montoPesos:
                self.CAPesos.saldo -= montoPesos
                self.CADolares.saldo += cantidadDolares
                self.transaccion.append(Transaccion("aprobada", "Compra_Dolar", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoPesos, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Operación realizada: "+str(cantidadDolares) +
                      " dólares comprados por "+str(montoPesos)+" pesos")
            else:
                self.transaccion.append(Transaccion("rechazada", "Compra_Dolar", len(
                    self.transaccion)+1, self.CAPesos.tipo, montoPesos, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Saldo insuficiente")
        else:
            print(
                "Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

    def ventaDolar(self, cantidadDolares):
        if self.cajaDeAhorroDisponiblePesos == 0 and self.cajaDeAhorroDisponibleDolares == 0:
            montoPesos = 350 * cantidadDolares
            if self.CADolares.saldo >= cantidadDolares:
                self.CAPesos.saldo += montoPesos
                self.CADolares.saldo -= cantidadDolares
                self.transaccion.append(Transaccion("aprobada", "Venta_Dolar", len(
                    self.transaccion)+1, self.CADolares.tipo, cantidadDolares, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Operación realizada: "+str(cantidadDolares) +
                      " dólares vendidos por "+str(montoPesos)+" pesos")
            else:
                self.transaccion.append(Transaccion("rechazada", "Venta_Dolar", len(
                    self.transaccion)+1, self.CADolares.tipo, cantidadDolares, datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
                print("Saldo insuficiente")
        else:
            print(
                "Error: Debe poseer caja de ahorro en pesos y dólares para realizar esta transacción")

    def mostrartransaccion(self):
        for i in range(len(self.transaccion)):
            print(str(self.transaccion[i])+"\n")
