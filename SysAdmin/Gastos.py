class Gastos():
    def __init__(self, comision, parqueos, transportes, propinas,acpm,peajes,porcentaje,
                 lavada_brillada, cargue, descargue, montada_llantas, cumplidos, manifiesto):
        self.acpm = acpm
        self.peajes = peajes
        self.porcentaje = porcentaje
        self.comision = comision
        self.parqueos = parqueos
        self.transportes = transportes
        self.propinas = propinas
        self.lavada_brillada = lavada_brillada
        self.cargue = cargue
        self.descargue = descargue
        self.montada_llantas = montada_llantas
        self.cumplidos = cumplidos
        self.manifiesto = manifiesto

    def total_gastos(self):
        return (self.acpm + self.peajes + self.porcentaje + self.comision +
                self.parqueos + self.transportes + self.propinas +
                self.lavada_brillada + self.cargue + self.descargue +
                self.montada_llantas + self.cumplidos)

