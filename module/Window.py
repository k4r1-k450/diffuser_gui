#!python3.8

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class TopWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diffuser GUI")
        self.resize(1280, 720)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # それぞれのモードの画面を開くためのボタンを仕込むレイアウト
        contents_layout = QHBoxLayout()

        # img2img
        i2i_btn = QPushButton("img2img")
        i2i_btn.setFixedHeight(self.height()/2)
        contents_layout.addWidget(i2i_btn)

        # text2img
        t2i_btn = QPushButton("text2img")
        t2i_btn.setFixedHeight(self.height()/2)
        contents_layout.addWidget(t2i_btn)
        
        layout.addLayout(contents_layout)
