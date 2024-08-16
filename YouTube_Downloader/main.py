import pytube
try:
    url = input("Enter video URL: ")
    path = "C:\\Users\\Hamza Akılotu\\OneDrive\\Desktop\\Ders-Yazılım\\Videos"
    pytube.YouTube(url).streams.get_by_resolution().download(path)
except:
    print("Bir hata oluştu.")