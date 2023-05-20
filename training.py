import numpy as np
from signalSpectrum  import  *


    

import numpy as np

class SongGenreDetector:
    def __init__(self, Xw_magnitude_song, Xw_list):
        self.Xw_magnitude_song = Xw_magnitude_song
        self.Xw_list = Xw_list

    def detect_genre(self):
        distances = [np.linalg.norm(self.Xw_magnitude_song - Xw) for Xw in self.Xw_list]
        min_distance_index = np.argmin(distances)

        if 0 <= min_distance_index < 30:
            return min_distance_index, "Rock"
        elif 30 <= min_distance_index < 60:
            return min_distance_index, "EDM"
        elif 60 <= min_distance_index < 90:
            return min_distance_index, "Pop"
        else:
            return min_distance_index, "Género no disponible"
