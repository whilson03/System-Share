# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'join_server_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_joinDialog(object):
    def setupUi(self, joinDialog):
        joinDialog.setObjectName("joinDialog")
        joinDialog.resize(400, 164)
        joinDialog.setMinimumSize(QtCore.QSize(400, 164))
        joinDialog.setMaximumSize(QtCore.QSize(400, 164))
        self.gridLayout = QtWidgets.QGridLayout(joinDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.password_label = QtWidgets.QLabel(joinDialog)
        self.password_label.setObjectName("password_label")
        self.gridLayout.addWidget(self.password_label, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.password_entry = QtWidgets.QTextEdit(joinDialog)
        self.password_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.password_entry.setObjectName("password_entry")
        self.gridLayout.addWidget(self.password_entry, 3, 1, 1, 1)
        self.username_entry = QtWidgets.QTextEdit(joinDialog)
        self.username_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.username_entry.setObjectName("username_entry")
        self.gridLayout.addWidget(self.username_entry, 3, 0, 1, 1)
        self.join_button = QtWidgets.QPushButton(joinDialog)
        self.join_button.setObjectName("join_button")
        self.gridLayout.addWidget(self.join_button, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.username_label = QtWidgets.QLabel(joinDialog)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.hostname_label = QtWidgets.QLabel(joinDialog)
        self.hostname_label.setObjectName("hostname_label")
        self.gridLayout.addWidget(self.hostname_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.hostname_entry = QtWidgets.QTextEdit(joinDialog)
        self.hostname_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.hostname_entry.setObjectName("hostname_entry")
        self.gridLayout.addWidget(self.hostname_entry, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)

        self.retranslateUi(joinDialog)
        QtCore.QMetaObject.connectSlotsByName(joinDialog)

    def retranslateUi(self, joinDialog):
        _translate = QtCore.QCoreApplication.translate
        joinDialog.setWindowTitle(_translate("joinDialog", "Join Server"))
        self.password_label.setText(_translate("joinDialog", "Password"))
        self.join_button.setText(_translate("joinDialog", "Join"))
        self.username_label.setText(_translate("joinDialog", "Username"))
        self.hostname_label.setText(_translate("joinDialog", "Host name"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    joinDialog = QtWidgets.QDialog()
    ui = Ui_joinDialog()
    ui.setupUi(joinDialog)
    joinDialog.show()
    sys.exit(app.exec_())
