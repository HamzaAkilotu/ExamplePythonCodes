import pytube
from pytube.cli import on_progress
import os


def progress_callback(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    print(f"\rİndirme ilerlemesi: {percent:.2f}%", end="")


try:
    url = input("Enter video URL: ")
    path = "C:\\Users\\Hamza Akılotu\\OneDrive\\Desktop\\Ders-Yazılım\\Videos"

    yt = pytube.YouTube(url, on_progress_callback=progress_callback)

    stream = yt.streams.get_highest_resolution()

    if stream:
        print(f"İndirme başlıyor: {yt.title}")
        stream.download(output_path=path)
        print("\nVideo başarıyla indirildi!")
    else:
        print("Uygun video akışı bulunamadı.")
        
except Exception as e:
    print(f"\nBir hata oluştu: {e}")
