from Deduccion import Deduccion
from Gastos import Gastos


class Manifiesto():
    def __init__(self, identificacion, fecha, flete, anticipo,
                  origen,destino, empresa, carro, conductor):
        self.id = identificacion
        self.fecha = fecha
        self.flete = flete
        self.anticipo = anticipo
        self.saldo = flete-anticipo
        self.gastos = None
        self.total_gastos = None
        self.ganancia_neta = None
        self.origen = origen
        self.destino = destino
        self.empresa = empresa
        self.carro = carro
        self.conductor = conductor
        self.deduccion = None




    def determinar_deduccion(self):
        deduccion=self.anticipo-self.total_gastos
        if deduccion>0:
            self.deduccion=Deduccion(self.conductor,deduccion)
        elif deduccion<0:
            self.deduccion=Deduccion("Juan",deduccion)
        else:
            self.deduccion=Deduccion("NULO",deduccion)
        if self.deduccion:
            return True
        else:
            return False

    def determinar_gastos(self,comision, parqueos, transportes, propinas,acpm,peajes,
                 lavada_brillada, cargue, descargue, montada_llantas, cumplidos):
        porcentaje=self.flete*0.1
        manifiesto=self.id
        self.gastos = Gastos(comision, parqueos, transportes, propinas,acpm,peajes,porcentaje,
                 lavada_brillada, cargue, descargue, montada_llantas, cumplidos, manifiesto)
        self.total_gastos=self.gastos.total_gastos()
        if self.gastos and self.total_gastos:
            return True
        else:
            return False
    def determinar_ganacia_neta(self):
        self.ganancia_neta=self.saldo-self.deduccion.valor
        if self.ganancia_neta:
            return True
        else:
            return False
        
