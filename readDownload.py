
import os
import yt_dlp as youtube_dl
import subprocess
import soundfile as sf




class list_converter_txt:
    def __init__(self, file_txt):
        self.file_txt = file_txt
    
    def list_converter(self):
        file = open(self.file_txt, "r")
        lines = file.readlines()
        file.close()
        lines = [line.strip() for line in lines]
        return lines
    
    
#links_songs = list_converter_txt("links_songs.txt")
#list_links = links_songs.list_converter()
#print(list_links)

#names_songs = list_converter_txt("name_songs.txt")
#list_names = names_songs.list_converter()
#print(list_names)



class DB_YT_Dowloader:
    
    def __init__(self, name_list, link_list):
        self.name_list = name_list
        self.link_list = link_list
        self.mp3_dir = 'mp3_files'
        self.wav_dir = 'wav_files'
        
        
        os.makedirs(self.mp3_dir, exist_ok=True)
        os.makedirs(self.wav_dir, exist_ok=True)
        
    def download_ytvid_as_mp3(self, video_url, name):
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False)
        filename = os.path.join(self.mp3_dir, f"{name}.mp3")
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:  
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
    
    def convert_to_wav(self, name):
        mp3_path = os.path.join(self.mp3_dir, name+'.mp3')
        wav_path = os.path.join(self.wav_dir, name+'.wav')
        subprocess.call(['ffmpeg', '-i', mp3_path, wav_path])
    
    def read_wav(self, name):
        wav_path = os.path.join(self.wav_dir, name+'.wav')
        x, fs = sf.read(wav_path)
        print('Frecuencia de muestreo %.2f[Hz]\naudio %s' % (fs,wav_path))
        return x, fs

    def download_and_convert_all(self):
        for name, link in zip(self.name_list, self.link_list):
            print(f"Downloading {name}...")
            self.download_ytvid_as_mp3(link, name)
            print(f"Converting {name} to WAV...")
            self.convert_to_wav(name)




#yt_downloader = DB_YT_Dowloader(list_names, list_links)
#yt_downloader.download_and_convert_all()

 

class SongDowloader(DB_YT_Dowloader):
    def __init__(self, video_url):
        super().__init__(["inputsong"], [video_url])
        code_dir = os.path.dirname(os.path.abspath(__file__))
        self.mp3_dir = os.path.join(code_dir, "inputsongs_mp3")
        self.wav_dir = os.path.join(code_dir, "inputsongs_wav")
        os.makedirs(self.mp3_dir, exist_ok=True)
        os.makedirs(self.wav_dir, exist_ok=True)

    def download_ytvid_as_mp3(self, video_url, name):
        code_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(code_dir, f"{name}.mp3")
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:  
            ydl.download([video_url])

        print("Download complete... {}".format(filename))
    
    def convert_to_wav(self, name):
        code_dir = os.path.dirname(os.path.abspath(__file__))
        mp3_path = os.path.join(code_dir, name+'.mp3')
        wav_path = os.path.join(code_dir, name+'.wav')
        subprocess.call(['ffmpeg', '-i', mp3_path, wav_path])
    
    def read_wav(self, name):
        code_dir = os.path.dirname(os.path.abspath(__file__))
        wav_path = os.path.join(code_dir, name+'.wav')
        x, fs = sf.read(wav_path)
        print('Frecuencia de muestreo %.2f[Hz]\naudio %s' % (fs,wav_path))
        return x, fs


#new_downloader =SongDowloader("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#new_downloader.download_and_convert_all()


