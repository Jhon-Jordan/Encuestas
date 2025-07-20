from src.datos.conexion import Conexion
from src.dominio.encuestas import Encuesta


class EncuestaDao:
    _ERROR = -1
    _INSERT = ("INSERT INTO Encuestas(codigo, nombre_cliente, tipo_servicio, correo, telefono, "
               "pregunta_1, pregunta_2, pregunta_3, fecha_registro) "
               "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")

    _SELECT = ("SELECT codigo, nombre_cliente, tipo_servicio, correo, telefono, "
               "pregunta_1, pregunta_2, pregunta_3, fecha_registro FROM Encuestas WHERE codigo = ?")

    _UPDATE = ("UPDATE Encuestas SET nombre_cliente=?, tipo_servicio=?, correo=?, telefono=?, "
               "pregunta_1=?, pregunta_2=?, pregunta_3=?, fecha_registro=? WHERE codigo = ?")

    _DELETE = "DELETE FROM Encuestas WHERE codigo = ?"

    @classmethod
    def insertar_encuesta(cls, encuesta):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    encuesta.codigo,
                    encuesta.nombre_cliente,
                    encuesta.tipo_servicio,
                    encuesta.correo,
                    encuesta.telefono,
                    encuesta.pregunta_1,
                    encuesta.pregunta_2,
                    encuesta.pregunta_3,
                    encuesta.fecha_registro
                )
                registros = cursor.execute(cls._INSERT, datos)
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al insertar encuesta: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_encuesta(cls, codigo):
        try:
            with Conexion.obtenerCursor() as cursor:
                registro = cursor.execute(cls._SELECT, (codigo,)).fetchone()

                if not registro:
                    return None

                return Encuesta(
                    codigo=registro[0],
                    nombre_cliente=registro[1],
                    tipo_servicio=registro[2],
                    correo=registro[3],
                    telefono=registro[4],
                    pregunta_1=registro[5],
                    pregunta_2=registro[6],
                    pregunta_3=registro[7],
                    fecha_registro=registro[8]
                )
        except Exception as e:
            print(f"Error al seleccionar encuesta: {e}")
            return None

    @classmethod
    def actualizar_encuesta(cls, encuesta):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    encuesta.nombre_cliente,
                    encuesta.tipo_servicio,
                    encuesta.correo,
                    encuesta.telefono,
                    encuesta.pregunta_1,
                    encuesta.pregunta_2,
                    encuesta.pregunta_3,
                    encuesta.fecha_registro,
                    encuesta.codigo
                )
                registros = cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al actualizar encuesta: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR

    @classmethod
    def eliminar_encuesta(cls, codigo):
        try:
            with Conexion.obtenerCursor() as cursor:
                registros = cursor.execute(cls._DELETE, (codigo,))
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al eliminar encuesta: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR
