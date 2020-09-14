import dl


class Player:

    def __init__(self):
        self.downloader = dl.Downloader()

        self.running = True
        self.loop()

    def loop(self):

        while self.running:

            command = input("> ")
            command = command.split(" ")

            if command[0] == "play":
                self.downloader.download(command[1])
