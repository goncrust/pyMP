from pytube import YouTube
import os
import subprocess
import json


class Downloader:

    def __init__(self):
        pass

    def download(self, url, manager):
        if not manager.check_existent(url):
            vid = YouTube(url)

            audio = vid.streams.filter(only_audio=True).first()
            audio.download("temp/")

            file = manager.register_new(url)

            return file

    def youtube_dl_query(self, keyword):
        query = os.popen(
            'youtube-dl -e -g --print-json "ytsearch5:' + keyword + '"').read()

        dic = query.split("\n")
        musics = {}

        i = 0
        while not (i >= (len(dic) - 1)):
            musics[dic[i]] = json.loads(dic[i+3])["webpage_url"]
            i += 4

        c = 1
        for m in musics:
            print(str(c) + ". " + m)
            c += 1

        option = int(input("Select one: "))

        current_opc = 1
        for e in musics:
            if current_opc == option:
                return musics[e]

            current_opc += 1
