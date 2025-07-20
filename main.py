import sys
from PySide6.QtWidgets import QApplication

from src.servicio.encuestas import EncuestaServicio

if __name__== "__main__":
    app = QApplication(sys.argv)
    vtnEncuestas = EncuestaServicio()
    vtnEncuestas.show()
    sys.exit(app.exec())
