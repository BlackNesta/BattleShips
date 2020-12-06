import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battleships")
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.placeShips()


        self.show()

    def keypad(self):

        container0 = qtw.QWidget()
        container0.setLayout(qtw.QGridLayout())
        labels = [qtw.QLabel("Player " + str(i + 1)) for i in range(2)]
        container0.layout().addWidget(labels[0], 0, 4)
        labels[0].setStyleSheet("background-color : white")
        labels[0].setAlignment(QtCore.Qt.AlignCenter)
        labels[1].setAlignment(QtCore.Qt.AlignCenter)
        labels[1].setStyleSheet("background-color : gray")
        container0.layout().addWidget(labels[1], 0, 12)
        self.layout().addWidget(container0)

        container1 = qtw.QWidget()
        container1.setLayout(qtw.QGridLayout())
        btns_player1 = [[qtw.QPushButton() for i in range(8)] for j in range(8)]
        btns_player2 = [[qtw.QPushButton() for i in range(8)] for j in range(8)]
        for i in range (8):
            for j in range (8):
                btns_player1[i][j].setStyleSheet("background-color : white")
                container1.layout().addWidget(btns_player1[i][j], i + 1, j)
                btns_player2[i][j].setStyleSheet("background-color : gray")
                container1.layout().addWidget(btns_player2[i][j], i + 1, j + 9)
                
        self.layout().addWidget(container1)
    
    def placeShips(self):
        return 0


if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
