

class Map:
    def __init__(self, width, height, name=""):
        self.width = width
        self.height = height
        self.name = name

    def on_update(self, step):
        print("Map {0} width: {1}, height: {2}".format(self.name, self.width, self.height))