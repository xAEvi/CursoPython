class Vehiculo:
    tipo = None
    ruedas = None
    velocidad_maxima = None

    def __init__(self, tipo, ruedas, velocidad_maxima):
        self.tipo = tipo
        self.ruedas = ruedas
        self.velocidad_maxima = velocidad_maxima

    def __str__(self):
        return f'Tipo: {self.tipo}\nRuedas: {self.ruedas}\nVelocidad Máxima: {self.velocidad_maxima}\n'