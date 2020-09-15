import os


class MusicManager:

    def __init__(self, directory):
        self.directory = directory

        self.dir_list = {}

    def check_existent(self, url):
        for m in self.dir_list:
            if self.dir_list.get(m) == url:
                return True

        return False

    def register_new(self, url):

        file = None
        for o in os.listdir("temp/"):
            found = False

            for l in self.dir_list:
                if o == l:
                    found = True

            if not found:
                file = o
                break

        self.dir_list[o] = url
