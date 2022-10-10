#!python3.8

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class TopWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diffuser GUI")

        layout = QVBoxLayout()
        self.setLayout(layout)
