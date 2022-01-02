'''
pyMP (https://github.com/goncrust/pyMP)

YouTube audio downloader

Copyright (C) 2022 goncrust
Released under the GPL v3.0
https://github.com/goncrust/pyMP/blob/master/LICENSE.md
'''

from yt_dlp import YoutubeDL
import utils
import os

def downloadYTURL(url, name, path=None, pl=False):
    """Download handler
    """


    def progress_hook(d):
        if d['status'] == 'downloading':
            db = d['downloaded_bytes']
            tb = d['total_bytes']
            per = (db/tb) * 100

            dm = utils.bytesToMegabytes(db)
            tm = utils.bytesToMegabytes(tb)
            print(f"Progress: {dm:.2f}MB/{tm:.2f}MB ({per:.1f}%)", end='\r')
        elif d['status'] == 'finished':
            f = d['filename']
            print(f"Finished downloading: {f}.\nConverting...")


    class DowloadLogger(object):
        def debug(self, msg):
            pass

        def warning(self, msg):
            pass

        def error(self, msg):
            print(msg)


    # Set download options
    ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'}],
            'logger': DowloadLogger(),
            'progress_hooks': [progress_hook]
    }
    
    # Fix name errors
    if "%" in name:
        name = name.replace("%", "")

    # Set path
    if path == None:
        ydl_opts['outtmpl'] = os.getcwd() + f'/{name}.mp3'
    else:

        # No file name in path
        if os.path.isdir(path) or pl:
            if (path[len(path) - 1] != "/"):
                path += "/"

            path += name + ".mp3"

        # Fix error "audio conversion failed: file:mp3: Invalid argument" (.mp3 not at end of path)
        if path[len(path) - 4:] != ".mp3":
            path += ".mp3"

        ydl_opts['outtmpl'] = path 
    
    # Download
    with YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        ydl.download([url])

