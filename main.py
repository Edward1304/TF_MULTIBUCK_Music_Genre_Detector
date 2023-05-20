import sys
import typing
from PyQt5.QtWidgets import QApplication
from giu import *
from readDownload import *
from training import *
from signalSpectrum import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Gui_Multi_Buck()

    def download_song():
        # Obtener el enlace de la canción desde la entrada de texto
        link = window.search_entry.text()

        # Descargar la canción
        downloader = SongDowloader(link)
        downloader.download_and_convert_all()
        print("Canción descargada")
        
        # Detectar el género de la canción
        detector = SongGenreDetector(Xw_magnitude_song, Xw_list)
        min_distance_index, genre = detector.detect_genre()
        print("El género de la canción es:", genre)
        print(min_distance_index)
        
        # Mostrar el género detectado en la interfaz
        show_results(genre)
    
    def show_results(genre):
        # Limpiar la lista de resultados
        window.results_list.clear()

        # Agregar el género detectado a la lista de resultados
        item = QListWidgetItem(genre)
        window.results_list.addItem(item)

    window.search_button.clicked.connect(download_song)


    

    window.show()
    sys.exit(app.exec_())









