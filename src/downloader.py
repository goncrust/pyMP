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
    
    # Fix name errors
    if ("%" in name):
        name = name.replace("%", "")

    # Set path
    if (path == None):
        ydl_opts['outtmpl'] = os.getcwd() + f'/{name}.mp3'
    else:

        # No file name in path
        if (os.path.isdir(path) or pl):
            if (path[len(path) - 1] != "/"):
                path += "/"

            path += name + ".mp3"

        # Fix error "audio conversion failed: file:mp3: Invalid argument" (.mp3 not at end of path)
        if (path[len(path) - 4:] != ".mp3"):
            path += ".mp3"

        ydl_opts['outtmpl'] = path 
    
    # Download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        ydl.download([url])

