# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connection_failed_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_connectionFailedDialog(object):
    def setupUi(self, connectionFailedDialog):
        connectionFailedDialog.setObjectName("connectionFailedDialog")
        connectionFailedDialog.resize(236, 101)
        self.gridLayout = QtWidgets.QGridLayout(connectionFailedDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(connectionFailedDialog)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(connectionFailedDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)

        self.retranslateUi(connectionFailedDialog)
        QtCore.QMetaObject.connectSlotsByName(connectionFailedDialog)

    def retranslateUi(self, connectionFailedDialog):
        _translate = QtCore.QCoreApplication.translate
        connectionFailedDialog.setWindowTitle(_translate("connectionFailedDialog", "Connection Failed"))
        self.pushButton.setText(_translate("connectionFailedDialog", "Try Again"))
        self.label_2.setText(_translate("connectionFailedDialog", "Connection Failed"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    connectionFailedDialog = QtWidgets.QDialog()
    ui = Ui_connectionFailedDialog()
    ui.setupUi(connectionFailedDialog)
    connectionFailedDialog.show()
    sys.exit(app.exec_())
