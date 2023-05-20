import matplotlib.pyplot as plt
import os
import numpy as np
import soundfile as sf
from IPython.display import Audio

class ProcessingFFT:
    def __init__(self, song_wav):
        self.x, self.fs = sf.read(song_wav)
        self.duration = len(self.x) / self.fs
        #print(f"Frecuencia de muestreo {self.fs:.2f}[Hz]\nAudio {song_wav} con duración {self.duration:.2f} segundos")
    
    def play_audio(self, duration):
        ns = duration
        Audio(self.x[:int(self.fs*ns),:].T,rate=self.fs)
    
    def plot_audio(self, ti, tf):
        xpro = self.x.copy()
        xs = xpro[int(ti*self.fs):int((tf*self.fs)),:]
        tt = np.arange(ti,tf,1/self.fs)
        plt.plot(tt,xs)
        plt.xlabel('$t[s]$')
        plt.ylabel('$x(t)$')
        plt.legend(('canal 1','canal 2'))
        plt.show()
        

    def plot_audio_spectrum(self, ti, tf):
        xpro = self.x.copy() #arreglo de la copia de la señal original
        xs = xpro[int(ti*self.fs):int((tf*self.fs)),:] #recorte temporal (tiempo[s])
        Xw = np.fft.rfft(xs,axis=0) #Se calcula FT de cada coloumna de xs
        vf = np.fft.rfftfreq(np.size(xs,0),1/self.fs) #vector de frecunecias (positivas)
        #print(f"Vector de frecuencias: {vf}")
        Xw_magnitude = np.abs(Xw) #Valor de las magnitudes
        Xw_magnitude_flat = np.ravel(Xw_magnitude) # Vectro en 1D
       # print(f"Vector de magnitud de la transformada de Fourier: {Xw_magnitude_flat}")
        #plt.plot(vf,Xw_magnitude_flat)
        #plt.xlabel(r'$f[Hz]$',fontsize = 14)
        #plt.ylabel(r'$|X[n]|$',fontsize = 14)
       # plt.title(r'Espectro audio original')
         #plt.show()
        return Xw_magnitude_flat
    



song_wav = "inputsong.wav"
fft_processor = ProcessingFFT(song_wav)
ti = 15
tf = 20
Xw_magnitude_song = fft_processor.plot_audio_spectrum(ti, tf)
print (Xw_magnitude_song)




folder_path = "C:\\Users\\Usuario\\Documents\\NATIONAL UNIVERSITY OF  COLOMBIA\ELECTRONIC ENGINEERING(MZ)\\7th SEMESTER (2023-1)MZ\\Signals and Systems\\Project 2023-1 Sys\\MultiBuck\\src\\wav_files" 

Xw_list = []  # lista vacía para almacenar los vectores de frecuencias

for file_name in os.listdir(folder_path):
    if file_name.endswith(".wav"):
        file_path = os.path.join(folder_path, file_name)
        audio_proc = ProcessingFFT(file_path)
        Xw_magnitude_flat = audio_proc.plot_audio_spectrum(15, 20)
        Xw_list.append(Xw_magnitude_flat)
np.savetxt("list_Xw.txt", Xw_list)
print (Xw_list)



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




"""
song_wav = "Adrenaline.wav"
ap = ProcessingFFT(song_wav)
ap.play_audio(30)
ap.plot_audio(10, 15)
ap.plot_audio_spectrum(10, 15)

"""

