# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_unsuccessful.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_serverUnsuccessfulDialog(object):
    def setupUi(self, serverUnsuccessfulDialog):
        serverUnsuccessfulDialog.setObjectName("serverUnsuccessfulDialog")
        serverUnsuccessfulDialog.resize(431, 138)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(serverUnsuccessfulDialog.sizePolicy().hasHeightForWidth())
        serverUnsuccessfulDialog.setSizePolicy(sizePolicy)
        serverUnsuccessfulDialog.setMinimumSize(QtCore.QSize(431, 138))
        serverUnsuccessfulDialog.setMaximumSize(QtCore.QSize(431, 146))
        self.gridLayout = QtWidgets.QGridLayout(serverUnsuccessfulDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.lower_failure_message = QtWidgets.QLabel(serverUnsuccessfulDialog)
        self.lower_failure_message.setObjectName("lower_failure_message")
        self.gridLayout.addWidget(self.lower_failure_message, 1, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.upper_failure_message = QtWidgets.QLabel(serverUnsuccessfulDialog)
        self.upper_failure_message.setObjectName("upper_failure_message")
        self.gridLayout.addWidget(self.upper_failure_message, 0, 1, 1, 1, QtCore.Qt.AlignBottom)
        self.failure_icon = QtWidgets.QLabel(serverUnsuccessfulDialog)
        self.failure_icon.setText("")
        self.failure_icon.setPixmap(QtGui.QPixmap("icons/sad_face.png"))
        self.failure_icon.setObjectName("failure_icon")
        self.gridLayout.addWidget(self.failure_icon, 0, 0, 2, 1)

        self.retranslateUi(serverUnsuccessfulDialog)
        QtCore.QMetaObject.connectSlotsByName(serverUnsuccessfulDialog)

    def retranslateUi(self, serverUnsuccessfulDialog):
        _translate = QtCore.QCoreApplication.translate
        serverUnsuccessfulDialog.setWindowTitle(_translate("serverUnsuccessfulDialog", "Server Unsuccessful"))
        self.lower_failure_message.setText(
            _translate("serverUnsuccessfulDialog", "This PC does not support this feature."))
        self.upper_failure_message.setText(_translate("serverUnsuccessfulDialog", "Server Cannot be Established."))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    serverUnsuccessfulDialog = QtWidgets.QDialog()
    ui = Ui_serverUnsuccessfulDialog()
    ui.setupUi(serverUnsuccessfulDialog)
    serverUnsuccessfulDialog.show()
    sys.exit(app.exec_())
