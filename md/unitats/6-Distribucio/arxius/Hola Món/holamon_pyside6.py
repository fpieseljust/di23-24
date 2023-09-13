import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, 
    QWidget, QVBoxLayout, QLabel, QPushButton)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setFixedSize(400, 200)
        self.setWindowTitle("Hola món! amb PySide6")

        layout = QVBoxLayout()
        label = QLabel("Hola món!")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        button = QPushButton("Tancar")
        button.pressed.connect(self.close)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
