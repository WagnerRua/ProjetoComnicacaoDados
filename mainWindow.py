# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.sendPage = QtWidgets.QWidget()
        self.sendPage.setObjectName("sendPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sendPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.messageEditBox = QtWidgets.QLineEdit(self.sendPage)
        self.messageEditBox.setClearButtonEnabled(True)
        self.messageEditBox.setObjectName("messageEditBox")
        self.verticalLayout_2.addWidget(self.messageEditBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBoxNRZ = QtWidgets.QCheckBox(self.sendPage)
        self.checkBoxNRZ.setChecked(True)
        self.checkBoxNRZ.setAutoExclusive(True)
        self.checkBoxNRZ.setObjectName("checkBoxNRZ")
        self.horizontalLayout_2.addWidget(self.checkBoxNRZ)
        self.checkBoxNRZ_L = QtWidgets.QCheckBox(self.sendPage)
        self.checkBoxNRZ_L.setAutoExclusive(True)
        self.checkBoxNRZ_L.setObjectName("checkBoxNRZ_L")
        self.horizontalLayout_2.addWidget(self.checkBoxNRZ_L)
        self.checkBoxNRZ_I = QtWidgets.QCheckBox(self.sendPage)
        self.checkBoxNRZ_I.setAutoExclusive(True)
        self.checkBoxNRZ_I.setObjectName("checkBoxNRZ_I")
        self.horizontalLayout_2.addWidget(self.checkBoxNRZ_I)
        self.checkBoxRZ = QtWidgets.QCheckBox(self.sendPage)
        self.checkBoxRZ.setAutoExclusive(True)
        self.checkBoxRZ.setObjectName("checkBoxRZ")
        self.horizontalLayout_2.addWidget(self.checkBoxRZ)
        self.sendMessageButton = QtWidgets.QPushButton(self.sendPage)
        self.sendMessageButton.setObjectName("sendMessageButton")
        self.horizontalLayout_2.addWidget(self.sendMessageButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.line0 = QtWidgets.QFrame(self.sendPage)
        self.line0.setFrameShape(QtWidgets.QFrame.HLine)
        self.line0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line0.setObjectName("line0")
        self.verticalLayout_2.addWidget(self.line0)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.messageLabel0 = QtWidgets.QLabel(self.sendPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.messageLabel0.setFont(font)
        self.messageLabel0.setObjectName("messageLabel0")
        self.horizontalLayout_4.addWidget(self.messageLabel0)
        self.showMessageLabel0 = QtWidgets.QLabel(self.sendPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showMessageLabel0.sizePolicy().hasHeightForWidth())
        self.showMessageLabel0.setSizePolicy(sizePolicy)
        self.showMessageLabel0.setText("")
        self.showMessageLabel0.setWordWrap(True)
        self.showMessageLabel0.setObjectName("showMessageLabel0")
        self.horizontalLayout_4.addWidget(self.showMessageLabel0)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.line1 = QtWidgets.QFrame(self.sendPage)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.verticalLayout_2.addWidget(self.line1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.binaryLabel0 = QtWidgets.QLabel(self.sendPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binaryLabel0.sizePolicy().hasHeightForWidth())
        self.binaryLabel0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.binaryLabel0.setFont(font)
        self.binaryLabel0.setObjectName("binaryLabel0")
        self.horizontalLayout_3.addWidget(self.binaryLabel0)
        self.showBinaryLabel0 = QtWidgets.QLabel(self.sendPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showBinaryLabel0.sizePolicy().hasHeightForWidth())
        self.showBinaryLabel0.setSizePolicy(sizePolicy)
        self.showBinaryLabel0.setText("")
        self.showBinaryLabel0.setWordWrap(True)
        self.showBinaryLabel0.setObjectName("showBinaryLabel0")
        self.horizontalLayout_3.addWidget(self.showBinaryLabel0)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line2 = QtWidgets.QFrame(self.sendPage)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.verticalLayout_2.addWidget(self.line2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.encodedLabel0 = QtWidgets.QLabel(self.sendPage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.encodedLabel0.setFont(font)
        self.encodedLabel0.setObjectName("encodedLabel0")
        self.horizontalLayout.addWidget(self.encodedLabel0)
        self.showEncodedLabel0 = QtWidgets.QLabel(self.sendPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showEncodedLabel0.sizePolicy().hasHeightForWidth())
        self.showEncodedLabel0.setSizePolicy(sizePolicy)
        self.showEncodedLabel0.setText("")
        self.showEncodedLabel0.setWordWrap(True)
        self.showEncodedLabel0.setObjectName("showEncodedLabel0")
        self.horizontalLayout.addWidget(self.showEncodedLabel0)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line3 = QtWidgets.QFrame(self.sendPage)
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.verticalLayout_2.addWidget(self.line3)
        self.graphicsView = PlotWidget(self.sendPage)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.tabWidget.addTab(self.sendPage, "")
        self.receivePage = QtWidgets.QWidget()
        self.receivePage.setObjectName("receivePage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.receivePage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.line4 = QtWidgets.QFrame(self.receivePage)
        self.line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.verticalLayout_3.addWidget(self.line4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.messageLabel1 = QtWidgets.QLabel(self.receivePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageLabel1.sizePolicy().hasHeightForWidth())
        self.messageLabel1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.messageLabel1.setFont(font)
        self.messageLabel1.setObjectName("messageLabel1")
        self.horizontalLayout_7.addWidget(self.messageLabel1)
        self.showMessageLabel1 = QtWidgets.QLabel(self.receivePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showMessageLabel1.sizePolicy().hasHeightForWidth())
        self.showMessageLabel1.setSizePolicy(sizePolicy)
        self.showMessageLabel1.setText("")
        self.showMessageLabel1.setWordWrap(True)
        self.showMessageLabel1.setObjectName("showMessageLabel1")
        self.horizontalLayout_7.addWidget(self.showMessageLabel1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.line5 = QtWidgets.QFrame(self.receivePage)
        self.line5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line5.setObjectName("line5")
        self.verticalLayout_3.addWidget(self.line5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.binaryLabel1 = QtWidgets.QLabel(self.receivePage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.binaryLabel1.setFont(font)
        self.binaryLabel1.setObjectName("binaryLabel1")
        self.horizontalLayout_6.addWidget(self.binaryLabel1)
        self.showBinaryLabel1 = QtWidgets.QLabel(self.receivePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showBinaryLabel1.sizePolicy().hasHeightForWidth())
        self.showBinaryLabel1.setSizePolicy(sizePolicy)
        self.showBinaryLabel1.setText("")
        self.showBinaryLabel1.setObjectName("showBinaryLabel1")
        self.horizontalLayout_6.addWidget(self.showBinaryLabel1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.line6 = QtWidgets.QFrame(self.receivePage)
        self.line6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line6.setObjectName("line6")
        self.verticalLayout_3.addWidget(self.line6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.encodedLabel1 = QtWidgets.QLabel(self.receivePage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.encodedLabel1.setFont(font)
        self.encodedLabel1.setObjectName("encodedLabel1")
        self.horizontalLayout_5.addWidget(self.encodedLabel1)
        self.showEncoddLabel1 = QtWidgets.QLabel(self.receivePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showEncoddLabel1.sizePolicy().hasHeightForWidth())
        self.showEncoddLabel1.setSizePolicy(sizePolicy)
        self.showEncoddLabel1.setText("")
        self.showEncoddLabel1.setWordWrap(True)
        self.showEncoddLabel1.setObjectName("showEncoddLabel1")
        self.horizontalLayout_5.addWidget(self.showEncoddLabel1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line7 = QtWidgets.QFrame(self.receivePage)
        self.line7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line7.setObjectName("line7")
        self.verticalLayout_3.addWidget(self.line7)
        self.graphicsView1 = PlotWidget(self.receivePage)
        self.graphicsView1.setObjectName("graphicsView1")
        self.verticalLayout_3.addWidget(self.graphicsView1)
        self.tabWidget.addTab(self.receivePage, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comunicação de Dados"))
        self.checkBoxNRZ.setText(_translate("MainWindow", "NRZ Unipolar"))
        self.checkBoxNRZ_L.setText(_translate("MainWindow", "NRZ-L"))
        self.checkBoxNRZ_I.setText(_translate("MainWindow", "NRZ-I"))
        self.checkBoxRZ.setText(_translate("MainWindow", "RZ"))
        self.sendMessageButton.setText(_translate("MainWindow", "Send Message"))
        self.messageLabel0.setText(_translate("MainWindow", "Message:"))
        self.binaryLabel0.setText(_translate("MainWindow", "Binary:"))
        self.encodedLabel0.setText(_translate("MainWindow", "Encoded"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sendPage), _translate("MainWindow", "Send Message"))
        self.messageLabel1.setText(_translate("MainWindow", "Message:"))
        self.binaryLabel1.setText(_translate("MainWindow", "Binary:"))
        self.encodedLabel1.setText(_translate("MainWindow", "Encoded:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.receivePage), _translate("MainWindow", "Receive Message"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

