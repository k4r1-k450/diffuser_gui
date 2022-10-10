#!python3.8

import sys

from PyQt6.QtWidgets import QApplication

from module import Window

def main():
    app = QApplication([])
    window = Window.TopWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
