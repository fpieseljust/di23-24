import sys, os
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
import resources

directori_arrel = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'ieseljust.editor.pyside6.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass

if __name__ == '__main__':
    loader = QUiLoader()
    app = QtWidgets.QApplication(sys.argv)
    ui_path = os.path.join(os.path.dirname(__file__), "ui/bloc_notes.ui")
    window = loader.load(ui_path, None)
    app.setWindowIcon(QIcon(os.path.join(directori_arrel,'img/editor.ico')))
    window.show()
    app.exec()
