# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_server_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createDialog(object):
    def setupUi(self, createDialog):
        createDialog.setObjectName("createDialog")
        createDialog.resize(400, 164)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(createDialog.sizePolicy().hasHeightForWidth())
        createDialog.setSizePolicy(sizePolicy)
        createDialog.setMinimumSize(QtCore.QSize(400, 164))
        createDialog.setMaximumSize(QtCore.QSize(400, 164))
        self.gridLayout_2 = QtWidgets.QGridLayout(createDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.directory_label = QtWidgets.QLabel(createDialog)
        self.directory_label.setObjectName("directory_label")
        self.gridLayout_2.addWidget(self.directory_label, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.password_label = QtWidgets.QLabel(createDialog)
        self.password_label.setObjectName("password_label")
        self.gridLayout_2.addWidget(self.password_label, 0, 1, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.password_entry = QtWidgets.QTextEdit(createDialog)
        self.password_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.password_entry.setObjectName("password_entry")
        self.gridLayout_2.addWidget(self.password_entry, 1, 1, 1, 1)
        self.username_label = QtWidgets.QLabel(createDialog)
        self.username_label.setObjectName("username_label")
        self.gridLayout_2.addWidget(self.username_label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.create_button = QtWidgets.QPushButton(createDialog)
        self.create_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.create_button.setObjectName("create_button")
        self.gridLayout_2.addWidget(self.create_button, 4, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.username_entry = QtWidgets.QTextEdit(createDialog)
        self.username_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.username_entry.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.username_entry.setObjectName("username_entry")
        self.gridLayout_2.addWidget(self.username_entry, 1, 0, 1, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.directory_entry = QtWidgets.QTextEdit(createDialog)
        self.directory_entry.setMaximumSize(QtCore.QSize(16777215, 25))
        self.directory_entry.setObjectName("directory_entry")
        self.gridLayout_2.addWidget(self.directory_entry, 3, 0, 1, 2)

        self.retranslateUi(createDialog)
        QtCore.QMetaObject.connectSlotsByName(createDialog)

    def retranslateUi(self, createDialog):
        _translate = QtCore.QCoreApplication.translate
        createDialog.setWindowTitle(_translate("createDialog", "Create Server"))
        self.directory_label.setText(_translate("createDialog", "Directory"))
        self.password_label.setText(_translate("createDialog", "Password"))
        self.username_label.setText(_translate("createDialog", "Username"))
        self.create_button.setText(_translate("createDialog", "Create"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    createDialog = QtWidgets.QDialog()
    ui = Ui_createDialog()
    ui.setupUi(createDialog)
    createDialog.show()
    sys.exit(app.exec_())
