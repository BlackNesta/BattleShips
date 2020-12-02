import PyQt5.QtWidgets as qtw

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Battleships")
        self.setLayout(qtw.QHBoxLayout())
        self.keypad()

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        btns = [[qtw.QPushButton() for i in range(9)] for j in range(9)]
        for i in range (9):
            for j in range (9):
                container.layout().addWidget(btns[i][j], i, j)
        self.layout().addWidget(container)


if __name__ == "__main__":
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()
