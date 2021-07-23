import youtube_dl
import os

def downloadYTURL(url, name, path=os.getcwd()):
    ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': path + f'/{name}.wav',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192', }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        ydl.download([url])
