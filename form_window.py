from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit, QFileDialog, QListView, QLabel, QLineEdit, QDialog
from database import Database

class FormWindow(QDialog):
    def __init__(self, parent= None, object = None):
        super().__init__(parent)
        if object is None:
            self.setWindowTitle("Добавление")
            self.button = QPushButton("Добавить")
            self.button.clicked.connect(self.close)
        else:
            self.setWindowTitle("Изменение")
            self.button = QPushButton("Изменить")
            self.button.clicked.connect(self.close)
            self.id = object.split(":")[0]
        label = QLabel("Название")
        if object is None:
            self.name_text = QLineEdit()
        else:
            self.name_text = QLineEdit(object.split(":")[1])
        name_input = QHBoxLayout()
        name_input.addWidget(label)
        name_input.addWidget(self.name_text)
        name_input_widget = QWidget()
        name_input_widget.setLayout(name_input)
        layout = QVBoxLayout()
        layout.addWidget(name_input_widget)
        layout.addWidget(self.button)

        self.setLayout(layout)
    def close(self):
        self.done(1) 
