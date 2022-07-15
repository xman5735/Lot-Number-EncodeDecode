import sys

from PyQt6 import QtWidgets, uic

from decoderGui import Ui_mainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

    #button
    def decodeClicked(self):
        print('clicked')

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
