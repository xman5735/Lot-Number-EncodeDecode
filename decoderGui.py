# Form implementation generated from reading ui file 'ascii-decoder-test.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(367, 451)
        mainWindow.setWindowOpacity(6.0)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LotNumberEntry = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LotNumberEntry.setGeometry(QtCore.QRect(10, 40, 281, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setUnderline(True)
        self.LotNumberEntry.setFont(font)
        self.LotNumberEntry.setObjectName("LotNumberEntry")
        self.color = QtWidgets.QLabel(self.centralwidget)
        self.color.setGeometry(QtCore.QRect(0, 160, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.color.setFont(font)
        self.color.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.color.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.color.setObjectName("color")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(0, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.date.setObjectName("date")
        self.dimensions = QtWidgets.QLabel(self.centralwidget)
        self.dimensions.setGeometry(QtCore.QRect(0, 260, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dimensions.setFont(font)
        self.dimensions.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dimensions.setObjectName("dimensions")
        self.palletnumber = QtWidgets.QLabel(self.centralwidget)
        self.palletnumber.setGeometry(QtCore.QRect(0, 310, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.palletnumber.setFont(font)
        self.palletnumber.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.palletnumber.setObjectName("palletnumber")
        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        self.decodeButton.setGeometry(QtCore.QRect(220, 120, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.decodeButton.setFont(font)
        self.decodeButton.setObjectName("decodeButton")
        self.linenumber = QtWidgets.QLabel(self.centralwidget)
        self.linenumber.setGeometry(QtCore.QRect(0, 360, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.linenumber.setFont(font)
        self.linenumber.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.linenumber.setObjectName("linenumber")
        self.colorOut = QtWidgets.QLabel(self.centralwidget)
        self.colorOut.setGeometry(QtCore.QRect(180, 160, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.colorOut.setFont(font)
        self.colorOut.setScaledContents(True)
        self.colorOut.setObjectName("colorOut")
        self.DateOut = QtWidgets.QLabel(self.centralwidget)
        self.DateOut.setGeometry(QtCore.QRect(180, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DateOut.setFont(font)
        self.DateOut.setScaledContents(True)
        self.DateOut.setObjectName("DateOut")
        self.DimsOut = QtWidgets.QLabel(self.centralwidget)
        self.DimsOut.setGeometry(QtCore.QRect(180, 260, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DimsOut.setFont(font)
        self.DimsOut.setScaledContents(True)
        self.DimsOut.setObjectName("DimsOut")
        self.palletOut = QtWidgets.QLabel(self.centralwidget)
        self.palletOut.setGeometry(QtCore.QRect(180, 310, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.palletOut.setFont(font)
        self.palletOut.setScaledContents(True)
        self.palletOut.setObjectName("palletOut")
        self.lineNumber = QtWidgets.QLabel(self.centralwidget)
        self.lineNumber.setGeometry(QtCore.QRect(180, 360, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineNumber.setFont(font)
        self.lineNumber.setScaledContents(True)
        self.lineNumber.setObjectName("lineNumber")
        self.enterlotnumber = QtWidgets.QLabel(self.centralwidget)
        self.enterlotnumber.setGeometry(QtCore.QRect(10, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.enterlotnumber.setFont(font)
        self.enterlotnumber.setObjectName("enterlotnumber")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)


        #own additions
        self.LotNumberEntry.textChanged.connect(self.lotInput)
        self.decodeButton.clicked.connect(self.clicked_btn)


        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Lot Number Decoder GUI"))
        self.color.setText(_translate("mainWindow", "Color:"))
        self.date.setText(_translate("mainWindow", "Date Produced:"))
        self.dimensions.setText(_translate("mainWindow", "Dimensions:"))
        self.palletnumber.setText(_translate("mainWindow", "Pallet Number:"))
        self.decodeButton.setText(_translate("mainWindow", "Decode"))
        self.linenumber.setText(_translate("mainWindow", "Line Number:"))
        self.colorOut.setText(_translate("mainWindow", "ColorOut"))
        self.DateOut.setText(_translate("mainWindow", "DateOut"))
        self.DimsOut.setText(_translate("mainWindow", "DimensionsOut"))
        self.palletOut.setText(_translate("mainWindow", "PalletOut"))
        self.lineNumber.setText(_translate("mainWindow", "LineOut"))
        self.enterlotnumber.setText(_translate("mainWindow", "Enter Lot Number:"))

    def clicked_btn(self):
        self.decodeButton.setStyleSheet('color:purple')

    def lotInput(self):
        inputLot = 

    #for alter
        #self.nameLabel = QLabel(self)
        #self.nameLabel.setText('Name:')
        #self.line = QLineEdit(self)