import re
from datetime import datetime
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QIntValidator
from src.UI.vtnEncuestas import Ui_Encuestas
from src.dominio.encuestas import Encuesta
from src.datos.EncuestasDao import EncuestaDao

class EncuestaServicio:
    def __init__(self, codigo, nombre_cliente, tipo_servicio,
                 correo, telefono, pregunta_1, pregunta_2,
                 pregunta_3, fecha_registro=None):
        self.codigo = codigo
        self.nombre_cliente = nombre_cliente
        self.tipo_servicio = tipo_servicio
        self.correo = correo
        self.telefono = telefono
        self.pregunta_1 = pregunta_1
        self.pregunta_2 = pregunta_2
        self.pregunta_3 = pregunta_3
        if fecha_registro is None:
            self.fecha_registro = datetime.now()
        else:
            self.fecha_registro = fecha_registro

    def __str__(self):
        return (f"Encuesta[{self.codigo}] - Cliente: {self.nombre_cliente}, "
                f"Servicio: {self.tipo_servicio}, Fecha: {self.fecha_registro.strftime('%Y-%m-%d')}")

    def to_dict(self):
        return {
            'codigo': self.codigo,
            'nombre_cliente': self.nombre_cliente,
            'tipo_servicio': self.tipo_servicio,
            'correo': self.correo,
            'telefono': self.telefono,
            'pregunta_1': self.pregunta_1,
            'pregunta_2': self.pregunta_2,
            'pregunta_3': self.pregunta_3,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d')
        }

    @staticmethod
    def from_dict(data):
        fecha = datetime.strptime(data['fecha_registro'], '%Y-%m-%d')
        return Encuesta(
            data['codigo'],
            data['nombre_cliente'],
            data['tipo_servicio'],
            data['correo'],
            data['telefono'],
            data['pregunta_1'],
            data['pregunta_2'],
            data['pregunta_3'],
            fecha
        )
