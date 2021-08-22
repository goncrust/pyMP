'''
pyMP (https://github.com/goncrust/pyMP)

YouTube audio downloader

Copyright (C) 2021 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

import youtube_dl
import os

def downloadYTURL(url, name, path=None, pl=False):
    
    # Set download options
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192', }]
    }
    
    # Set path
    if (path == None):
        ydl_opts['outtmpl'] = os.getcwd() + f'/{name}.mp3'
    else:
        if (not pl):

            # fix error "audio conversion failed: file:mp3: Invalid argument" (.mp3 not at end of path)
            if (path[len(path) - 4:] != ".mp3"):
                path = path + ".mp3"

            ydl_opts['outtmpl'] = path 
        else:
            ydl_opts['outtmpl'] = path + f'/{name}.mp3'
    
    # Download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        ydl.download([url])

