import os

from PyQt5 import QtCore, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QApplication, QStyle
from pyqt5_plugins.examplebutton import QtWidgets
import icon_rc
from button import Switch

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        ui_path = 'demo.ui'
        uic.loadUi(ui_path, self)


        self.MainWindow = self.window()
        self.MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.setAttribute(Qt.WA_TranslucentBackground, True)
        # Setting modal to center of the window
        self.MainWindow.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.MainWindow.size(),
                QApplication.instance().desktop().availableGeometry()
            )
        )

        self.closeButton = self.findChild(QtWidgets.QPushButton, 'closeButton')
        self.closeButton.clicked.connect(lambda:self.close())
        self.shadow = QGraphicsDropShadowEffect(blurRadius=3, xOffset=0, yOffset=1)
        self.closeButton.setGraphicsEffect(self.shadow)
        self.Modal = self.findChild(QtWidgets.QFrame, 'Modal')
        self.shadow_main = QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0)
        self.Modal.setGraphicsEffect(self.shadow_main)
        self.frame_27 = self.findChild(QtWidgets.QFrame, 'frame_27')
        self.frame_28 = self.findChild(QtWidgets.QFrame, 'frame_28')
        self.frame_62 = self.findChild(QtWidgets.QFrame, 'frame_62')
        self.frame_60 = self.findChild(QtWidgets.QFrame, 'frame_60')
        self.frame_43 = self.findChild(QtWidgets.QFrame, 'frame_43')
        self.frame_58 = self.findChild(QtWidgets.QFrame, 'frame_58')
        self.frame_65 = self.findChild(QtWidgets.QFrame, 'frame_65')
        self.frame_67 = self.findChild(QtWidgets.QFrame, 'frame_67')
        self.frame_63 = self.findChild(QtWidgets.QFrame, 'frame_63')
        Switch(self.frame_27)
        Switch(self.frame_28)
        Switch(self.frame_41)
        Switch(self.frame_62)
        Switch(self.frame_60)
        Switch(self.frame_43)
        Switch(self.frame_58)
        Switch(self.frame_65)
        Switch(self.frame_67)
        Switch(self.frame_63)

        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    qss = "static/qss/demo.qss"
    with open(qss, "r") as fh:
        app.setStyleSheet(fh.read())
    window = Ui()
    app.exec_()
