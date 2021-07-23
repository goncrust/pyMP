import youtube_dl
import os

def downloadYTURL(url, name, path=None, pl=False):
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', }]
    }
    
    if (path == None):
        ydl_opts['outtmpl'] = os.getcwd() + f'/{name}.mp3'
    else:
        if (not pl):
            ydl_opts['outtmpl'] = path 
        else:
            ydl_opts['outtmpl'] = path + f'/{name}.mp3'

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        ydl.download([url])

