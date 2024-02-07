# Testing sobre interfícies Qt amb pytest-qt
`pytest-qt` és un plugin de pytest que ens permet escriure proves sobre aplicacions PySide6, PySide2, PyQt5 i PyQt6.

Fixa't en el següent exemple:

!!! example "Exemple"
    ```python
    #!/usr/bin/env python
    # coding: utf-8
    """Hello app"""

    import sys
    from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QFormLayout

    class HelloWidget(QWidget):
        """HelloWidget example"""

        def __init__(self):
            """Constructor"""
            # Window
            super(HelloWidget, self).__init__()
            self.resize(200, 150)
            self.setWindowTitle("PySide6 Demo")

            # QLabel
            self.greet_label = QLabel(self)
            self.greet_label.setText("Hello World!")

            # QPushButton
            self.button_greet = QPushButton("Go")
            self.button_greet.clicked.connect(self.greet)

            # create layout
            form_layout = QFormLayout()
            form_layout.addRow(self.tr("Label"), self.greet_label)
            form_layout.addRow(self.tr("Say hi: "), self.button_greet)
            self.setLayout(form_layout)

        def greet(self):
            """Say hello"""
            self.greet_label.setText("Hello!")


    if __name__ == "__main__":
        app = QApplication([])
        window = HelloWidget()
        window.show()
        sys.exit(app.exec())
    ```

    ```python
    """Test the hello app"""

    from pytestqt.qt_compat import qt_api

    from hello import HelloWidget

    def test_hello(qtbot):
        """test clicking changes a label"""
        widget = HelloWidget()
        qtbot.addWidget(widget)

        # click in the Greet button and make sure it updates the appropriate label
        widget.button_greet.click()

        assert widget.greet_label.text() == "Hello!"
    ```

Pots obtindre [els fonts del següent enllaç](../../code/pytest-qt/hello.py).

Per a més informació visita la web de [documentació de pytest-qt](https://pytest-qt.readthedocs.io/en/latest/intro.html).

Donat el següent dialeg, desenvolupa un test per a comprovar que s'inserta un usuari i la seua contrasenya a una base de dades temporal que s'eliminarà en acabar la prova.

```python
import sys
import bcrypt

from PySide6.QtWidgets import QApplication, QDialog, QFormLayout, QLineEdit, QPushButton, QLabel, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlQuery

class CreateUserDialog(QDialog):
    def __init__(self, database_path):
        super().__init__()
        self.user = QLineEdit(self)
        self.user.setPlaceholderText("usuari")
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("contrasenya")
        self.btn_create = QPushButton('Create user', self)
        self.layout = QFormLayout(self)
        self.layout.addRow(QLabel("Usuari:"), self.user)
        self.layout.addRow(QLabel("Contrasenya:"), self.password)
        self.layout.addRow(self.btn_create)
        self.btn_create.clicked.connect(self.createUser)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(database_path)

    def createUser(self):
        if self.db.open():
            if (self.user.text() != '' and self.password.text() != ''):
                query = QSqlQuery()
                query.prepare("INSERT INTO users (user, password) VALUES (?, ?)")
                query.addBindValue(self.user.text())
                hashed_password = bcrypt.hashpw(self.password.text().encode('utf-8'), bcrypt.gensalt())
                query.addBindValue(hashed_password.decode('utf-8'))
                query.exec()
        self.close()

    def create_database(self):
        if self.db.open():
            query = QSqlQuery()
            query.exec_('CREATE TABLE IF NOT EXISTS users (user TEXT, password BLOB)')
            # Insert some users
            users = [("user1", "password1"), ("user2", "password2")]
            for user, password in users:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                query.prepare("INSERT INTO users (user, password) VALUES (?, ?)")
                query.addBindValue(user)
                query.addBindValue(hashed_password.decode('utf-8'))
                query.exec_()

def main():    
    app = QApplication(sys.argv)
    login = CreateUserDialog('users.db')
    login.create_database()
    login.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()

```