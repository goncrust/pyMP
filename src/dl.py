from pytube import YouTube
import os


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
