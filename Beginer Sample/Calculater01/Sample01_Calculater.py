import sys
from Calculater01 import Calculater01
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Calculater01.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())