class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if(color in ["rojo", "verde", "amarillo", "negro", "blanco"]):
            self.color = color
        else:
            print("Color no disponible")


class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        k = 0
        for i in self.asientos:
            if isinstance(i, Asiento):
                k += 1
        return k

    def verificarIntegridad(self):
        for i in self.asientos:
            if(i == None):
                pass
            elif(i.registro != self.registro | i.registro != self.motor.registro | self.registro != self.motor.registro):
                return "Las piezas no son originales"
            else:
                return "Auto original"


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, newregistro):
        self.registro = newregistro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo
        else:
            print("Tipo de motor no disponible")
