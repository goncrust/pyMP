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
        for o in os.listdir(self.directory):
            found = False

            for l in self.dir_list:
                if o == l:
                    found = True

            if not found:
                file = o
                break

        extension = os.path.splitext(self.directory + o)

        if extension[1] == ".mp4":
            last = o
            o = o.replace(".mp4", ".mp3")

            os.rename(self.directory + last, self.directory + o)

        self.dir_list[o] = url

        return self.directory + o

    def delete(self):
        for m in os.listdir(self.directory):
            os.remove(self.directory + m)
