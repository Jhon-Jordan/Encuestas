import sys
import pyodbc as bd

class Conexion:
    _SERVIDOR = '192.168.100.41\\JHON-DESKTOP\\JORDAN'
    _BBDD = 'encuestas'
    _USUARIO = 'grupo6segundo'
    _PASSWORD = 'grupo6segundo123'
    _conexion = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    f'UID={cls._USUARIO};'
                    f'PWD={cls._PASSWORD};'
                    'Network=dbmssocn;'
                    'TrustServerCertificate=yes;'
                )
            except Exception as e:
                print(f'Ocurrió una excepción al obtener la conexión: {e}')
                sys.exit()
        return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        try:
            return cls.obtenerConexion().cursor()
        except Exception as e:
            print(f'Ocurrió una excepción al obtener el cursor: {e}')
            sys.exit()

if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())
