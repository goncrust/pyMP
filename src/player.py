import dl
import music_manager


class Player:

    def __init__(self):

        # downloader
        self.downloader = dl.Downloader()

        # manager
        self.temp_music_manager = music_manager.MusicManager("temp/")

        self.running = True
        self.loop()

    def loop(self):

        while self.running:

            command = input("> ")
            command = command.split(" ")

            if command[0] == "play":
                self.downloader.download(command[1], self.temp_music_manager)
