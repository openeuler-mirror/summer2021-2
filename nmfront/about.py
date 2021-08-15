import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QSize


NAME = "nm"
VERSION = 1.0
DESCRIPTION = ""
PNG_PATH=os.path.dirname(os.path.realpath(__file__))
ICON = "nm.png"


class nmSettingsAbout(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(100, 100)
        nm_logo = QLabel(self)
        nm_logo_pix = QPixmap(f"{PNG_PATH}/{ICON}")
        nm_logo.setScaledContents(True)
        nm_logo.setMaximumSize(QSize(200, 200))
        nm_logo.setPixmap(nm_logo_pix)
        nm_logo.setAlignment(Qt.AlignHCenter)
        nm_name = QLabel(f"<h1>Name: {NAME}</h1>")
        nm_name.setAlignment(Qt.AlignHCenter)
        nm_version = QLabel(f"Version: {VERSION}")
        nm_version.setAlignment(Qt.AlignHCenter)
        nm_description = QLabel(f"{DESCRIPTION}")
        nm_description.setAlignment(Qt.AlignHCenter)
        vbox = QVBoxLayout()
        vbox.addWidget(nm_logo)
        vbox.addWidget(nm_name)
        vbox.addWidget(nm_version)
        vbox.addWidget(nm_description)
        vbox.setSpacing(14)
        self.setLayout(vbox)
        self.setWindowTitle('About')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = nmSettingsAbout()
    ex.show()
    sys.exit(app.exec_())
