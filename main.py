from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow
import sys 
from main_window import MainWindow
app = QApplication(sys.argv)
window = MainWindow()
window.show() 
app.exec()
