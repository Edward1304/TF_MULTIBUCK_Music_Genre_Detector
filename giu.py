import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Gui_Multi_Buck(QWidget):

    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle('MultiBUCK')
        self.setGeometry(100, 100, 800, 600)

        # Creación de los widgets
        self.logo_label = QLabel()
        self.logo_pixmap = QPixmap('logo1.png')
        self.logo_pixmap = self.logo_pixmap.scaled(self.logo_pixmap.width() // 1, self.logo_pixmap.height() // 1)  # Redimensionar la imagen
        self.logo_label.setPixmap(self.logo_pixmap)
        self.search_label = QLabel('Ingrese El link de la Cancion:')
        self.search_entry = QLineEdit()
        self.search_button = QPushButton('Escuchar')
        self.results_label = QLabel('Resultado de Genero de la Cancion:')
        self.results_list = QListWidget()
        self.results_list.setMaximumHeight(50) # Modificar tamaño para que quepa una palabra

        self.spectrum_label = QLabel('Espectro de Audio:')
        self.spectrum_list = QListWidget()

        self.play_button = QPushButton('Reproducir')

        self.setStyleSheet('background-color: ##FFFFFF  ; color: #4D5156; font-size: 16px; font-family: Arial, sans-serif;')
        self.search_label.setStyleSheet('color: #4285F4; font-size: 20px; font-weight: bold;')
        self.search_entry.setStyleSheet('border: 2px solid #4285F4; padding: 10px;')
        self.search_button.setStyleSheet('background-color: #FF2D00 ; color: white; padding: 10px; border-radius: 5px;')
        self.results_label.setStyleSheet('color: #4285F4; font-size: 20px; font-weight: bold;')
        self.results_list.setStyleSheet('border: 2px solid #4285F4; padding: 10px;')
        self.spectrum_label.setStyleSheet('color: #4285F4; font-size: 20px; font-weight: bold;')
        self.spectrum_list.setStyleSheet('border: 2px solid #4285F4; padding: 10px;')

        grid = QGridLayout()
        grid.addWidget(self.logo_label, 0, 0, 2, 2)
        grid.addWidget(self.search_label, 2, 0)
        grid.addWidget(self.search_entry, 3, 0)
        grid.addWidget(self.search_button, 3, 1)
        grid.addWidget(self.results_label, 4, 0)
        grid.addWidget(self.results_list, 5, 0)
        grid.addWidget(self.spectrum_label, 6, 0)
        grid.addWidget(self.spectrum_list, 7, 0)
        grid.addWidget(self.play_button, 8, 0)
        self.setLayout(grid)

        # Conexión de señales y slots
        self.search_button.clicked.connect(self.search)

    def search(self):
        # Obtener el enlace de la canción desde la entrada de texto
        link = self.search_entry.text()
         # Hacer algo con el texto, como imprimirlo en la consola
        print("Texto ingresado en 'search_entry':",link)




    
      

   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui_Multi_Buck()
    window.show()
    sys.exit(app.exec_())
