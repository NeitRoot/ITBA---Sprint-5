class Cliente:
    def __init__(self, nombre, apellido, dni, codCliente):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__codCliente = codCliente

    def __str__(self):
        return ("Bienvenido " + self.__nombre + " " + self.__apellido)
