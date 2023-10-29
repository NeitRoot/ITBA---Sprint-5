class Credito():

    def __init__(self, marca, limite, limiteCuotas, id):
        self.marca = marca
        self.limite = limite
        self.limiteCuotas = limiteCuotas
        self.tipo = "Credito"
        self.extensiones = 0
        self.id = id

    def __str__(self):
        return ("Tarjeta de "+self.tipo + " -Marca "+self.marca+"\n" +
                "posee límite de "+str(self.limite)+" en un pago y "+str(self.limiteCuotas)+" en cuotas"+"\n" +
                "Cantidad de extensiones: "+str(self.extensiones) + ". Número de id: "+str(self.id))
