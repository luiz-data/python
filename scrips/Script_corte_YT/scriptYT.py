#Script para fazer cortes no YouTube

from pytubefix import YouTube
import os, subprocess


# Entrada de dados
url = input("URL: ").strip()
inicio = input("Início (HH:MM:SS): ").strip()
fim = input("Fim (HH:MM:SS): ").strip()

# Converter tempos
def segundos(t): parts = [int(p) for p in t.split(':')]; return parts[0]*3600 + parts[1]*60 + parts[2] if len(parts)==3 else parts[0]*60 + parts[1] if len(parts)==2 else parts[0]
inicio_s, fim_s = segundos(inicio), segundos(fim)

# Download e recorte
yt = YouTube(url)
yt.streams.get_highest_resolution().download(filename="temp.mp4")
subprocess.run(['ffmpeg', '-i', 'temp.mp4', '-ss', str(inicio_s), '-to', str(fim_s), '-c', 'copy', '-y', 'video_recortado.mp4'], capture_output=True)
os.remove("temp.mp4")

print("✅ Vídeo recortado pronto!")
files.download("video_recortado.mp4")
