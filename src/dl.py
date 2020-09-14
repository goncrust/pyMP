from pytube import YouTube


class Downloader:

    def __init__(self):
        pass

    def download(self, url):
        vid = YouTube(url)

        audio = vid.streams.filter(type="audio").first()

        audio.download()
