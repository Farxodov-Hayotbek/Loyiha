from PyQt5.QtWidgets import QWidget

import ss
class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,600)
        self.setWindowTitle("Login")

