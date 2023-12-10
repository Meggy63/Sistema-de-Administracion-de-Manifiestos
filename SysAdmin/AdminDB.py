class AdminDB():
    def __init__(self,conexion,cursor):
        self.conexion = conexion
        self.cursor = cursor
    def consultarConductores(self):
        rows = self.cursor.execute("SELECT * FROM PERSONAL").fetchall()
        return rows
    def consultarCarros(self):
        rows = self.cursor.execute("SELECT * FROM CARROS").fetchall()
        return rows
    def consultarCiudades(self):
        rows = self.cursor.execute("SELECT * FROM ORIGEN_DESTINO").fetchall()
        return rows
    def consultarEmpresa(self):
        rows = self.cursor.execute("SELECT * FROM EMPRESAS").fetchall()
        return rows

