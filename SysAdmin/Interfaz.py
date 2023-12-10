import sqlite3
import streamlit as st

from AdminDB import AdminDB


# Función para establecer la conexión con la base de datos SQLite
def conectar_bd():
    conn = sqlite3.connect('C:\\Users\\DELL\\Documents\\GitHub\\Sistema-de-Administracion-de-Manifiestos\\SysAdmin\\DB_TRANSPORTES_CORREA.db')
    return conn

class Interfaz():
    def __init__(self, conexion, cursor):
        self.conexion = conexion
        self.cursor = cursor


    def inicio_sesion(self):
        if not st.session_state["loggedin"]:
            with loginSection:
                st.title("Sistema de Administración de Manifiestos")

                # Obtener credenciales del usuario
                username = st.text_input("Usuario")
                password = st.text_input("Contraseña", type="password")

                # Verificar las credenciales
                if st.button("Ingresar"):
                    if self.verificar_credenciales(username, password):
                        st.session_state["loggedin"]=True
                        st.rerun()
                    else:
                        st.error("Credenciales incorrectas. Por favor, inténtalo de nuevo.")

    def verificar_credenciales(self, usuario, contrasena):
        # Consulta SQL para verificar las credenciales
        query = 'SELECT * FROM USUARIOS WHERE Usuario=? AND Contrasena=?'
        self.cursor.execute(query, (usuario, contrasena))
        resultado = self.cursor.fetchone()
        return resultado is not None

    def inicio(self):
        with inicioSection:
            st.title("TRANSPORTES CORREA")

            if st.button("Ingresar Manifiesto"):
                st.session_state["ingreso"]=True
                st.rerun()
            if st.button("Buscador"):
                st.session_state["buscador"] = True
                st.rerun()
            if st.button("Pagos Pendientes"):
                st.session_state["pago"] = True
                st.rerun()

    def ingresar_manifiesto(self):
        with ingresoSection:
            admin=AdminDB(self.conexion,self.cursor)
            st.title("INGRESAR NUEVO MANIFIESTO")
            conductores=[tupla[0] for tupla in admin.consultarConductores()]
            conductor= st.selectbox('Seleccione un Conductor', conductores)
            carros=[tupla[0] for tupla in admin.consultarCarros()]
            carro=st.selectbox('Seleccione un Carro', carros)
            fecha = st.date_input('Fecha ')
            ciudades=[tupla[0] for tupla in admin.consultarCiudades()]
            origen=st.selectbox('Seleccione un Origen',ciudades)
            destino=st.selectbox('Seleccione un Destino', ciudades)
            empresas=[tupla[0] for tupla in admin.consultarEmpresa()]
            empresa=st.selectbox('Seleccione una Empresa', empresas)
            manifiesto=st.text_input('Escribe el número de manifiesto')
            flete=st.text_input('Escribe el flete correspondiente')
            anticipo=st.text_input('Escribe el anticipo correspondiente')
            if st.button("Ingresar Gastos"):
                acpm=st.text_input("GASTO ACPM")
                peajes=st.text_input("GASTO PEAJES")
                porcentaje=st.text_input("GASTO PORCENTAJE")
                comision=st.text_input("GASTO COMISION")
                parqueos=st.text_input("GASTO PARQUEOS")
                transportes=st.text_input("GASTO TRANSPORTES")
                propinas=st.text_input("GASTO PROPINAS")
                lavada_brillada=st.text_input("GASTO LAVADA Y BRILLADA")
                cargue=st.text_input("CARGUE")
                descargue=st.text_input("GASTO DESCARGUE")
                montada=st.text_input("GASTO MONTADA LLANTAS")
                cumplidos=st.text_input("GASTO CUMPLIDOS")
            if st.button("Registrar Manifiesto"):
                """ Aqui iria una confirmacion antes de alterar la base de datos. la idea es primero manejar
                el objeto y despues manejar el cambio confirmado en base de datos"""
            if st.button("Volver a inicio"):
                st.session_state["ingreso"]=False
                st.rerun()

    def buscador(self):
        with buscadorSection:
            st.write("Buscador")
            if st.button("Volver a inicio"):
                st.session_state["buscador"]=False
                st.rerun()

    def pagos_pendientes(self):
        with buscadorSection:
            st.write("Pagos Pendientes")
            if st.button("Volver a inicio"):
                st.session_state["pago"]=False
                st.rerun()

if __name__ == "__main__":
    conexion = conectar_bd()
    cursor = conexion.cursor()
    interfaz = Interfaz(conexion, cursor)

    # Creando contenedores para mostrar el contenido de la app
    loginSection = st.container()
    inicioSection = st.container()
    ingresoSection = st.container()
    buscadorSection = st.container()
    pagoSection = st.container()

    # Manejo de transición en inicio de sesión
    with loginSection:
        if "loggedin" not in st.session_state:
            st.session_state["loggedin"] = False
            st.session_state["ingreso"] = False
            st.session_state["buscador"] = False
            st.session_state["pago"] = False
            interfaz.inicio_sesion()
        else:
            if st.session_state["loggedin"] and not st.session_state["ingreso"] and not st.session_state[
                    "buscador"] and not st.session_state["pago"]:
                interfaz.inicio()
            if st.session_state["loggedin"] and st.session_state["ingreso"]:
                interfaz.ingresar_manifiesto()
            if st.session_state["loggedin"] and st.session_state["buscador"]:
                interfaz.buscador()
            if st.session_state["loggedin"] and st.session_state["pago"]:
                interfaz.pagos_pendientes()


            else:
                interfaz.inicio_sesion()





