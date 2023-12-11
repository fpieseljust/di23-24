from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

class FinestraPrincipal(QMainWindow):
    '''
    Classe FinestraPrincipal, hereta de QMainWindow.
    El QMainWindow és un component pensat per ser
    la finestra principal d'una aplicació.
    '''

    def __init__(self):
        super().__init__()
        self.setWindowTitle("finestra")
        self.boton1 = QPushButton("Fes clic!", self)
        # Configurem el botó com a element principal de la finestra.
        # Això és perquè estem usant un QMainWindow. No calia
        # passar-li el parent en la seua creació.
        self.setCentralWidget(self.boton1)
        # Connectem l'esdeveniment clic del botó a la ranura clic_de_boton
        self.boton1.clicked.connect(self.clic)

    # Definim la ranura que s'executarà amb el clic del botó
    def clic(self):
        print("Senyal de clic rebut -> Execució de la ranura")

if __name__ == "__main__":
    app = QApplication([])
    finestra1 = FinestraPrincipal()
    finestra1.show()
    app.exec()