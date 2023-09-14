# Made by Niklas

from Handler import ConnectionHandler, NotificationHandler
from UI import Connection, Main
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)
from PyQt5.QtCore import pyqtSignal, QObject
import sys
import threading

class Worker(QObject):
    finished = pyqtSignal(bool)

    def checkConnection(self, ServerHandler, UI_M):
        res = ServerHandler.checkConneection(UI_M)
        self.finished.emit(res)

if __name__ == "__main__":
    print("Intializing Server Verwaltung...")
    app = QApplication(sys.argv)
    UI_1 = QMainWindow()
    UI_2 = QMainWindow()
    UI_M = Connection.Ui_MainWindow()
    UI_M2 = Main.Ui_MainWindow()
    UI_M.setupUi(UI_1)
    UI_M2.setupUi(UI_2)
    UI_1.show()

    print("Connecting to Server..")
    ServerHandler = ConnectionHandler.ServerAPI()
    Worker1 = Worker()
    threading.Thread(target=Worker1.checkConnection, args=(ServerHandler, UI_M, )).start()

    def doneCheckConnection(res):
        if res == False:
            UI_M.label.setText("Verbindung konnte nicht aufgebaut werden")
            threading.Thread(target=NotificationHandler.balloon_tip, args=("Server Verwaltung", "Verbindung konnte nicht hergestellt werden.")).start()
        else:
            UI_M.label.setText("Verbindung wurde hergestellt")
            threading.Thread(target=NotificationHandler.balloon_tip, args=("Server Verwaltung", "Verbindung konnte hergestellt werden.")).start()
            UI_1.close()
            UI_2.show()

    Worker1.finished.connect(doneCheckConnection)

    sys.exit(app.exec_())

    