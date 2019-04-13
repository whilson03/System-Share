# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_established.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_serverEstablishedDialog(object):
    def setupUi(self, serverEstablishedDialog):
        serverEstablishedDialog.setObjectName("serverEstablishedDialog")
        serverEstablishedDialog.resize(378, 146)
        serverEstablishedDialog.setMinimumSize(QtCore.QSize(378, 146))
        serverEstablishedDialog.setMaximumSize(QtCore.QSize(378, 146))
        self.gridLayout = QtWidgets.QGridLayout(serverEstablishedDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.ip_address_entry = QtWidgets.QLabel(serverEstablishedDialog)
        self.ip_address_entry.setText("")
        self.ip_address_entry.setObjectName("ip_address_entry")
        self.gridLayout.addWidget(self.ip_address_entry, 1, 2, 1, 1, QtCore.Qt.AlignTop)
        self.const_ip_address_label = QtWidgets.QLabel(serverEstablishedDialog)
        self.const_ip_address_label.setObjectName("const_ip_address_label")
        self.gridLayout.addWidget(self.const_ip_address_label, 1, 1, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)
        self.checl_icon = QtWidgets.QLabel(serverEstablishedDialog)
        self.checl_icon.setAutoFillBackground(True)
        self.checl_icon.setText("")
        self.checl_icon.setPixmap(QtGui.QPixmap("icons/check_sign.png"))
        self.checl_icon.setObjectName("checl_icon")
        self.gridLayout.addWidget(self.checl_icon, 0, 0, 2, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.server_established_label = QtWidgets.QLabel(serverEstablishedDialog)
        self.server_established_label.setObjectName("server_established_label")
        self.gridLayout.addWidget(self.server_established_label, 0, 1, 1, 2,
                                  QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)

        self.retranslateUi(serverEstablishedDialog)
        QtCore.QMetaObject.connectSlotsByName(serverEstablishedDialog)

    def retranslateUi(self, serverEstablishedDialog):
        _translate = QtCore.QCoreApplication.translate
        serverEstablishedDialog.setWindowTitle(_translate("serverEstablishedDialog", "Server Established"))
        self.const_ip_address_label.setText(_translate("serverEstablishedDialog", "IP Address:"))
        self.server_established_label.setText(_translate("serverEstablishedDialog", "Server Established."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    serverEstablishedDialog = QtWidgets.QDialog()
    ui = Ui_serverEstablishedDialog()
    ui.setupUi(serverEstablishedDialog)
    serverEstablishedDialog.show()
    sys.exit(app.exec_())
