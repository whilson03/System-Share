from PyQt5 import QtWidgets

from client import client_operation
from gui.connection_failed_dialog import Ui_connectionFailedDialog
from gui.create_server_dialog import Ui_createDialog
from gui.join_server_dialog import Ui_joinDialog
from gui.main_window import Ui_MainWindow
from gui.server_established import Ui_serverEstablishedDialog
from gui.server_unsuccessful import Ui_serverUnsuccessfulDialog


def openJoinDialog():
    Ui_MainWindow.join_dialog = QtWidgets.QDialog()
    Ui_MainWindow.ui = Ui_joinDialog()
    Ui_MainWindow.ui.setupUi(Ui_MainWindow.join_dialog)
    Ui_MainWindow.join_dialog.show()


def openCreateDialog():
    Ui_MainWindow.create_dialog = QtWidgets.QDialog()
    Ui_MainWindow.ui = Ui_createDialog()
    Ui_MainWindow.ui.setupUi(Ui_MainWindow.create_dialog)
    Ui_MainWindow.create_dialog.show()


def openServerEstablishedDialog():
    Ui_MainWindow.server_established_dialog = QtWidgets.QDialog()
    Ui_MainWindow.ui = Ui_serverEstablishedDialog()
    Ui_MainWindow.ui.setupUi(Ui_MainWindow.server_established_dialog)
    Ui_MainWindow.server_established_dialog.show()


def openServerUnsuccessfuldDialog():
    Ui_MainWindow.server_unsuccessful_dialog = QtWidgets.QDialog()
    Ui_MainWindow.ui = Ui_serverUnsuccessfulDialog()
    Ui_MainWindow.ui.setupUi(Ui_MainWindow.server_unsuccessful_dialog)
    Ui_MainWindow.server_unsuccessful_dialog.show()


def openConnectionFailedDialog():
    Ui_MainWindow.connection_failed_dialog = QtWidgets.QDialog()
    Ui_MainWindow.ui = Ui_connectionFailedDialog()
    Ui_MainWindow.ui.setupUi(Ui_MainWindow.connection_failed_dialog)
    Ui_MainWindow.connection_failed_dialog.show()


def updateClientInterface(link):
    Ui_MainWindow.textEdit.setText(link)

    tree_list = []
    buffer = client_operation.list_client_dir(link)
    for item in buffer:
        tree_list.append(QtWidgets.QTreeWidgetItem(item))
    Ui_MainWindow.treeWidget.addTopLevelItems(tree_list)


def openParentDirectory():
    client_operation.open_parent_directory()
    Ui_MainWindow.treeWidget.clear()
    Ui_MainWindow.updateClientInterface(client_operation.get_current_directory())


def openSelectedDirectory():
    get_selected = Ui_MainWindow.treeWidget.selectedItems()
    if get_selected:
        base_node = get_selected[0]
        get_child_node = base_node.text(0)
        client_operation.open_directory(get_child_node)
        Ui_MainWindow.treeWidget.clear()
        Ui_MainWindow.updateClientInterface(client_operation.get_current_directory())


client_operation.set_home_directory()
updateClientInterface(client_operation.get_current_directory())
Ui_MainWindow.actionJoin.triggered.connect(Ui_MainWindow.openJoinDialog)
Ui_MainWindow.actionHost.triggered.connect(Ui_MainWindow.openCreateDialog)
Ui_MainWindow.client_parent_button.clicked.connect(Ui_MainWindow.openParentDirectory)
Ui_MainWindow.treeWidget.itemSelectionChanged.connect(Ui_MainWindow.openSelectedDirectory)
