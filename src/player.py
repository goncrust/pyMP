import dl
import music_manager
import vlc


class Player:

    def __init__(self):

        # downloader
        self.downloader = dl.Downloader()

        # manager
        self.temp_music_manager = music_manager.MusicManager("temp/")

        # vlc_player
        self.vlc_player = None

        self.running = True
        self.loop()

    def loop(self):

        while self.running:

            command = input("> ")

            command = command.split(" ")

            self.command(command)

    def command(self, command):

        if command[0] == "play":

            if command[1] == "-u":
                file = self.downloader.download(
                    command[2], self.temp_music_manager)
            else:
                c = 0
                keyword = ""
                for s in command:
                    if c != 0:
                        keyword += s
                    c += 1

                url = self.downloader.youtube_dl_query(keyword)
                file = self.downloader.download(
                    url, self.temp_music_manager)

            self.vlc_player = vlc.MediaPlayer(file)
            self.vlc_player.play()

        elif command[0] == "download":
            pass
            # future

        elif command[0] == "quit":

            self.vlc_player.stop()

            self.temp_music_manager.delete()

            self.running = False
